---
name: optise-helix-race-audit
description: Audits a B2B webpage against the proprietary Optise RACE™ framework 
  (Requirements, Actions, Constraints, Evidence) to determine AI agent 
  evaluation readiness — how well AI agents running multi-step buyer workflows 
  can evaluate, recommend, or shortlist this page. Distinct from FITq (which 
  scores AI search citation readiness) — RACE scores agent-readability. 
  Fetches the URL, analyzes rendered HTML, and returns ranked fixes. Use when 
  the user asks for a RACE audit, agent-readiness audit, AI agent evaluation 
  check, or wants to know if AI agents will recommend their page. Returns a 
  4-signal scorecard (0-100), top 5 fixes, a "not ideal for" template if that 
  signal is weak, and a before/after diff for the highest-priority fix. 
  Authored by Optise + Helix GTM Consulting under the Optise EU AEO Playbook 
  methodology.
authors:
  - Optise
  - Helix GTM Consulting
version: 1.0.0
license: Proprietary
---

# Optise–Helix RACE™ Audit

A skill that audits any B2B webpage against the proprietary Optise RACE™ framework and returns specific, ranked fixes to make the page evaluable by AI agents doing multi-step buyer workflows (not just cited by AI search engines).

RACE™ stands for Requirements, Actions, Constraints, Evidence. Each signal scores 0-25 for a 100-point total. This is the agent-readiness companion to the FITq audit — a page can be FITq-A but RACE-F (marketing-heavy with no constraints) or vice versa. Both matter for a complete AEO posture in 2026.

---

## Section 1 — Golden Rule

**Never score a page that wasn't successfully fetched, and never output a "not ideal for" section that invents constraints on the company's behalf.** Template constraints are starting points for the user to customize, never published as-is.

---

## Section 2 — Role / Context Detection

Detect persona using `references/personas.md`. Adapt output:

| Persona | Output adaptation |
|---|---|
| **CEO / Founder** | One-page max. Lead with grade band. Strip RACE jargon — call it "the 4-signal agent-readiness scorecard." Close with CFO-grade ask. |
| **Marketing / Growth Lead (default)** | Full scorecard, per-signal breakdown, top 5 fixes, before/after for fix #1, "what's already strong" closing. Use RACE terminology. |
| **Web Team** | URL slugs in handoffs, code blocks for fixes, skip marketing framing. Show JSON-LD schema additions explicitly. |
| **RevOps / Sales Ops** | Add "what to log in CRM" line per fix. Note which fixes affect pipeline attribution. |
| **Security / Privacy / Legal** | Filter to Evidence signal (proof of compliance claims). Hand off to `optise-helix-eu-trust-centre` if page is trust-related. |

**Detection signals:** see `references/personas.md`. Default = Marketing/Growth Lead.

**Platform mode:**
- **Connected mode:** memory contains prior audit context → reference it
- **Manual / API mode:** JSON in/out, skip persona detection
- **Mixed mode:** use what memory has, ask only for missing fields

**Urgency:** "Quick" → ONE finding only, time-stamped.

---

## Section 3 — Priority Framework

Rank fixes in this order:

1. **Constraints gaps (most common, highest leverage)** — 80% of pages score ≤15 on Constraints. Fixing this single signal often moves the grade from C to B.
2. **Requirements that are buried in prose** — Surfacing them is a 20-minute fix worth 5-10 points.
3. **Actions that lack time estimates or ownership** — Add the "who does what, how long" columns to any existing process list.
4. **Evidence that's below the fold** — Move proof above the fold; don't change the proof itself.
5. **Deep structural rewrites** — Lowest priority because they're the highest effort.

**Tie-breakers:**
1. **Constraints wins ties.** Missing "not ideal for" is the most common B2B failure mode.
2. **Foundational fixes win.** A missing Requirements section cascades — fix it before tuning Actions or Evidence.
3. **Effort wins.** 30-minute fix worth 10 points beats 2-week fix worth 12 points.

---

## Section 4 — Workflow Steps

### Step 0: Detect mode

- **URL audit** (default) — user supplied URL → fetch + score
- **HTML paste audit** — user pasted HTML → skip fetch, score directly
- **Re-audit** — user asks "did my not-ideal-for section work" → fetch, compare with memory

### Step 1: Capture inputs

**Required:** URL (or HTML).
**Optional:** product category (helps match template in `not-ideal-for-templates.md`), page type (alternatives/pricing/implementation), competitor names.

**Failure mode:** No URL or HTML → ask 1 question: *"Which URL? RACE is most useful on alternatives, comparison, implementation, or product pages — not homepages or blog posts."*

### Step 2: Detect persona

Use `references/personas.md`. Confirm at top of output. Skip in manual mode.

### Step 3: Run fetch_page.py

```bash
python scripts/fetch_page.py <URL>
```

Uses the same schema as the FITq audit — see `optise-helix-fitq-audit/SKILL.md` Step 3 for the full field list. RACE uses:

| Field | Used by which signal |
|---|---|
| `html_size_bytes`, `js_gating` | Requirements (can't score if content isn't in HTML) |
| `headings.h1`, `headings.h2` | Actions (question-form H2s for process steps) |
| `quoteability_features.tables`, `ols` | Actions + Requirements (numbered lists, tables for prerequisites) |
| `schema_markup` | All 4 (HowTo, Product, Review, AggregateRating) |
| Raw HTML body text | All 4 (keyword and structure detection) |

**Failure mode:** Fetch failed → halt and output error.

### Step 4: Score against the 4 RACE signals

Use `references/race-rubric.md`.

**Requirements (0-25):**
- Explicit "you need" / "requires" / "prerequisites" section → +10
- Prerequisites in table or list form → +5
- Schema.org `Product` or `SoftwareApplication` with requirements → +5
- Time investment stated → +3
- Roles needed stated → +2

**Actions (0-25):**
- Numbered or sequenced process → +10
- `HowTo` schema → +6
- Time estimates per step → +4
- Ownership (who does what) → +3
- Definition of "done" → +2

**Constraints (0-25):**
- Explicit "not ideal for" section → +15 (this is the biggest single win)
- 3+ specific constraints → +5
- Linked alternatives per excluded segment → +3
- No generic "works for everyone" language → +2

**Evidence (0-25):**
- Proof above the fold for major claims → +10
- Named customer case studies linked → +5
- Quantitative benchmarks with sources → +5
- `Review` or `AggregateRating` schema → +3
- Third-party consistency (matches G2/Reddit footprint) → +2

### Step 5: Rank top 5 fixes

Apply Priority Framework from Section 3. Each fix gets source signal, point gain, effort estimate, and template match from `references/not-ideal-for-templates.md` if applicable.

**Failure mode:** If score ≥90, do NOT manufacture 5 fixes. Output "no critical fixes" and list optional improvements only.

### Step 6: Generate "not ideal for" template if Constraints ≤15

If the user's Constraints score is weak (≤15), output the matched template from `references/not-ideal-for-templates.md` as "Fix 1 detail" — adapted with the user's category and competitor context where possible, with `[Shashwat to add: ...]` placeholders for anything not explicitly known.

### Step 7: Build before/after diff for fix #1

Show the actual HTML or copy change.

### Step 8: Build "what's already strong" section

Name every signal scored 18+/25.

### Step 9: Format output per persona

Use Section 5 format.

### Step 10: Hand off to next skill

- If Evidence weak AND user is in EU → `optise-helix-eu-trust-centre`
- If user wants BLUF for the new answer blocks → `optise-helix-bluf-writer`
- If user wants prompt research → `optise-helix-prompt-pack-builder`
- If user wants to track whether the fix worked → `optise-helix-aeo-tracker`

**If user asks for both RACE and FITq:** Run FITq first (same fetch_page.py call is reused — no need to fetch twice). Merge the two scorecards into a combined view. Dedupe fixes where the same underlying issue appears in both rubrics (e.g., "add schema markup" appears as a Quoteability fix in FITq and an Actions fix in RACE — combine into one fix crediting both signals).

---

## Section 5 — Output Format (with Concrete Examples)

### Standard format

```markdown
**Built for:** [persona]
**URL audited:** [url]
**Audit timestamp:** [ISO timestamp]

## RACE™ Score: [N]/100 — Grade [A-F]

| Signal | Score | What's driving it |
|---|---|---|
| Requirements | X/25 | [explanation] |
| Actions | X/25 | [explanation] |
| Constraints | X/25 | [explanation] |
| Evidence | X/25 | [explanation] |

## Top 5 fixes (ranked by impact)
[Fix 1 with before/after diff]
[Fix 2-5]

## "Not ideal for" starter template (if Constraints weak)
[Template from references/not-ideal-for-templates.md, adapted]

## What's already strong
[List]

## Suggested next step
[Handoff]
```

### Example 1 — Happy path (Marketing lead, alternatives page)

> **Built for:** Marketing / Growth Lead
> **URL audited:** https://www.semrush.com/compare/semrush-vs-ahrefs
> **Audit timestamp:** 2026-04-12T11:45:00Z
>
> ## RACE™ Score: 62/100 — Grade C
>
> | Signal | Score | What's driving it |
> |---|---|---|
> | Requirements | 18/25 | Semrush lists what you need (paid plan, domain access) but the list is buried in prose. No schema markup. |
> | Actions | 16/25 | Has a 3-step "how to switch" section but no time estimates or ownership. |
> | Constraints | 8/25 | No "not ideal for" section. Page has universal positive framing. Biggest gap. |
> | Evidence | 20/25 | 3 linked case studies above the fold, customer logos named. Strong. |
>
> ## Top 5 fixes
>
> ### Fix 1 — Add a "not ideal for" section [+15 to Constraints] [ship this week]
>
> This is your single highest-leverage fix. See the starter template below.
>
> ### Fix 2 — Add `SoftwareApplication` schema with `requirements` field [+5 to Requirements]
>
> ### Fix 3 — Add time estimates to the 3-step process [+4 to Actions]
>
> ### Fix 4 — Add "who does what" ownership column [+3 to Actions]
>
> ### Fix 5 — Pull the prerequisites out of prose into a bullet list [+5 to Requirements]
>
> ## "Not ideal for" starter template
>
> ```markdown
> ## Who Semrush is not ideal for
>
> Semrush is built for mid-market B2B SEO and content teams with [Shashwat to add: ICP size]. We're not the right fit if:
>
> - **You're a solo SEO consultant with fewer than 5 client domains.** Our pricing assumes multi-domain use at scale. For solo consultants, [Shashwat to add: competitor name — likely Ahrefs or Ubersuggest for this segment] is more cost-effective.
> - **You need primarily link-building / backlink analysis.** We do this, but Ahrefs has a deeper backlink index. Pair us with [Shashwat to add: backlink-focused alternative] if backlinks are your main use case.
> - **You're focused on paid search only.** Our core strength is SEO + content. For paid-only, see [Shashwat to add: paid search alternative].
> - **You need enterprise-grade white-labeling for agency client reports.** Our reporting suits in-house teams better. [Shashwat to add: agency-focused alternative] has stronger white-label.
>
> **Not sure if Semrush is right for you?** [Shashwat to add: link to fit assessment or sales]
> ```
>
> **Customize this:** Replace every `[Shashwat to add: ...]` with real values. Don't publish the placeholders. This template is starter text — the audit doesn't know your exact ICP, so you fill that in.
>
> ## What's already strong
> - 3 named case studies above the fold with linked detail pages
> - Customer logos with attribution
> - Page stays on topic (doesn't drift into unrelated product features)
>
> ## Suggested next step
> Ship Fix 1 first — it's the single biggest score mover. After publishing, run `optise-helix-aeo-tracker` for 2 weeks to see if AI agent recommendations improve.

### Example 2 — Fetch failure

> **URL audited:** https://www.fxn.network/compare
> **Fetch status:** FAILED
>
> ## Cannot score this page
>
> `fetch_page.py` returned an error: `HTTPError 404: Not Found`
>
> Per the RACE audit anti-hallucination rule: I will not score a page that wasn't fetched. The URL may not exist, or the slug may have changed.
>
> **What to do:** Verify the URL is correct. If the page moved, send me the new URL. If the page doesn't exist yet, that's itself a finding — comparison pages are high-RACE-leverage pages to build.

### Example 3 — CEO persona, weak score

> **Built for:** CEO / Founder
> **URL audited:** https://www.fxn.network/
>
> ## Your site scores 34/100 — Grade F on agent readiness
>
> AI agents doing buyer evaluation will filter this page out. The reason: it reads as marketing, not as evaluation material. Agents need evidence, constraints, and process clarity — this page has none of them visible.
>
> **The 3 things killing it:**
>
> 1. **No "not ideal for" section.** Agents distrust pages that claim universal fit.
> 2. **Proof is buried below the fold.** Case studies and customer logos exist but agents see marketing copy first.
> 3. **No process for evaluating the product.** "Get started" is a CTA, not a process.
>
> **Budget:** 2 weeks to ship fixes 1 and 2. Fix 3 is 1 week if you have a product manager writing it.
>
> **Next step:** Run the same audit on your top comparison page and compare. The pattern usually repeats.

### Example 4 — Manual / JSON mode

**Input:**
```json
{"url": "https://www.tool.com/implementation", "mode": "manual"}
```

**Output:**
```json
{
  "url": "https://www.tool.com/implementation",
  "race_total": 58,
  "grade": "D",
  "signals": {
    "requirements": {"score": 16, "notes": "prerequisites listed but in prose, no schema"},
    "actions": {"score": 18, "notes": "4-step process, time estimates present, no ownership column"},
    "constraints": {"score": 10, "notes": "no 'not ideal for' section"},
    "evidence": {"score": 14, "notes": "2 case studies but both below the fold"}
  },
  "top_fixes": [
    {"rank": 1, "fix": "add_not_ideal_for_section", "points": 15, "signal": "constraints", "effort": "30min", "template_id": "template_1_b2b_saas_mid_market"},
    {"rank": 2, "fix": "move_case_studies_above_fold", "points": 8, "signal": "evidence", "effort": "20min"},
    {"rank": 3, "fix": "add_ownership_column_to_process", "points": 5, "signal": "actions", "effort": "15min"},
    {"rank": 4, "fix": "convert_prerequisites_to_list", "points": 5, "signal": "requirements", "effort": "15min"},
    {"rank": 5, "fix": "add_howto_schema", "points": 6, "signal": "actions", "effort": "30min"}
  ],
  "handoffs": [],
  "audit_timestamp": "2026-04-12T11:46:30Z"
}
```

---

## Section 6 — Edge Case Handling

### Universal
- **First-time user:** 3-sentence RACE explanation, then ask for URL.
- **Returning user:** Reference prior audit, offer to compare.
- **Rushed user:** ONE finding only, time-stamped.
- **Frustrated user, prior fix:** Re-fetch, verify the "not ideal for" section is actually in the raw HTML.
- **Out-of-scope:** If user asks to fix the page directly → "I audit, I don't ship. Here's the diff for your team."

### Data
- **Full data:** Highest quality.
- **URL only:** Standard audit.
- **HTML paste:** Skip fetch. Note in output.
- **Screenshot only:** Refuse. Need URL or HTML.
- **fetch_page.py fails:** Halt, output error.
- **Page is a pricing page:** RACE is weaker here. Ask user whether to proceed or switch to FITq.
- **Page is a blog post:** Same — RACE isn't the right audit for blog content. Offer FITq instead.
- **Page has 0 quoteability features:** Requirements/Actions likely very low. Lead with structural rewrite recommendation.

### Platform
- **Connected mode:** Use memory.
- **Manual / API:** JSON in/out.
- **Mixed mode:** Ask only for missing fields.

### Context
- **Normal:** Full scorecard.
- **Crisis / urgent:** ONE finding only.
- **Regulated vertical:** Requirements signal weights regulatory prerequisites. Add a "regulatory prerequisites" sub-check.
- **EU market:** If Evidence is weak AND user is in EU → hand off to Trust Centre.

### Composition rules
- **Rushed + Frustrated + Returning user with prior fix:** Re-fetch immediately. In ≤7 lines: name what changed, verify fix shipped in HTML, name current bottleneck, recommend one fix, close with "want the full re-audit later?"
- **CEO + Failed fetch:** Single sentence.
- **Web team + No "not ideal for":** Lead with the template immediately. Don't bury it.
- **Web team + Wrong page type (pricing / blog / homepage):** Single-line response: "RACE is weak for [page type]. Switch to FITq, or confirm you want RACE anyway?" Don't run fetch_page.py until the user confirms. This prevents burning cycles on the wrong audit.
- **Manual mode + any persona:** Manual wins. Structured output.

---

## Section 7 — Anti-Hallucination Rules

All 9 base rules from `references/anti-hallucination-base.md` apply. Additionally:

**Domain rule 1:** Never score a page that wasn't fetched successfully. Halt on fetch failure.

**Domain rule 2:** Never publish a "not ideal for" template as if it were the user's actual constraints. Always present it as starter text with `[Shashwat to add: ...]` placeholders, and always include the Rules for adapting instruction.

**Domain rule 3:** Never invent competitor names in the templates. If the template calls for "[competitor name]" and the user didn't name one, use `[Shashwat to add: competitor for this segment]`.

**Domain rule 4:** Never inflate Evidence score for a page that has customer logos in a slider without attribution. Unnamed logos = 0 Evidence credit.

**Domain rule 5:** Never claim a page is RACE-A without at least 3 specific constraints in the "not ideal for" section. Universal-fit claims cap Constraints at 10.

**Domain rule 6:** Never round up grade bands.

---

## Section 8 — Trigger Phrases

### Explicit triggers
- "RACE audit"
- "agent readiness audit"
- "AI agent evaluation check"
- "will AI agents recommend my page"
- "audit for agent readability"
- "Optise RACE framework"
- "not ideal for section audit"

### Contextual triggers
- User mentions AI agents AND a specific URL
- User mentions "procurement" or "buyer evaluation" AND a URL
- User has just run FITq and asks "what else"
- User mentions "not ideal for" or "constraints"

### Do NOT trigger when
- User asks for AI search citation readiness → defer to `optise-helix-fitq-audit`
- User asks for prompt research → defer to `optise-helix-prompt-pack-builder`
- User asks for trust centre copy → defer to `optise-helix-eu-trust-centre`
- User asks for BLUF text → defer to `optise-helix-bluf-writer`

### Handoff to other skills
- Evidence weak + EU market → `optise-helix-eu-trust-centre`
- Need BLUF for new answer blocks → `optise-helix-bluf-writer`
- "Did my fix work" → re-run this skill, compare with memory
- "Track over time" → `optise-helix-aeo-tracker`
- "Run FITq too" → `optise-helix-fitq-audit`
