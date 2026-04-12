# 12 Most Common FITq Failure Modes — Template Fixes

**Used by:** `optise-helix-fitq-audit` exclusively.
**Purpose:** When the audit identifies a common failure, the skill outputs the template fix verbatim — no inventing new fixes per page. Templates are validated against the Optise EU AEO Playbook, Sections 4-5.

## Contents
- 1. No visible last-updated date
- 2. Page is JS-gated (content not in raw HTML)
- 3. H1 doesn't mirror a real buyer prompt
- 4. No BLUF in the first 100 words
- 5. Wall-of-text body (no tables, lists, FAQs)
- 6. Anonymous author / no byline
- 7. Stats with no source links
- 8. No FAQ schema markup
- 9. Marketing copy at the top, answer below the fold
- 10. Pricing missing from a comparison page
- 11. No "not ideal for" / honesty section
- 12. Bot-blocking via robots.txt or Cloudflare challenge

---

## Failure 1 — No visible last-updated date

**Detection:** `fetch_page.py` returns `last_updated.found = False`
**Trust score impact:** -10 to -15 points
**Effort:** 30 minutes (one-time, then automate via CMS)

**Template fix:**

Add this immediately below the H1:

```html
<p class="last-updated">
  <time datetime="2026-04-12">Last updated: April 12, 2026</time>
</p>
```

For dynamic CMS injection (preferred), use the CMS's "last modified" field and surface it visibly. The date must be:
- Visible to a sighted reader (not in `<meta>` only)
- Inside a `<time datetime="...">` tag for AI engine extraction
- Updated whenever content materially changes (not just on every save)

**Why this matters:** Per the FITq rubric, Trust signal scores ≤15 if there's no date or the date is stale (>90 days). AI engines use freshness as a primary trust filter.

---

## Failure 2 — Page is JS-gated

**Detection:** `fetch_page.py` returns `js_gating.js_gated = True`
**Findability score impact:** Capped at 5/25
**Effort:** 1-4 weeks (engineering work)

**Template fix:**

This is a structural fix, not a content fix. The page must render in raw HTML on first byte. Three options:

1. **Server-side rendering (SSR):** Convert the page from client-side React/Vue to SSR. For Next.js use `getServerSideProps` or app router. For Nuxt use `asyncData`. For React without a framework, deploy via something like Vercel ISR.
2. **Static pre-rendering:** If the content doesn't change per-user, pre-render at build time. Faster than SSR. Most decision pages (alternatives, pricing, trust centre) qualify.
3. **Hybrid:** Render the answer block server-side, hydrate the rest client-side. Lowest engineering effort if the site is mostly client-side already.

**Until this is fixed, no other AEO work matters.** AI engines see almost nothing on a JS-gated page.

---

## Failure 3 — H1 doesn't mirror a real buyer prompt

**Detection:** `fetch_page.py` returns H1 text. The skill compares against the target prompt (if provided) or against the page's URL slug. Generic H1s like "Welcome to [Brand]" or "[Brand] Service Desk" fail this check.
**Intent Match score impact:** -5 to -15 points
**Effort:** 10 minutes per page

**Template fix:**

Replace generic H1 with a question-form H1 that mirrors the buyer prompt.

**Before:**
```html
<h1>Freshservice — IT Service Management</h1>
```

**After:**
```html
<h1>Best service desk software for German Mittelstand IT teams</h1>
```

If the page covers multiple buyer questions, lead with the highest-volume one in the H1 and use H2s for the others.

---

## Failure 4 — No BLUF in the first 100 words

**Detection:** The first 100 words of body text don't contain a direct, self-contained answer to the H1's implicit question.
**Intent Match + Quoteability score impact:** -10 points combined
**Effort:** 30 minutes per page

**Template fix:**

Insert a 40-60 word BLUF immediately after the H1, before any marketing copy.

**Before:**
```
[H1] Best service desk software for German Mittelstand IT teams
[Marketing hero copy]
[Subheading]
[More marketing]
[Eventually, the answer 800 words down]
```

**After:**
```
[H1] Best service desk software for German Mittelstand IT teams
[BLUF — 40-60 words] For German Mittelstand IT teams (200-2000 employees), the three best service desk options in 2026 are Freshservice (best for fast deployment, BSI C5 certified), ServiceNow (best for complex enterprise stacks, premium pricing), and OTRS (best for full data sovereignty, German vendor).
[Then the rest of the page]
```

The BLUF must:
- Be 40-60 words (not 30, not 80)
- Answer the H1's implicit question directly
- Name the top 3 options or the single recommendation
- Be self-contained (extractable as a single quote)
- Use the buyer's own framing, not marketing language

→ Hand off to `optise-helix-bluf-writer` for help drafting the actual text.

---

## Failure 5 — Wall-of-text body

**Detection:** `fetch_page.py` reports paragraphs >> headings/tables/lists. Specifically: paragraph count > 30 AND (table count + list count) < 5.
**Quoteability score impact:** -10 to -15 points
**Effort:** 1-2 hours per page

**Template fix:**

Convert paragraph prose to structured answer blocks. Each block:
- Question-style H2 heading
- 1-sentence direct answer
- 2-3 bullet supporting points OR a short table
- Optional 1-sentence proof statement with a source link

**Before:**
```
[800 words of paragraph prose explaining pricing]
```

**After:**
```
## How much does [tool] cost for German Mittelstand?

Pricing starts at €X per agent per month for the Starter plan and scales to €Y for Enterprise.

| Plan | Price (per agent/month) | Best for |
|---|---|---|
| Starter | €X | <50 agents |
| Pro | €Y | 50-200 agents |
| Enterprise | €Z | 200+ agents, custom SLAs |

All EU customers can request annual billing in EUR. Volume discounts available above 100 agents.
```

---

## Failure 6 — Anonymous author / no byline

**Detection:** No `<author>`, no schema.org `Person`, no visible "By [Name]" text.
**Trust score impact:** -5 to -10 points
**Effort:** 15 minutes per page

**Template fix:**

Add a byline with a real named person and link to a bio:

```html
<p class="byline">
  By <a href="/team/alex-mueller" rel="author">Alex Müller</a>,
  Head of IT Operations at [Company]
</p>
```

If no real person is appropriate (e.g., it's a product page), at minimum use:

```html
<p class="byline">By the [Company] Product Team. Last reviewed by <a href="/team/cto">[CTO Name]</a>.</p>
```

**Never use:** "By [Brand] Team" with no link. AI engines treat this as no byline at all.

---

## Failure 7 — Stats with no source links

**Detection:** Page contains numeric claims (e.g., "85% of users", "saves 20 hours/week") without `<a href>` to a source.
**Trust score impact:** -5 to -10 points
**Effort:** 20 minutes per page

**Template fix:**

Every quantitative claim must link to its source. Pattern:

**Before:**
```
85% of customers report faster ticket resolution.
```

**After:**
```
85% of customers report faster ticket resolution
(<a href="/case-studies/freshservice-2026-customer-survey">2026 Customer Survey, n=1,247</a>).
```

If the source is internal, link to a named methodology page. If the source is external, link to the original (not an aggregator). If the stat has no defensible source, **drop the stat** rather than weaken it with vague attribution.

---

## Failure 8 — No FAQ schema markup

**Detection:** `fetch_page.py` returns `schema_markup` without a `FAQPage` entry, but the page contains 3+ Q&A-style headings.
**Quoteability score impact:** -5 to -10 points
**Effort:** 30 minutes (one-time per page template)

**Template fix:**

Add JSON-LD `FAQPage` schema in the `<head>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is [tool] GDPR compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. [Tool] is GDPR-compliant and operates as both a Data Processor and Data Controller under EU Regulation 2016/679. Our DPA is available at [URL]."
      }
    },
    {
      "@type": "Question",
      "name": "Where is customer data stored?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Customer data is stored in our EU regions: Frankfurt (primary) and Dublin (failover). Data does not leave the EU without explicit customer instruction."
      }
    }
  ]
}
</script>
```

The schema must mirror visible page content (don't add Q&A pairs only in the schema — Google penalizes this).

---

## Failure 9 — Marketing copy at top, answer below the fold

**Detection:** First 100 words of body text contain marketing language ("revolutionary", "leading", "world-class", "transform") but no direct answer to the page's implicit question.
**Intent Match score impact:** -10 to -15 points
**Effort:** 30 minutes per page

**Template fix:**

Move the answer above the marketing. The page should answer the buyer's question first, then expand into the brand story (if at all). Marketing language is allowed below the answer block, not before it.

This is the same fix as Failure 4 (BLUF) but applied to pages that have an answer somewhere — just not in the right place.

---

## Failure 10 — Pricing missing from a comparison page

**Detection:** Page is a `/compare/*`, `/alternatives/*`, or `/vs/*` URL but contains no pricing information for the user's product OR for the competitors.
**Intent Match score impact:** -10 points (this is a deal-breaker for AEO citation on pricing prompts)
**Effort:** 30 minutes per page

**Template fix:**

Add a pricing comparison table. If you don't disclose your pricing publicly, at minimum show pricing model differences:

```markdown
| Tool | Pricing model | Starting price | Free trial |
|---|---|---|---|
| [You] | Per agent/month | €29/agent/month | 14 days |
| [Competitor 1] | Per agent/month + setup fee | €45/agent/month + €5,000 | 21 days |
| [Competitor 2] | Tiered packages | "Contact sales" | None |
```

**Why this matters:** Comparison pages without pricing get filtered out of AI engine citation chains. AI engines treat pricing as a structural completeness signal, not just user-relevant info.

---

## Failure 11 — No "not ideal for" section

**Detection:** Page makes only positive claims. No section explicitly stating who shouldn't use the product.
**Trust score impact:** -5 points (and a major RACE failure when that audit runs)
**Effort:** 20 minutes per page

**Template fix:**

Add a "Not ideal for" section near the bottom of decision pages:

```markdown
## Who [tool] is not ideal for

- **Companies under 20 employees:** Our pricing model assumes 20+ agents. Smaller teams should look at [smaller competitor] instead.
- **Healthcare providers needing on-prem deployment:** We're SaaS-only. For on-prem health-tech, [on-prem competitor] is a better fit.
- **Companies that need real-time call recording:** We focus on tickets and chat. For voice-led support, [voice tool] is better.
```

Honest constraints are a trust signal. AI engines and procurement teams trust products that admit their limits.

---

## Failure 12 — Bot-blocking via robots.txt or Cloudflare

**Detection:** `fetch_page.py` returns 403 even with the ChatGPT-User UA, OR robots.txt blocks GPTBot/ClaudeBot/PerplexityBot.
**Findability score impact:** 0/25 — page is invisible
**Effort:** 5 minutes (robots.txt) to a few hours (Cloudflare config)

**Template fix:**

Robots.txt — explicitly allow AI crawlers:
```
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
```

Cloudflare — disable "Block AI Bots" in the dashboard, OR add a Page Rule that whitelists AI crawler UAs. If you're worried about content scraping, use the `nosnippet` meta tag for selective sections instead of blocking entire crawlers.

**Until this is fixed, no other AEO work matters.** Bot-blocking is the most common silent killer of AI citation.
