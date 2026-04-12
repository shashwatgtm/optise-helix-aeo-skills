---
name: optise-helix-fitq-audit
description: Audits a B2B webpage against the proprietary Optise FITq™ framework 
  (Findability, Intent match, Trust, Quoteability) to determine AI search 
  citation readiness for ChatGPT, Perplexity, Gemini, and Claude. Fetches the 
  URL, analyzes rendered HTML, and returns specific fixes ranked by impact — 
  not generic best practices. Use whenever the user asks for an AEO audit, FITq 
  audit, AI visibility check, ChatGPT citation readiness check, or wants to 
  know why their page isn't being cited by AI engines. Always trigger for any 
  URL audit request related to AI search visibility. Returns a 4-signal 
  scorecard (0-100 total), top 5 fixes ranked by impact, and a before/after 
  diff for the highest-priority fix. Authored by Optise + Helix GTM Consulting 
  under the Optise EU AEO Playbook methodology.
authors:
  - Optise
  - Helix GTM Consulting
version: 1.0.0
license: Proprietary
---

# Optise–Helix FITq™ Audit

A skill that audits any B2B webpage against the proprietary Optise FITq™ framework and returns specific, ranked fixes to make the page citable by ChatGPT, Perplexity, Gemini, Claude, and Google AI Overviews.

FITq™ stands for Findability, Intent match, Trust, and Quoteability — the four signals AI engines use to select sources. Each signal scores 0-25 for a 100-point total, mapped to A/B/C/D/F grade bands. Full scoring rubric is in `references/fitq-rubric.md`.

This skill is the headline FITq audit in the Optise-Helix AEO toolkit. It depends on `scripts/fetch_page.py` for URL fetching and structural analysis.

---

## Section 1 — Golden Rule

**Never score a page that wasn't successfully fetched, and never invent fixes that aren't in the 12-failure-mode template library or that the user's actual page evidence doesn't justify.** A page that fails fetch gets a fetch-error report, not a fabricated score. A page that scores well gets honest credit, not manufactured fixes for padding.

---

## Section 2 — Role / Context Detection

Detect persona using `references/personas.md`. Adapt output as follows:

| Persona | Output adaptation |
|---|---|
| **CEO / Founder** | One-page max. Lead with the grade band as a single statement ("F — invisible to AI engines"). Strip the "FITq" jargon — call it "the 4-signal scorecard." Skip the per-signal breakdown unless asked. Close with a CFO-grade ask: "To move from F to B, budget [N] weeks." |
| **Marketing / Growth Lead (default)** | Full scorecard + per-signal breakdown + top 5 fixes split by ship-this-week vs ship-this-month + before/after diff for fix #1 + "what's already strong" closing. Use Optise terminology (FITq, BLUF, RACE). |
| **Web Team** | Same as Marketing but with URL slugs in handoff suggestions, raw HTML diffs (not prose descriptions of fixes), and explicit code blocks for every fix. Skip the marketing framing entirely. |
| **RevOps / Sales Ops** | Add a "what to track in CRM" line per fix. Otherwise same as Marketing. |
| **Security / Privacy / Legal** | Filter to Trust signal findings only. Hand off to `optise-helix-eu-trust-centre` if Trust score < 15. |

**Detection signals:** see `references/personas.md`. Default = Marketing/Growth Lead.

**Platform mode:**
- **Connected mode:** memory contains the company's prior audit context → reference it ("Last audit was X. Has Y changed?")
- **Manual / API mode:** structured JSON in/out, skip persona detection
- **Mixed mode:** use what memory has, ask only for missing fields

**Urgency:** If the user says "quick" or "what's the #1 thing wrong" → return ONE finding (the lowest-scored signal's top fix), no full scorecard.

---

## Section 3 — Priority Framework

When ranking fixes for the top 5, use this order:

1. **Findability blockers (0/25 or near-zero)** — These cap all other signals. Always #1 if present. Fix: enable rendering, unblock crawlers, fix robots.txt.
2. **Intent Match gaps where the H1 doesn't mirror the buyer prompt** — Fix the H1 first; everything else cascades.
3. **Trust gaps that are quick wins** — Last-updated date, byline. 30-minute fixes that move score 10+ points.
4. **Quoteability gaps** — Add tables, FAQ schema, restructure walls of text into answer blocks.
5. **Trust gaps that require third-party work** — Source links to G2/Reddit/customer cases. Slower, lower priority.

**Tie-breakers:**
1. **Effort wins.** A 30-minute fix worth 10 points beats a 2-week fix worth 12 points.
2. **Foundational fixes win.** Findability and BLUF unblock other signals — they belong above pure-Quoteability fixes even when raw scores are similar.
3. **EU compliance wins in EU markets.** If the user is selling into EU and Trust includes a missing GDPR disclosure, that fix moves up the list.

---

## Section 4 — Workflow Steps

### Step 0: Detect mode

Detect whether this is:
- **URL audit** (default) — user supplied a URL → fetch + score
- **HTML paste audit** — user pasted HTML → skip fetch, score directly with a note about partial Findability scoring
- **Re-audit** — user asks "did my fix work" → fetch the same URL, compare the new fetch_page output against memory, report deltas

### Step 1: Capture inputs

**Required:** URL (or HTML).
**Optional:** target prompt (anchors the Intent Match check), page type (alternatives/comparison/pricing/trust/etc.), EU market context.

**Failure mode:** If no URL or HTML → ask 1 question: *"Which URL? I need a specific page, not a homepage. Most useful: your highest-value decision page (alternatives, comparison, pricing, or trust centre)."*

### Step 2: Detect persona

Use `references/personas.md`. Confirm at top of output: *"Built for: [persona]."* Skip in manual mode.

### Step 3: Run fetch_page.py

```bash
python scripts/fetch_page.py <URL>
```

Capture the JSON output. The schema you can rely on:

| Field | Type | Used by which signal |
|---|---|---|
| `fetch_status` | "ok" / "failed" / "error" | All — halt if not "ok" |
| `http_status` | int | Findability (200 = +5, 4xx/5xx = 0) |
| `ttfb_ms` | int | Findability (<2000 = +5, 2000-5000 = +2, >5000 = 0) |
| `html_size_bytes` | int | Findability (<1.5MB = +5, 1.5-3MB = +2, >3MB = 0) |
| `title` | string | Intent Match (mirrors prompt = +5) |
| `headings.h1` | list of strings | Intent Match (question-form = +5, brand-led = -10) |
| `headings.h2` | list of strings | Quoteability (question-form H2s = +4) |
| `canonical` | string or null | Findability (present = +5) |
| `meta_robots` | string or null | Findability (noindex = 0) |
| `last_updated.found` | bool | Trust (true within 90d = +8, true stale = +4, false ≤+0) |
| `last_updated.raw_value` | string or null | Trust (parse for recency check) |
| `schema_markup` | dict of {type: count} | Quoteability (FAQPage = +6, Article/Org = +4) |
| `js_gating.js_gated` | bool | Findability (true = cap at 5/25; other signals capped at "cannot score") |
| `quoteability_features.tables` | int | Quoteability (≥2 = +4) |
| `quoteability_features.uls + ols + dls` | int | Quoteability (≥5 = +4) |
| `quoteability_features.paragraphs` | int | Quoteability (≤30 with ≥5 lists = healthy structure) |
| `quoteability_features.h2` | int | Used together with `headings.h2` for question-form check |

If `fetch_status != "ok"`, halt the workflow and output the error per the Golden Rule.

**Failure mode:** Fetch failed → output the error with the user-facing explanation from `references/anti-hallucination-base.md` rule 3. Never proceed to scoring.

### Step 4: Score against the 4 FITq signals

Use `references/fitq-rubric.md`. For each signal, compute 0-25 based on the structured data from fetch_page.py:

**Findability (0-25):**
- HTTP 200 + content in raw HTML body + TTFB < 2000ms + canonical present + not blocked by robots → 25
- One issue → -5
- JS-gated body OR robots blocking → cap at 5
- 4xx/5xx → 0

**Intent Match (0-25):**
- H1 mirrors target prompt (or is question-form if no target prompt provided) → +10
- BLUF in first 100 words of body → +10
- Page stays on a single decision topic → +5
- Generic brand H1 → -10
- Off-topic body → -10

**Trust (0-25):**
- Visible last-updated date within 90 days → +8
- Date present but stale (>90 days) → +4
- Named author byline → +5
- Quantitative claims sourced → +5
- Schema.org Article/Organization markup → +4
- E-E-A-T signals (author bio, expertise) → +3

**Quoteability (0-25):**
- 2+ tables OR 5+ structured lists → +8
- FAQ schema present → +6
- Average paragraph length ≤ 4 sentences → +5
- H2 headings are question-form → +4
- BLUF is extractable as a single quote → +2

### Step 5: Rank top 5 fixes

Apply Priority Framework from Section 3. Each fix gets:
- Source signal it improves
- Estimated point gain
- Effort estimate (ship-this-week / ship-this-month)
- Template from `references/common-fixes.md` if it matches one of the 12 known failure modes

**Failure mode:** If the page scores 90+, do NOT manufacture 5 fixes. Output "no critical fixes — page is citation-ready" and list optional improvements only.

### Step 6: Build the before/after diff for fix #1

Show the actual HTML or copy change. If fix #1 is "add a last-updated date", show the exact HTML snippet. If it's "rewrite the H1", show the current H1 and the proposed H1.

### Step 7: Build the "what's already strong" section

For every signal scored 18+/25, name what's working. This prevents the user from breaking what already works.

### Step 8: Format output per persona

Use Section 5 format. Always include the score, breakdown, top fixes, before/after diff, and "what's already strong."

### Step 9: Hand off to next skill

- If Trust < 15 AND user is in EU markets → recommend `optise-helix-eu-trust-centre`
- If Intent Match gap is "no BLUF" → recommend `optise-helix-bluf-writer`
- If user asks "now what" after the audit → recommend `optise-helix-race-audit` for agent-readiness
- If user wants to track whether the fixes worked → recommend `optise-helix-aeo-tracker`

---

## Section 5 — Output Format (with Concrete Examples)

### Standard format (Marketing persona, default)

```markdown
**Built for:** [persona]
**URL audited:** [url]
**Audit timestamp:** [ISO timestamp from fetch_page.py]

## FITq™ Score: [N]/100 — Grade [A-F]

| Signal | Score | What's driving it |
|---|---|---|
| Findability | X/25 | [1-line explanation] |
| Intent Match | X/25 | [1-line explanation] |
| Trust | X/25 | [1-line explanation] |
| Quoteability | X/25 | [1-line explanation] |

## Top 5 fixes (ranked by impact)

### Fix 1 — [name] [+N points] [ship this week]
[1-paragraph explanation]
[before/after diff]

### Fix 2-5
[same format, shorter]

## What's already strong (don't break these)
- [strength 1]
- [strength 2]

## Suggested next step
[Hand off recommendation]
```

### Example 1 — Happy path (Marketing lead, semrush.com)

> **Built for:** Marketing / Growth Lead
> **URL audited:** https://www.semrush.com/features/site-audit/
> **Audit timestamp:** 2026-04-12T11:23:47Z
>
> ## FITq™ Score: 78/100 — Grade B
>
> | Signal | Score | What's driving it |
> |---|---|---|
> | Findability | 23/25 | Renders fully in HTML, TTFB 240ms, canonical present, no bot blocks. -2 for 2.1MB page weight. |
> | Intent Match | 18/25 | H1 is "Site Audit Tool" — descriptive but not question-form. BLUF present in first 80 words. Stays on topic. |
> | Trust | 17/25 | Last-updated date present (2026-03-14, within 90 days). No named author byline (uses "Semrush Team"). Stats sourced to internal Semrush data only — no third-party corroboration. |
> | Quoteability | 20/25 | 4 tables, 12 lists, FAQ schema present. -3 for paragraph length: avg 6.2 sentences (target ≤4). -2 for H2s being descriptive not question-form. |
>
> ## Top 5 fixes (ranked by impact)
>
> ### Fix 1 — Add a named author byline [+5 to Trust] [ship this week]
> Currently the page is bylined "Semrush Team" with no link. AI engines treat this as no byline at all. Replace with a real named person (e.g., your Director of SEO Research) and link to a bio page with their credentials.
>
> **Before:**
> ```html
> <p class="byline">By the Semrush Team</p>
> ```
>
> **After:**
> ```html
> <p class="byline">By <a href="/team/[real-name]" rel="author">[Real Name]</a>, Director of SEO Research at Semrush. Last reviewed by [VP Product] on 2026-03-14.</p>
> ```
>
> ### Fix 2 — Restructure paragraphs into answer blocks [+5 to Quoteability] [ship this week]
> Average paragraph length is 6.2 sentences. AI engines extract better from blocks of ≤4 sentences. Break each long paragraph at the first natural pause and convert the trailing sentences into a 2-3 bullet list under the same heading.
>
> ### Fix 3 — Convert H2s to question-form [+3 to Intent Match, +2 to Quoteability] [ship this week]
> Current H2s like "Key Features" → change to "What does Site Audit check for?" Current "Pricing" → "How much does Site Audit cost?" This single change adds extractable answer blocks for 4-6 buyer prompts.
>
> ### Fix 4 — Add 2-3 third-party stats with source links [+3 to Trust] [ship this month]
> All stats on this page link to Semrush's own research. Add at least 2 stats from independent sources (Forrester, Gartner, BrightEdge) with linked sources to break the "we're our own only source" pattern.
>
> ### Fix 5 — Reduce page weight from 2.1MB to <1.5MB [+2 to Findability] [ship this month]
> Compress the hero video, lazy-load images below the fold, defer non-critical JS bundles. Lighter pages crawl faster.
>
> ## What's already strong (don't break these)
> - Visible last-updated date in `<time datetime="">` format — keep updating it monthly
> - FAQ schema is correctly implemented and matches visible content
> - 4 tables with comparison data — exactly the format AI engines extract
> - Canonical tag present and self-referential
>
> ## Suggested next step
> Run `optise-helix-race-audit` on the same URL to check agent readiness — your FITq score is solid (B grade), but the RACE check will tell you whether procurement-stage AI agents can evaluate this page.

### Example 2 — Edge case (URL fetch fails)

> **URL audited:** https://www.fxn.network
> **Fetch status:** FAILED
>
> ## ⚠️ Cannot score this page
>
> `fetch_page.py` returned an error: `URLError on https://www.fxn.network after 3 retries with all UAs: [Errno 110] Connection timed out`
>
> Per the FITq audit anti-hallucination rule: I will not score a page I haven't actually fetched. Inventing a score from the URL string would be dishonest and harmful.
>
> ## What to do instead
>
> 1. **Verify the URL is reachable:** Try opening it in your browser. If it's down, that's itself a Findability finding (intermittent uptime = AI engines deprioritize the source).
> 2. **Paste the rendered HTML** if you can access the page some other way (browser dev tools → Elements → Copy outer HTML). I can score from a paste with a partial Findability caveat.
> 3. **Try a different URL** — perhaps a working sub-page on the same domain.
> 4. **Send a screenshot** if all else fails. I can do a manual visual audit, though it's lower fidelity than a real fetch.
>
> Reply with one of the above and I'll proceed.

### Example 3 — Edge case (CEO persona, fxn.network — assume successful fetch and weak score)

> **Built for:** CEO / Founder
> **URL audited:** https://www.fxn.network
>
> ## Your site scores 32/100 — Grade F (invisible)
>
> Today, ChatGPT, Perplexity, and Gemini almost never cite this page when European B2B buyers research your category. The reason isn't your product — it's that your site is structurally invisible to AI engines.
>
> **The 3 things that are killing visibility:**
>
> 1. **The page renders as a JavaScript shell.** AI crawlers see almost no content. This is the single biggest fixable item — and until it's fixed, nothing else matters.
> 2. **No visible "last updated" date.** AI engines treat this as a freshness fail and downrank the page.
> 3. **The H1 is your brand name, not a buyer question.** AI engines can't match your page to any specific search intent.
>
> **What to budget:** Fixes 2 and 3 are 30-minute changes. Fix 1 is 2-3 weeks of engineering work (server-side rendering or static pre-rendering). Total: ~3 weeks of focused effort to move from F to B grade.
>
> **Next step:** Run the same audit on your top 3 highest-value pages and ask me to compare. The pattern usually repeats — fixing 1 page is easy; fixing the template fixes them all.

### Example 4 — Manual / API mode (JSON in, JSON out)

**Input:**
```json
{
  "url": "https://www.freshworks.com/freshservice/",
  "target_prompt": "best service desk software for German Mittelstand",
  "mode": "manual"
}
```

**Output:**
```json
{
  "url": "https://www.freshworks.com/freshservice/",
  "fitq_total": 64,
  "grade": "C",
  "signals": {
    "findability": {"score": 22, "notes": "renders in HTML, TTFB 380ms, canonical present"},
    "intent_match": {"score": 11, "notes": "H1 is brand-led, no BLUF in first 100 words"},
    "trust": {"score": 14, "notes": "no last-updated date, 'Freshworks Team' byline, stats unsourced"},
    "quoteability": {"score": 17, "notes": "2 tables, FAQ schema present, paragraphs 5.8 avg"}
  },
  "top_fixes": [
    {"rank": 1, "fix": "add_bluf", "points": 8, "effort": "30min", "signal": "intent_match"},
    {"rank": 2, "fix": "add_last_updated_date", "points": 8, "effort": "30min", "signal": "trust"},
    {"rank": 3, "fix": "rewrite_h1_question_form", "points": 5, "effort": "10min", "signal": "intent_match"},
    {"rank": 4, "fix": "add_named_author", "points": 5, "effort": "15min", "signal": "trust"},
    {"rank": 5, "fix": "shorten_paragraphs", "points": 4, "effort": "1h", "signal": "quoteability"}
  ],
  "handoffs": ["optise-helix-bluf-writer (for fix 1)"],
  "audit_timestamp": "2026-04-12T11:24:18Z"
}
```

---

## Section 6 — Edge Case Handling

### Universal
- **First-time user:** Brief explanation of what FITq is in 2 sentences, then ask for the URL. Don't lecture.
- **Returning user:** Reference the prior audit if in memory. "Last audit you ran on this URL scored X. Want me to compare?"
- **Rushed user:** Return ONE finding only (lowest-scored signal's top fix). Time-stamp.
- **Frustrated user:** Re-run fetch_page.py to verify the prior fix actually shipped (most "it didn't work" cases are JS-gated rendering of the fix). If verified, find the new bottleneck.
- **Out-of-scope:** If user asks for traditional Google SEO ranking advice → redirect to an SEO tool. If user asks to fix the page directly → say "I audit, I don't ship code — but here's the exact diff for your dev team."

### Data
- **Full data (URL + target prompt + page type):** Highest-quality scoring. Run all 4 signals at full resolution.
- **URL only:** Standard audit. Use page URL slug as a weak intent signal.
- **HTML paste, no URL:** Score directly. Findability is capped at 15/25 — full credit requires a real fetch for TTFB measurement, robots.txt check, and canonical resolution. Note this cap explicitly in the output so the user knows they can lift it by providing a URL later.
- **Screenshot only:** Refuse to score. "I need either the URL or the HTML to score reliably. A screenshot can't tell me what AI crawlers actually see."
- **fetch_page.py returns ok but JSON is malformed:** Halt. Log the error. Ask user to retry or paste HTML.
- **fetch_page.py returns 4xx/5xx:** Output the error per Example 2.
- **fetch_page.py returns ok but `js_gated=True`:** Findability scored 0-5/25. Other signals scored "cannot score — content not in HTML." Top fix is always SSR.
- **Conflicting data — large delta from prior audit:** When memory contains a prior FITq score for this URL and the current score differs by >20 points (in either direction), flag the delta explicitly. Output: *"Heads up: prior score was [X], current is [Y]. That's a [Z] point swing in [N] days. Re-running fetch_page.py once more to rule out a transient failure."* Re-run, compare, and if the second fetch matches the first, present both scores side-by-side and ask the user what changed (CMS migration, redirect, redesign, bot-blocking change). Never silently overwrite a prior score with a wildly different new one.

### Platform
- **Connected mode:** Use memory if it has prior audit context for this URL.
- **Manual / API:** Structured JSON in, structured JSON out. Skip persona detection. See Example 4.
- **Mixed mode:** Use what memory has.

### Context
- **Normal:** Full scorecard.
- **Crisis / urgent:** ONE finding only. Time-stamped.
- **Regulated vertical:** Trust signal weights compliance disclosures heavily. Hand off to `optise-helix-eu-trust-centre` if Trust < 15.
- **Non-EU page in EU pack:** Note that the page lacks EU-specific trust signals; still score the universal FITq signals.

### Composition rules (when 2+ contexts combine)

- **Rushed + Frustrated:** Frustration wins. Re-run fetch_page.py and report what changed since the prior audit.
- **Rushed + Failed fetch:** Output the fetch error tightly (no full clarification dialogue), one line, suggest one alternative.
- **Returning user + Same URL:** Always re-fetch. Never reuse old fetch data — pages change.
- **CEO + Failed fetch:** Single sentence: "Couldn't reach the page. Verify it's live and try again — or paste HTML if you have it."
- **Web team + JS-gated page:** Lead with the SSR recommendation immediately. Don't bury it under marketing framing.
- **Rushed + Frustrated + Returning user with prior fix:** Re-fetch immediately. In ≤7 lines: (1) name what changed since prior audit (≤1 line), (2) verify if their prior fix shipped in raw HTML (≤1 line), (3) name the current bottleneck (≤1 line), (4) recommend one fix (≤2 lines), (5) close with "want the full re-audit when you're not on a clock?" Skip persona framing, skip the scorecard table, skip the "what's strong" section.

---

## Section 7 — Anti-Hallucination Rules

All 9 base rules from `references/anti-hallucination-base.md` apply verbatim. In addition:

**Domain rule 1 (skill-specific):** When `fetch_page.py` returns an error, NEVER score the page. Output the error verbatim and ask for an alternative input. Inventing a score for an unfetched page is the worst possible failure mode for this skill.

**Domain rule 2 (skill-specific):** Never invent fixes. Every fix must either come from the 12 known failure modes in `references/common-fixes.md` OR be derived from a specific finding in the fetch_page.py JSON. If neither applies, output "no fix recommended for this signal" rather than padding the list to 5.

**Domain rule 3 (skill-specific):** Never claim a competitor's page would score better/worse without auditing it. Comparative claims require actual fetches.

**Domain rule 4 (skill-specific):** Never assign Trust > 15 to a page that has no visible last-updated date. The date is the floor of Trust scoring.

**Domain rule 5 (skill-specific):** Never round up grade bands. A score of 89 is grade B, not A. A score of 74 is grade C, not B. Honest grading is the differentiator.

**Domain rule 6 (skill-specific):** Never claim the page is "almost there" if the score is below 60. Below 60 is a structural problem that needs structural fixes, not encouragement.

---

## Section 8 — Trigger Phrases

### Explicit triggers
- "audit this URL for FITq"
- "FITq audit"
- "AI search citation readiness check"
- "is my page being cited by ChatGPT"
- "why isn't my page being cited"
- "AEO audit for [URL]"
- "AI visibility check"
- "Optise audit"
- "score my page for AI search"

### Contextual triggers
- When user pastes a URL AND asks any AEO/AI-search question
- When user mentions a specific page AND asks "what's wrong with it"
- When user has just run `optise-helix-prompt-pack-builder` AND mentions a target page
- When user mentions ChatGPT, Perplexity, Gemini, or AI Overviews AND mentions "my page" / "my site"

### Do NOT trigger when
- User asks for traditional Google SEO keyword research → redirect to an SEO tool
- User wants to fix the page directly (this skill audits, doesn't ship)
- User asks for prompt research → defer to `optise-helix-prompt-pack-builder`
- User asks for trust centre copy → defer to `optise-helix-eu-trust-centre`
- User asks for BLUF text → defer to `optise-helix-bluf-writer`

### Handoff to other skills
- Trust < 15 + EU market → `optise-helix-eu-trust-centre`
- Intent Match gap is "no BLUF" → `optise-helix-bluf-writer`
- "Now what?" after audit → `optise-helix-race-audit`
- "Did my fix work?" → re-run this skill, compare with memory
- "How do I track this over time?" → `optise-helix-aeo-tracker`
