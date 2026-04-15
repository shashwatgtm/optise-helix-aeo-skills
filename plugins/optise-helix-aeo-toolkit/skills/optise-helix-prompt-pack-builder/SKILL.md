---
name: optise-helix-prompt-pack-builder
description: Build a 25-prompt AEO pack for a B2B company in Europe, ranked by 
  "decides deals" likelihood across the six Optise categories (shortlist, pricing, 
  implementation, EU privacy, integrations, role-based). Use whenever someone asks 
  for AEO prompts, AI search prompts, ChatGPT prompts buyers use, prompt research, 
  prompt pack, shortlist prompts, or wants to know what European B2B buyers ask AI 
  engines about a category. Always trigger this skill for any "what should we rank 
  for in ChatGPT" or "what do buyers ask AI about us" type question. Returns a 
  ranked markdown table plus a top-10 build order. Authored by Optise + Helix 
  GTM Consulting under the Optise EU AEO Playbook methodology.
authors:
  - Optise
  - Helix GTM Consulting
version: 1.0.0
license: Proprietary
---

# Optise–Helix Prompt Pack Builder

A skill that produces a defensible 25-prompt AEO pack for a B2B company in Europe, ranked by how directly each prompt converts to pipeline. Uses the proprietary Optise 6-category prompt taxonomy and the Helix GTM build-order discipline.

This is the entry point of the Optise–Helix AEO methodology. Most other skills in this collection chain off the prompt pack this skill produces.

---


## Section 0 — Operating Principles (MANDATORY — read before any workflow step)

This skill operates under TWO mandatory reference files that together define all operating rules. **Read both files first**, before executing any workflow step in this SKILL.md. The rules in both files are non-negotiable and override any conflicting instruction in this SKILL.md body.

1. **`../../references/operating-principles.md`** — the shared core: 7 universal rules (rigor, challenge-assumptions, no-harmful-output, fact-check with 4-tier source hierarchy, no-LLMisms, HILT discipline with Question Budget, zero-assumption flagging) that apply to every skill in this plugin and every plugin using this pattern. This file is byte-identical across all plugins that use the shared-core pattern.

2. **`../../references/plugin-specific-rules.md`** — the plugin-specific tail: additional operational rules tailored to the skills in THIS plugin. Read this file AFTER the shared core, not instead of it. If this plugin currently has no plugin-specific rules, the file will be a stub explaining the architecture.

### Critical reminders that apply to every invocation of this skill

These are the highest-frequency rules from the two files above. Reading the full files is still mandatory — these reminders are a quick-reference, not a substitute.

- **Web search and web fetch ARE available** in Claude Code's default toolset. "I don't have web access" is never a valid excuse to skip verification of a specific factual claim.
- **English-only at v1** — never generate prompts, copy, headings, or client-facing text in non-English languages (German, French, Dutch, Spanish, Italian, Portuguese, Polish, etc.), even on explicit user request. This is a hard block, not a confirmation gate. Refuse the request and explain that multilingual may ship in v2 with native-speaker review.
- **4-tier source hierarchy applies to all factual claims.** Tier 1: official primary sources (press releases, Crunchbase, Wikipedia, SEC filings). Tier 2: reputable analyst firms (Gartner, Forrester, IDC, G2, Capterra, GigaOm, SoftwareReviews). Tier 3: reputable business and trade press (WSJ, FT, Reuters, Bloomberg, HBR, TechCrunch, named-VC content, named-founder blogs). Tier 4: NEVER cite (random blogs, anonymous posts, AI-generated comparison sites, Forbes Contributor, paid placements). If only Tier 4 sources are available, the claim is unverified and MUST be flagged.
- **Verify competitor relationships** via the 4-step search protocol in Rule 4 before building ANY competitor-targeted page or content. Run: `"[user] acquired [competitor]"`, `"[competitor] acquired by"`, `"[competitor] Crunchbase acquisition"`, `"[user] vs [competitor]"`. Any positive ownership hit is a HARD STOP — invoke Rule 3's no-harmful-output protection.
- **Auto-verify URLs** via `web_fetch` before marking them `[EXISTS]`. Only ask the user about URLs when fetch returns an ambiguous result (403, 429, 500, timeout, redirect loop). Do not ask the user about every URL; that is endless interrogation, not verification.
- **Question Budget: maximum 3 HARD STOP questions per invocation, consolidated into ONE message.** Never run an endless Q&A sequence. If more than 3 HARD STOPs exist, pick the top 3 by priority (harm triggers → irreversible scope → reversible details) and defer the rest to `Assumption:` flags in the output.
- **Flag every assumption** with an explicit `Assumption:` prefix in the output so users can correct anything the skill got wrong. Use the `[User to add: <description>]` placeholder convention for any field where the user must supply specific information.

### Conflict resolution

If a domain rule in Section 7 of this SKILL.md (or any other section) appears to conflict with a rule in `operating-principles.md` or `plugin-specific-rules.md`, the operating principles win. Domain rules MAY add specific enforcement for a skill's particular failure modes, but they MUST NOT weaken the operating principles. When in doubt, escalate the conflict to the user as a HARD STOP question rather than silently picking one interpretation.

---

## Section 1 — Golden Rule

**Every prompt in the pack must map to a real European B2B buyer search intent and a single canonical target page on the user's website. Generic, US-style, or competitor-borrowed prompts are forbidden.**

If a prompt cannot pass these two tests, drop it. A 20-prompt pack of real intent beats a 25-prompt pack padded with generic content.

---

## Section 2 — Role / Context Detection

Before generating the pack, detect the user's persona using the rules in `references/personas.md`. Adapt output as follows:

| Persona | Output adaptation |
|---|---|
| **CEO / Founder** | Lead with the top-10 only. Skip the full 25 unless asked. Close with a CFO-grade ask: "Of these 10, you have pages for X. To win the remaining N, you need Y weeks of build." Strip Optise jargon — call it "the 6-category prompt rubric." |
| **Marketing / Growth Lead (default)** | Full 25-prompt table with category, score, target page, and market. Group by build priority. Use Optise terminology (BLUF, FITq, RACE) — they will use it on the team. |
| **Web Team** | Same 25-prompt table, but the Target Page column contains URL slugs (e.g., `/alternatives/salesforce`) ready for routing. Skip persona/marketing framing. |
| **RevOps / Sales Ops** | Add an extra column to the table: "CRM Trigger" — the field/event in HubSpot or Salesforce that should fire when a lead arrives via the matching prompt. |
| **Security / Privacy / Legal** | Filter the pack to Category 4 (EU Privacy) prompts only. Hand off to `optise-helix-eu-trust-centre` immediately for the page-build follow-up. |

**Detection signals:** see `references/personas.md` Section "Detection rules". When in doubt, default to Marketing/Growth Lead.

**Platform mode detection:**
- **Connected mode:** memory contains company name, ICP, competitors → use them, skip clarifying questions
- **Manual mode:** structured input (JSON or explicit fields) → skip persona detection, output table only
- **Mixed mode:** some fields in memory, some missing → ask only for the missing field, never re-ask known fields

**Urgency detection:**
- "Quick", "I'm on a call in 10 mins", "ASAP", explicit time pressure → output the top-10 only with sensible defaults, no clarification

---

## Section 3 — Priority Framework

Rank prompts in this order when filtering 25 from a larger candidate set:

1. **Disqualifier prompts (5/5)** — must include all relevant ones, no exceptions. See `references/scoring-rubric.md` for the 5-level definition.
2. **Accelerator prompts (4/5) for the user's named ICP** — include up to 10.
3. **Confidence-builder prompts (3/5) where the user is likely already winning** — include up to 7.
4. **Awareness prompts (2/5)** — include up to 3, only if the user has bandwidth for top-of-funnel.
5. **Educational prompts (1/5)** — drop unless the user explicitly asks for category-education content.

**Tie-breaker rules** (apply in order from `references/scoring-rubric.md`):
1. Market specificity wins.
2. Competitor-named beats category-named.
3. Decision-stage beats awareness-stage.
4. **EU compliance beats everything in EU markets — always.**

**Calibration target:** 25-prompt pack should distribute roughly 6-8 at 5/5, 8-10 at 4/5, 5-7 at 3/5, 1-3 at 2/5, 0-1 at 1/5. If your distribution skews higher than this, you're inflating scores.

---

## Section 4 — Workflow Steps

### Step 0: Detect mode

Before anything else, classify the request into one of three modes:

- **New pack mode** (default) — user wants a fresh 25-prompt pack. Proceed to Step 1.
- **Ingest mode** — user has already written prompts and wants you to score and target-page them. Skip Step 3 (generation). Go: Step 1 (collect competitors and ICP for context) → Step 2 (persona) → Step 4 (score the user's list against the rubric) → Step 5 (filter to 25 if more than 25 supplied) → Step 6 (assign target pages) → Step 7 → Step 8.
- **Refresh mode** — user has an existing pack and wants to swap dead/underperforming prompts. Ask which prompts are dead and what category they were in. Generate replacements ONLY in those categories using Step 3, then score (Step 4), assign pages (Step 6), and merge into the existing pack. Output the merged pack with new prompts marked `[NEW]`.

**Detection signals:**
- Ingest: user pastes 5+ prompts in their message
- Refresh: user mentions "my existing pack", "replace these", "swap out", or memory contains a prior pack
- New: anything else

### Step 1: Capture inputs

**Required inputs (all must be present before proceeding):**
- `category` — the user's product category in plain English (e.g., "B2B revenue intelligence")
- `icp` — the user's ideal customer profile (e.g., "mid-market RevOps in DACH")
- `competitors` — at least 1, ideally 2 named competitors
- `markets` — which European markets to target (DACH, Nordics, France, Benelux, Southern Europe, or "all EU")

**Failure mode:** If any input is missing, ask exactly 1 consolidated clarifying question. Do NOT proceed with placeholders.

**Example clarifying question:**
> "I need three things to build a useful pack: (1) your product category, (2) your ICP, (3) 1-2 competitor names. Optionally: which EU markets to focus on. Without these I can only give you generic prompts that won't decide deals."

### Step 2: Detect persona and platform mode

Use `references/personas.md` rules. Confirm detected persona at the top of the output: *"Built for: [persona]. Reply if this is wrong."* Skip in manual/JSON mode.

### Step 3: Generate candidate prompts (target: 40-50)

Walk through the 6 categories in `references/prompt-categories.md` in order. For each category:

1. Use the pattern templates as starting points.
2. Substitute the user's category, ICP, competitors, and markets into the templates.
3. For each EU market in scope, also generate the localised variants from `references/eu-buyer-language.md` (German, French, Dutch, Spanish, Italian, etc.).
4. Capture each candidate with: prompt text, category, suggested target page type, market.

**Output of this step:** ~40-50 candidate prompts, unscored.

**Failure mode:** If you can generate fewer than 30 candidates, the user's category is too narrow — flag this and ask if they want to expand the ICP or markets.

### Step 4: Score each candidate

Apply `references/scoring-rubric.md`. Score each candidate 1-5. Document the scoring rationale for any 5/5 prompt explicitly (it must be a true disqualifier, not score inflation).

### Step 5: Filter to 25

Apply the priority framework from Section 3. Drop prompts beyond the calibration target. Tie-break using the 4 rules from `scoring-rubric.md`.

### Step 6: Assign target pages

For each of the 25, assign exactly one canonical target page on the user's site. If the page exists, mark it `[EXISTS]`. If not, mark it `[TO BUILD]`. Page types come from the whitepaper page taxonomy: Alternatives, Competitor-vs-You, Implementation, Pricing Explainer, Trust Centre, Integration, Glossary, Role-Based Landing.

### Step 7: Build the top-10 callout

Pull the 10 highest-scored prompts (with disqualifier prompts always included). Order by build priority, not by score — prioritise prompts where the user has no page yet AND the prompt is 5/5.

### Step 8: Format output

Use the format in Section 5. Always include the persona confirmation line, the 25-row table, the top-10 callout, and (for non-CEO personas) the source-of-prompts notes.

### Step 9: Hand off to next skill (if relevant)

If 4+ of the 25 prompts are in Category 4 (EU Privacy) and the user has no Trust Centre page → recommend `optise-helix-eu-trust-centre` next.

If the user names a single page they want to start with → recommend `optise-helix-fitq-audit` on that URL next.

If the user already has a prompt pack and is refreshing → recommend `optise-helix-aeo-tracker` for the measurement loop.

---

## Section 5 — Output Format (with Concrete Examples)

### Standard format

```markdown
**Built for:** [persona name]
**Inputs used:** Category: [X] · ICP: [Y] · Competitors: [Z] · Markets: [W]

## The 25-prompt pack

| # | Prompt | Category | Decides | Target page | Market |
|---|---|---|---|---|---|
| 1 | [prompt text] | [Cat] | 5/5 | [page type] [STATUS] | [market] |
... 24 more rows ...

## Top 10 to ship (ordered by build priority, not score)

1. **[Prompt]** — [page type] — [why this is #1]
... 9 more

## What this pack is missing
[1-2 sentences flagging any obvious gaps the user should know about]

## Suggested next step
[Hand-off to FITq audit / Trust Centre / Tracker, or "build the top 3 pages"]
```

### Example 1 — Happy path (Marketing lead, Freshworks-style brief)

> **Built for:** Marketing / Growth Lead
> **Inputs used:** Category: B2B service desk software · ICP: mid-market IT at 200-2000 employee companies · Competitors: ServiceNow, Zendesk · Markets: DACH, Nordics
>
> ## The 25-prompt pack
>
> | # | Prompt | Category | Decides | Target page | Market |
> |---|---|---|---|---|---|
> | 1 | ServiceNow alternatives for mid-market | Shortlist | 5/5 | /alternatives/servicenow [TO BUILD] | DACH+Nordics |
> | 2 | Zendesk vs Freshworks | Shortlist | 5/5 | /compare/zendesk [EXISTS] | DACH+Nordics |
> | 3 | is Freshworks DSGVO konform | EU Privacy | 5/5 | /trust [TO BUILD] | DACH (DE) |
> | 4 | does Freshworks offer EU data residency | EU Privacy | 5/5 | /trust/data-residency [TO BUILD] | DACH+Nordics |
> | 5 | Freshworks AVV Vertrag download | EU Privacy | 5/5 | /trust/dpa [TO BUILD] | DACH (DE) |
> | 6 | who are Freshworks subprocessors | EU Privacy | 5/5 | /trust/subprocessors [TO BUILD] | DACH+Nordics |
> | 7 | Freshworks pricing for 500 agents | Pricing | 5/5 | /pricing [EXISTS] | DACH+Nordics |
> | 8 | how long does Freshworks implementation take | Implementation | 4/5 | /implementation [TO BUILD] | DACH+Nordics |
> | 9 | does Freshworks integrate with Slack | Integration | 4/5 | /integrations/slack [EXISTS] | DACH+Nordics |
> | 10 | Freshworks for IT teams in DACH | Role-based | 4/5 | /it-teams [TO BUILD] | DACH (DE+EN) |
> | 11 | beste service desk software für deutsche Unternehmen | Shortlist | 4/5 | /alternatives/servicenow [TO BUILD] | DACH (DE) |
> | 12 | Zendesk Alternative für Mittelstand | Shortlist | 4/5 | /alternatives/zendesk [TO BUILD] | DACH (DE) |
> | 13 | Freshworks SOC 2 ISO 27001 | EU Privacy | 4/5 | /trust [TO BUILD] | All EU |
> | 14 | Freshworks data center Frankfurt | EU Privacy | 4/5 | /trust/data-residency [TO BUILD] | DACH (DE) |
> | 15 | Freshworks vs ServiceNow für Sicherheitsteams | Shortlist | 4/5 | /compare/servicenow [TO BUILD] | DACH (DE) |
> | 16 | Freshworks customer support time to value | Implementation | 3/5 | /implementation [TO BUILD] | DACH+Nordics |
> | 17 | Freshworks API documentation | Integration | 3/5 | /developers [EXISTS] | All EU |
> | 18 | Freshworks customer reviews 2026 | Shortlist | 3/5 | /reviews [TO BUILD] | DACH+Nordics |
> | 19 | best service desk for Nordic IT teams | Role-based | 3/5 | /nordics [TO BUILD] | Nordics |
> | 20 | Freshworks WCAG accessibility | EU Privacy | 3/5 | /trust/accessibility [TO BUILD] | Nordics |
> | 21 | Freshworks SAML SSO setup | Integration | 3/5 | /sso [EXISTS] | All EU |
> | 22 | Freshworks ticket automation | Implementation | 3/5 | /features/automation [EXISTS] | All EU |
> | 23 | Freshworks for RevOps teams | Role-based | 2/5 | /revops [TO BUILD] | All EU |
> | 24 | Freshworks history and founders | Shortlist | 2/5 | /about [EXISTS] | All EU |
> | 25 | what is a service desk | Shortlist | 1/5 | /glossary/service-desk [TO BUILD] | All EU |
>
> ## Top 10 to ship (ordered by build priority)
>
> 1. **/trust** — Trust Centre — wins 4 disqualifier prompts (3, 5, 6, 13). Highest leverage page in this pack. → **Hand off to `optise-helix-eu-trust-centre`**
> 2. **/alternatives/servicenow** — Alternatives page — wins prompt 1 (5/5) and 11. Competitor with the largest EU footprint.
> 3. **/trust/data-residency** — wins prompts 4 and 14. Standalone page so DACH buyers can verify in 10 seconds.
> 4. **/trust/dpa** — wins prompt 5. Self-serve DPA download = procurement-ready.
> 5. **/trust/subprocessors** — wins prompt 6. Live updated list with 30-day notice policy.
> 6. **/compare/servicenow** — wins prompt 15. The German-language variant matters.
> 7. **/it-teams** — wins prompt 10. Role-based landing page for the highest-fit ICP.
> 8. **/implementation** — wins prompts 8 and 16. Reduces sales cycle friction.
> 9. **/alternatives/zendesk** — wins prompt 12. Mittelstand framing.
> 10. **/nordics** — wins prompt 19. Standalone page for the Nordics market.
>
> ## What this pack is missing
> No prompt for AI Act compliance yet. Add one once your AI features ship and you have a stance on EU AI Act risk classification.
>
> ## Suggested next step
> Run `optise-helix-eu-trust-centre` to draft the Trust Centre page that answers prompts 3, 4, 5, 6, 13, 14, 20 in one shot. After that, run `optise-helix-fitq-audit` on `/pricing` and `/integrations/slack` since both are existing pages that probably need tightening to actually win their prompts.

### Example 2 — Partial data (founder, no markets specified)

> I have your category and competitors but I need one more thing: which EU markets should I target?
>
> Pick 1-3 to start, or "all" for the broad pack:
> - **DACH** (Germany, Austria, Switzerland) — most rigorous GDPR market, best for trust-led plays
> - **Nordics** (SE, DK, NO, FI) — highest EU AI adoption, English-friendly
> - **France** — French-language search dominates, sovereignty-conscious
> - **Benelux** (NL, BE, LU) — multinational B2B, English-friendly
> - **Southern Europe** (ES, IT, PT) — local-language only, price-sensitive
> - **All EU**
>
> Once I have this I'll build the pack in one shot.

### Example 4 — Manual / API mode (structured input → structured output)

**Input (JSON):**
```json
{
  "category": "data warehouse",
  "icp": "mid-market data team",
  "competitors": ["Snowflake", "Databricks"],
  "markets": ["DACH"],
  "mode": "manual"
}
```

**Output (markdown table + JSON dual format, no conversational framing):**

```markdown
| # | Prompt | Category | Decides | Target page | Market |
|---|---|---|---|---|---|
| 1 | Snowflake vs [you] | Shortlist | 5/5 | /compare/snowflake | DACH |
| 2 | is [you] DSGVO konform | EU Privacy | 5/5 | /trust | DACH (DE) |
... 23 more rows ...
```

```json
{
  "pack": [
    {"prompt": "Snowflake vs [you]", "category": "shortlist", "score": 5, "target_page": "/compare/snowflake", "market": "DACH", "status": "TO_BUILD"},
    {"prompt": "is [you] DSGVO konform", "category": "eu_privacy", "score": 5, "target_page": "/trust", "market": "DACH-DE", "status": "TO_BUILD"}
  ],
  "top_10_build_order": ["/trust", "/compare/snowflake", ...],
  "calibration": {"5/5": 7, "4/5": 9, "3/5": 6, "2/5": 2, "1/5": 1}
}
```

### Example 3 — Edge case (rushed user, 10 mins to a call)

> **Top 10 (rushed). Built using sensible defaults: Gong, Clari as competitors; DACH + Nordics. Reply if these are wrong, otherwise this is your pack:**
>
> 1. Gong vs [you] — Compare page — 5/5
> 2. is [you] DSGVO konform — Trust Centre — 5/5 (DACH)
> 3. Clari alternatives EU — Alternatives page — 5/5
> 4. [you] EU data residency — Trust/Residency — 5/5
> 5. [you] DPA download — Trust/DPA — 5/5
> 6. [you] pricing for [ICP] — Pricing — 5/5
> 7. [you] vs Gong vs Clari — Comparison — 4/5
> 8. how long to implement [you] — Implementation — 4/5
> 9. does [you] integrate with HubSpot — Integration — 4/5
> 10. [you] for RevOps in DACH — Role-based — 4/5
>
> *Generated 12:34 GMT. Run again with full inputs after your call for the complete 25.*

---

## Section 6 — Edge Case Handling

### Universal
- **First-time user:** Brief 3-sentence explanation of what a prompt pack is, then ask for the 4 inputs. Do not lecture.
- **Returning user:** Check memory for prior pack. If found, offer to extend rather than replace.
- **Rushed user:** Detect time-pressure language. Output top-10 only with sensible defaults, time-stamp the response.
- **Frustrated user (prior bad output):** Acknowledge directly, ask which prompts felt generic, regenerate with category labels visible and scoring rationale shown.
- **Out-of-scope request:** If the user asks for SEO keyword research, traditional Google rankings, or US-only prompts, redirect: "This skill is for European B2B AEO prompts. For US prompts, use [other tool]. For SEO keywords, use [other tool]."

### Data
- **Full data (all 4 inputs):** Proceed directly to generation.
- **Partial data (3 of 4 inputs):** Ask only for the missing one.
- **Partial data (2 or fewer):** Ask once for all missing fields in a single consolidated message.
- **No data:** Ask the 4 inputs as one consolidated question.
- **Conflicting data (memory says X, message says Y):** Honor the message, confirm the override at the top of the output.
- **Stale data (memory >6 months old):** Confirm before using: "Memory says your competitors are X, Y. Still accurate?"

### Platform
- **Connected mode (memory available):** Use memory to skip clarifying questions; confirm context at top of output.
- **Manual mode (JSON / structured):** Skip persona detection, skip conversational framing, output table only in markdown + JSON dual format.
- **Mixed mode:** Ask only for missing fields.
- **API/developer mode:** Same as manual mode. Add a JSON output block at the end of the markdown for programmatic consumption.

### Context
- **Normal:** Full output, all sections.
- **Crisis/urgent:** Top-10 only, defaults applied, time-stamped.
- **Time-sensitive:** Same as urgent.
- **Regulated vertical (health-tech, fin-tech, legal-tech):** Heavily weight Category 4 prompts. Add vertical-specific compliance terms (e.g., BfArM/DiGA for health in Germany, MiCA for fintech). Recommend immediate handoff to `optise-helix-eu-trust-centre`.
- **Non-EU user wanting EU pack:** Confirm EU is the target. Ask which markets. Add a note that EU prompts differ from US prompts.

### Composition rules (when 2+ contexts combine)

When multiple edge cases apply to the same request, these rules resolve the conflict:

- **Rushed + Frustrated:** Frustration wins. The user's prior bad experience is more important than saving 30 seconds. Acknowledge in one line ("Got it — re-running with the methodology visible."), then output the pack with category labels and scoring rationale visible. No apology spiral.

- **Rushed + Regulated vertical:** Vertical wins. Even rushed users in regulated verticals must see Category 4 prompts — skipping them is a real liability. Output top-10 with at least 5 of the 10 being Cat 4 compliance prompts. Still time-stamp.

- **Stale memory + new request:** Always ask once to confirm the stale data is still accurate before using it. Never assume. One-line question: *"Memory says your competitors are X, Y. Still accurate?"*

- **CEO + Ingest mode:** CEO output format (top-10 only, CFO-grade close) + ingest workflow (score the user's list, don't generate new prompts). Output: top-10 drawn from the user's list ranked by score, with the "pages you have vs pages you need to build" calculation at the close.

- **First-time user + Regulated vertical:** Educate first (3-4 sentence explanation of what a prompt pack is in regulated context), then offer to build with a strong vertical-specific framing. Don't assume regulated-vertical users know the Optise methodology.

- **Manual mode + any persona:** Manual/JSON mode overrides persona detection. Structured input → structured output, no conversational framing regardless of who's calling the skill.

---

## Section 7 — Anti-Hallucination Rules

All 9 base rules from `references/anti-hallucination-base.md` apply verbatim. In addition:

**Domain rule 1 (skill-specific):** When ranking prompts by "decides deals" score, never assign 5/5 to a prompt category the user hasn't validated against their own sales calls. If the user is unsure whether a category-4 (compliance) prompt actually decides their deals, score it 4/5 with a note: *"Score conservative — confirm with your sales team that compliance is actually disqualifying buyers."*

**Domain rule 2 (skill-specific):** Never invent competitor names. If the user gives one competitor, generate prompts using just that competitor — do not infer "you probably also compete with X."

**Domain rule 3 (skill-specific):** Never invent EU market presence. If the user says "DACH" but there's no signal they sell into Austria or Switzerland specifically, default to Germany only and ask: *"DACH usually means Germany + Austria + Switzerland. Are you actually selling into all three, or just Germany?"*

**Domain rule 4 (skill-specific):** Never generate a German, French, Dutch, Spanish, or Italian prompt that you cannot back-translate to English. If you're unsure of the local-language idiom, ask for confirmation: *"I'm generating a German variant. Want me to include native-language prompts or English-only?"*

**Domain rule 5 (skill-specific):** Never claim a prompt has search volume. The skill scores intent, not volume. Output that says "this prompt gets 1,000 searches/month" is fabrication.

---

## Section 8 — Trigger Phrases

### Explicit triggers
- "build me an AEO prompt pack"
- "what AI search prompts should I rank for"
- "what do European B2B buyers ask ChatGPT about [my category]"
- "AI search prompt research"
- "prompt pack for [my product / category]"
- "what should we rank for in ChatGPT / Perplexity / Gemini"
- "Optise prompt pack"
- "Helix prompt pack"
- "generate AEO prompts"

### Contextual triggers
- When user mentions "AEO" AND "prompts" in the same message
- When user mentions a B2B category AND a European market in the same message
- When user mentions a competitor name AND asks "what do buyers search for"
- When memory contains a prior AEO conversation AND user asks "what's next"
- When user has just read the Optise EU AEO Playbook (memory or conversation evidence) and asks "where do I start"

### Do NOT trigger when
- User asks about traditional Google SEO keyword research → redirect to a keyword tool
- User asks about US-only prompts → confirm EU scope first
- User asks about social media post ideas → out of scope
- User asks how to write content for one specific page → defer to `optise-helix-bluf-writer`
- User asks "how is my page ranking in ChatGPT" → defer to `optise-helix-fitq-audit` or `optise-helix-aeo-tracker`

### Handoff to other skills
- If request mentions a URL to audit → defer to `optise-helix-fitq-audit`
- If request mentions trust centre / GDPR / DPA → after generating the pack, hand off to `optise-helix-eu-trust-centre`
- If request mentions writing the page opening → defer to `optise-helix-bluf-writer`
- If request mentions tracking what's working → defer to `optise-helix-aeo-tracker`
- If request mentions agent-readiness or "not ideal for" → defer to `optise-helix-race-audit`
