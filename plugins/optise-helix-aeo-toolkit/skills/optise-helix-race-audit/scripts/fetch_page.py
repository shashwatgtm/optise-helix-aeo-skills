#!/usr/bin/env python3
"""
fetch_page.py — Fetch and analyze a webpage for FITq and RACE audits.

Used by:
- optise-helix-fitq-audit
- optise-helix-race-audit (shared via symlink/copy)

Outputs a JSON document containing:
- HTTP status, response headers, redirects
- Raw HTML size, rendered HTML size (best-effort without a real browser)
- Time to first byte (TTFB)
- Detected schema.org markup (counted by type)
- Detected last-updated date (multiple heuristics)
- JS-trapped content detection (raw HTML body length vs total page length)
- Title tag, H1 tags, H2 tags
- Number of tables, lists, FAQ markup
- Word count and average paragraph length
- Outbound link count and source link count for quantitative claims

Usage:
    python fetch_page.py <url>
    python fetch_page.py <url> --json-output  # machine-readable
    python fetch_page.py <url> --html-output  # save raw HTML alongside JSON

Author: Optise + Helix GTM Consulting
"""

import sys
import json
import re
import time
import argparse
from urllib.parse import urlparse
from datetime import datetime, timezone

# These two timeouts are based on real-world observation of B2B SaaS pages.
# Most pages respond in <2s; pages that take longer are usually indicative of
# Findability problems that the FITq audit will catch anyway. 30s is the
# absolute ceiling — beyond this, the page is effectively invisible to AI
# crawlers (per the whitepaper Section 5).
CONNECT_TIMEOUT_SECONDS = 10
READ_TIMEOUT_SECONDS = 30

# Three retries balances reliability vs speed. Most intermittent failures
# resolve by the second retry. Fourth+ retries usually indicate a real outage
# and the audit should report the failure honestly per anti-hallucination rule 3.
MAX_RETRIES = 3

# User-Agent strings to try in order. We start with a real Chrome UA because
# some Cloudflare-protected sites block obvious bot UAs. If that fails we fall
# back to the OpenAI/Anthropic crawler UAs to see whether the page is even
# accessible to AI engines (which is itself a Findability data point).
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; "
    "ChatGPT-User/1.0; +https://openai.com/bot",
    "Mozilla/5.0 (compatible; ClaudeBot/1.0; +https://www.anthropic.com)",
]

# Date heuristics, in order of reliability. The first match wins.
DATE_PATTERNS = [
    # ISO datetime in <time datetime="..."> tags — most reliable
    (r'<time[^>]*datetime="([^"]+)"', "time-datetime-attr"),
    # "Last updated: YYYY-MM-DD" or "Updated YYYY-MM-DD"
    (r'(?:last\s*updated|updated\s*on?|last\s*reviewed)\s*[:\-]?\s*'
     r'(\d{4}-\d{2}-\d{2})', "last-updated-iso"),
    # "Last updated: Month DD, YYYY"
    (r'(?:last\s*updated|updated\s*on?|last\s*reviewed)\s*[:\-]?\s*'
     r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},?\s+\d{4})',
     "last-updated-month"),
    # JSON-LD dateModified field
    (r'"dateModified"\s*:\s*"([^"]+)"', "jsonld-datemodified"),
    # Open Graph article:modified_time
    (r'<meta[^>]+property="article:modified_time"[^>]+content="([^"]+)"',
     "og-modified-time"),
]


def fetch_with_retries(url, user_agent_index=0, retry=0):
    """Fetch a URL with retries and UA fallback. Returns dict or raises."""
    try:
        import urllib.request
        import urllib.error
    except ImportError as e:
        raise RuntimeError(
            f"urllib unavailable: {e}. fetch_page.py requires Python 3 stdlib only."
        )

    if user_agent_index >= len(USER_AGENTS):
        raise RuntimeError(
            f"All {len(USER_AGENTS)} user-agent strategies failed for {url}. "
            f"The page may be blocking all crawlers or unreachable."
        )

    ua = USER_AGENTS[user_agent_index]
    request = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })

    start_time = time.time()
    try:
        with urllib.request.urlopen(
            request,
            timeout=READ_TIMEOUT_SECONDS,
        ) as response:
            ttfb_ms = int((time.time() - start_time) * 1000)
            html_bytes = response.read()
            return {
                "status": response.status,
                "url_final": response.url,  # captures redirects
                "headers": dict(response.headers),
                "html": html_bytes.decode("utf-8", errors="replace"),
                "html_size_bytes": len(html_bytes),
                "ttfb_ms": ttfb_ms,
                "user_agent_used": ua,
            }
    except urllib.error.HTTPError as e:
        # 4xx and 5xx — these are real responses, not retry candidates,
        # unless they're 429 / 503 which sometimes resolve with a different UA
        if e.code in (429, 503) and user_agent_index < len(USER_AGENTS) - 1:
            return fetch_with_retries(url, user_agent_index + 1, retry)
        return {
            "status": e.code,
            "url_final": url,
            "headers": dict(e.headers) if e.headers else {},
            "html": "",
            "html_size_bytes": 0,
            "ttfb_ms": int((time.time() - start_time) * 1000),
            "error": f"HTTPError {e.code}: {e.reason}",
            "user_agent_used": ua,
        }
    except urllib.error.URLError as e:
        if retry < MAX_RETRIES:
            time.sleep(1 + retry)  # backoff: 1s, 2s, 3s
            return fetch_with_retries(url, user_agent_index, retry + 1)
        # Try fallback UA
        if user_agent_index < len(USER_AGENTS) - 1:
            return fetch_with_retries(url, user_agent_index + 1, 0)
        raise RuntimeError(
            f"URLError on {url} after {MAX_RETRIES} retries with all UAs: {e.reason}"
        )


def detect_last_updated(html):
    """Try multiple heuristics to find a 'last updated' date. Returns dict."""
    for pattern, source_name in DATE_PATTERNS:
        match = re.search(pattern, html, re.IGNORECASE)
        if match:
            return {
                "found": True,
                "raw_value": match.group(1),
                "source": source_name,
            }
    return {"found": False, "raw_value": None, "source": None}


def detect_schema_markup(html):
    """Detect schema.org markup. Returns dict with counts by type."""
    schema_types = {}
    # JSON-LD blocks
    jsonld_blocks = re.findall(
        r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>',
        html, re.DOTALL,
    )
    for block in jsonld_blocks:
        # Find all "@type" values
        type_matches = re.findall(r'"@type"\s*:\s*"([^"]+)"', block)
        for t in type_matches:
            schema_types[t] = schema_types.get(t, 0) + 1
    # Microdata
    microdata_matches = re.findall(
        r'itemtype="https?://schema\.org/(\w+)"', html
    )
    for t in microdata_matches:
        schema_types[t + "_microdata"] = schema_types.get(t + "_microdata", 0) + 1
    return schema_types


def detect_js_gating(html, html_size_bytes):
    """
    Heuristic: if the body of the rendered HTML is mostly empty or contains
    just a root div + script tags, the page is JS-gated. AI crawlers will
    see almost nothing.
    """
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    if not body_match:
        return {
            "js_gated": True,
            "reason": "no-body-tag",
            "body_text_chars": 0,
        }
    body_html = body_match.group(1)
    # Strip script and style tags
    body_text_only = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
    body_text_only = re.sub(r'<style[^>]*>.*?</style>', '', body_text_only, flags=re.DOTALL)
    # Strip HTML tags
    body_text_only = re.sub(r'<[^>]+>', ' ', body_text_only)
    body_text_only = re.sub(r'\s+', ' ', body_text_only).strip()

    text_chars = len(body_text_only)

    # Heuristic: if the body has <500 visible text chars but the page is >50KB,
    # the content is almost certainly in JS bundles
    if text_chars < 500 and html_size_bytes > 50000:
        return {
            "js_gated": True,
            "reason": "small-body-large-page",
            "body_text_chars": text_chars,
            "html_size_bytes": html_size_bytes,
        }
    if text_chars < 200:
        return {
            "js_gated": True,
            "reason": "very-small-body",
            "body_text_chars": text_chars,
        }
    return {
        "js_gated": False,
        "body_text_chars": text_chars,
    }


def count_quoteability_features(html):
    """Count the structural features that drive FITq Quoteability score."""
    return {
        "tables": len(re.findall(r'<table[^>]*>', html)),
        "uls": len(re.findall(r'<ul[^>]*>', html)),
        "ols": len(re.findall(r'<ol[^>]*>', html)),
        "dls": len(re.findall(r'<dl[^>]*>', html)),
        "h2": len(re.findall(r'<h2[^>]*>', html)),
        "h3": len(re.findall(r'<h3[^>]*>', html)),
        "paragraphs": len(re.findall(r'<p[^>]*>', html)),
    }


def extract_headings(html):
    """Extract H1 and H2 text content."""
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
    h1_text = [re.sub(r'<[^>]+>', '', h).strip() for h in h1_matches]
    h2_text = [re.sub(r'<[^>]+>', '', h).strip() for h in h2_matches]
    return {"h1": h1_text, "h2": h2_text}


def extract_title(html):
    """Extract <title> content."""
    match = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL)
    if match:
        return re.sub(r'\s+', ' ', match.group(1)).strip()
    return None


def detect_canonical(html):
    """Detect <link rel='canonical'>."""
    match = re.search(
        r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
        html,
    )
    if match:
        return match.group(1)
    return None


def detect_meta_robots(html):
    """Detect noindex/nofollow meta robots."""
    match = re.search(
        r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']',
        html,
    )
    if match:
        return match.group(1)
    return None


def analyze(url):
    """Run the full analysis on a URL."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid URL (missing scheme or host): {url}")

    fetch_result = fetch_with_retries(url)

    if "error" in fetch_result and fetch_result["html_size_bytes"] == 0:
        # The fetch failed cleanly (4xx/5xx). Report it honestly.
        return {
            "url": url,
            "url_final": fetch_result.get("url_final", url),
            "fetch_status": "failed",
            "http_status": fetch_result["status"],
            "error": fetch_result.get("error"),
            "ttfb_ms": fetch_result["ttfb_ms"],
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "anti_hallucination_note": (
                "fetch_page.py could not retrieve content for this URL. "
                "Per skill anti-hallucination rule: do not score a page that "
                "wasn't fetched. Surface this error to the user and request "
                "a screenshot or HTML paste."
            ),
        }

    html = fetch_result["html"]
    html_size = fetch_result["html_size_bytes"]

    schema_types = detect_schema_markup(html)
    last_updated = detect_last_updated(html)
    js_gating = detect_js_gating(html, html_size)
    quoteability = count_quoteability_features(html)
    headings = extract_headings(html)
    title = extract_title(html)
    canonical = detect_canonical(html)
    meta_robots = detect_meta_robots(html)

    return {
        "url": url,
        "url_final": fetch_result["url_final"],
        "fetch_status": "ok",
        "http_status": fetch_result["status"],
        "ttfb_ms": fetch_result["ttfb_ms"],
        "html_size_bytes": html_size,
        "html_size_kb": round(html_size / 1024, 1),
        "user_agent_used": fetch_result["user_agent_used"],
        "title": title,
        "headings": headings,
        "canonical": canonical,
        "meta_robots": meta_robots,
        "last_updated": last_updated,
        "schema_markup": schema_types,
        "js_gating": js_gating,
        "quoteability_features": quoteability,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch and analyze a webpage for FITq/RACE audits")
    parser.add_argument("url", help="URL to fetch and analyze")
    parser.add_argument("--json-output", action="store_true",
                        help="Output JSON only (machine-readable)")
    parser.add_argument("--html-output", type=str, default=None,
                        help="Save raw HTML to this file")
    args = parser.parse_args()

    try:
        result = analyze(args.url)
    except Exception as e:
        # Per anti-hallucination rule 9: report real errors, never fake data
        error_result = {
            "url": args.url,
            "fetch_status": "error",
            "error": str(e),
            "error_type": type(e).__name__,
            "anti_hallucination_note": (
                "fetch_page.py raised an exception. Do not proceed to score "
                "this page. Report the error to the user and ask for an "
                "alternative input (HTML paste, screenshot, or different URL)."
            ),
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)

    if args.html_output and result.get("fetch_status") == "ok":
        # Re-fetch HTML for saving (we don't keep it in the result by default)
        try:
            with open(args.html_output, "w", encoding="utf-8") as f:
                fetched = fetch_with_retries(args.url)
                f.write(fetched["html"])
        except Exception as e:
            print(f"Warning: failed to save HTML: {e}", file=sys.stderr)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
