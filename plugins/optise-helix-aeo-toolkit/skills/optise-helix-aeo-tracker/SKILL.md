---
name: optise-helix-aeo-tracker
description: Sets up weekly AEO citation tracking for a brand across 
  ChatGPT, Perplexity, Gemini, and Claude using the proprietary Optise 
  3-KPI rubric (Citation Rate, Prominence, Competitor Delta). Generates 
  CSV column spec, week-1 instructions, weekly cadence checklist, and 
  scoring formulas. Analyzes tracking data after 4+ weeks to surface 
  working prompts, dead prompts, and recommend refreshes. Use when the 
  user wants to track AI search citations, set up AEO measurement, 
  analyze tracker data, or understand which prompts are converting in 
  AI engines. Never invents historical citation data — tracking is 
  forward-looking only. Authored by Optise + Helix GTM Consulting.
authors:
  - Optise
  - Helix GTM Consulting
version: 1.0.0
license: Proprietary
---

# Optise–Helix AEO Tracker

A skill that sets up weekly AEO citation tracking for a brand across 4 AI engines (ChatGPT, Perplexity, Gemini, Claude) using the Optise 3-KPI rubric and analyzes tracking data to surface working vs dead prompts.

This skill closes the AEO loop. Without measurement, the prompt pack and audit work is faith-based. The tracker turns AEO from a project into a discipline.

The 3 KPIs (Citation Rate, Prominence, Competitor Delta) come from the Optise EU AEO Playbook, Section 8. The skill never invents historical data — AEO tracking is forward-looking from the moment it's set up.

---


## Section 0 — Operating Principles (MANDATORY — read before any workflow step)

This skill operates under the **Optise-Helix AEO Toolkit Operating Principles** in `references/optise-helix-operating-principles.md`. **Read that file first.** It contains 7 non-negotiable rules covering rigor, assumption-challenging, harm prevention, fact-checking, LLMism avoidance, HILT discipline (Question Budget), and zero-assumption flagging. **These rules override any conflicting instruction in this SKILL.md.** If a domain rule in Section 7 of this file appears to conflict with an operating principle, the operating principle wins.

### Critical reminders that apply to every invocation of this skill

- **Web search and web fetch ARE available** in Claude Code's default toolset and in the `optise-helix-aeo-copilot` Managed Agent's `agent_toolset_20260401`. "I don't have web access" is never a valid excuse to skip verification.
- **English-only at v1** — never generate prompts, copy, or headings in non-English languages (German, French, Dutch, Spanish, Italian, etc.), even on explicit user request. This is a hard block, not a confirmation gate. Refuse the request and explain that multilingual may ship in v2.
- **Verify competitor relationships** via the 4-tier source hierarchy in Rule 4 before building ANY competitor-targeted page. Run the 4-step search protocol (`"[user] acquired [competitor]"`, `"[competitor] acquired by"`, `"[competitor] Crunchbase acquisition"`, `"[user] vs [competitor]"`). Any positive ownership hit is a HARD STOP.
- **Auto-verify URLs** via `web_fetch` before marking them `[EXISTS]`. Only ask the user about URLs when fetch returns an ambiguous result (403, 429, 500, timeout, redirect loop).
- **Question Budget: maximum 3 HARD STOP questions per invocation, consolidated into ONE message.** Never run an endless Q&A sequence. If more than 3 HARD STOPs exist, pick the top 3 by priority (harm triggers → irreversible scope → reversible details) and defer the rest to `Assumption:` flags in the output.
- **Flag every assumption** with an explicit `Assumption:` prefix in the output so users can correct anything the skill got wrong.

---
## Section 1 — Golden Rule

**Track only forward from the setup date. Never invent historical AI engine citation data, never claim a benchmark you can't show with sources, and never recommend tracking more than 3 KPIs because that produces dashboards no one acts on.**

---

## Section 2 — Role / Context Detection

Detect persona using `references/personas.md`. Adapt output:

| Persona | Output adaptation |
|---|---|
| **CEO / Founder** | Output the 3 KPIs as a single sentence each. Skip the formulas. Close with "review weekly for 4 weeks, then run analysis mode for the verdict." |
| **Marketing / Growth Lead (default)** | Full template: CSV columns, week-1 instructions, weekly checklist, formulas, the diagnostic. |
| **Web Team** | JSON schema instead of CSV. Add "what to log in your data warehouse" section if user has one. |
| **RevOps / Sales Ops** | Add CRM trigger column. Explain how to map AI engine citations to lead source attribution. Suggest the "AI assisted research" CRM field. |
| **Security / Privacy / Legal** | Filter to compliance-prompt tracking only (Cat 4 from prompt-pack-builder). Add a "did procurement reach our Trust Centre via AI" measurement column. |

**Detection signals:** see `references/personas.md`. Default = Marketing/Growth Lead.

**Platform mode:**
- Connected: use memory for prior pack data and prior tracking
- Manual / API: JSON in (prompt list), JSON out (tracking schema)
- Mixed: ask for missing fields only

**Urgency:** "Quick" → minimal 5-column CSV template only, no rubric explanation, time-stamped.

---

## Section 3 — Priority Framework

When setting up tracking for a new pack, allocate columns in this order:

1. **The 3 KPI columns first** (mention Y/N, prominence rank, competitor delta) — these are mandatory.
2. **Engine identifier column** (which AI engine was tested) — mandatory for the 4-engine rule.
3. **Date column** (week of measurement) — mandatory for weekly cadence.
4. **Prompt category column** (from the 6 Optise categories) — useful for cross-cutting analysis.
5. **Target page URL column** — for handoff to FITq audit when a prompt is dead.
6. **Optional columns based on persona** — RevOps adds CRM trigger; Security adds compliance flag; Web team adds JSON path.

**Tie-breakers:**
1. **Mandatory columns are non-negotiable.** Even rushed mode has all 3 KPIs.
2. **Persona-specific columns come last** to keep the base template universally usable.
3. **Never add a column the user can't fill.** If they don't have CRM data, skip the CRM column.

When analyzing tracking data (mode 2), prioritize:
1. **Dead prompts first** (0% citation after 4 weeks) — these need to be swapped.
2. **Negative competitor delta prompts** (you're losing ground) — these need FITq audits on the target page.
3. **Buried prominence prompts** (mentioned but late) — these need BLUF rewrites.
4. **Working prompts** (above benchmark) — flag what's working so the user doesn't break it.

---

## Section 4 — Workflow Steps

### Step 0: Detect mode

- **Setup mode** (default) — user has a prompt pack and wants to start tracking
- **Analysis mode** — user has 4+ weeks of tracking data and wants a verdict
- **Single-prompt mode** — user wants to track 1 prompt, not a full pack
- **Diagnostic mode** — user says "tracker isn't working" → run the 6-step diagnostic from the rubric

### Step 1: Capture inputs

**For setup mode:**
- **Required:** prompt pack (or reference to one), brand name, 1-2 competitors
- **Optional:** EU market focus, regulated vertical, CRM tool name (for RevOps persona)

**For analysis mode:**
- **Required:** 4+ weeks of tracking data (CSV or pasted table)
- **Optional:** the original prompt pack for context

**Failure mode:** If setup mode and no prompt pack → recommend `optise-helix-prompt-pack-builder` first. Don't generate trackers for unknown prompts.

### Step 2: Detect persona

Use `references/personas.md`. Default Marketing if ambiguous. Skip in manual mode.

### Step 3: Generate the tracking template (setup mode)

Build:
- **CSV column spec** with columns from Priority Framework Section 3
- **Example row** so the user knows what valid data looks like
- **Week-1 instructions** describing how to run the first measurement
- **Weekly checklist** for ongoing cadence

Use `references/tracker-rubric.md` for the 3 KPI formulas. Use `references/prompt-categories.md` to assign each prompt a category column value.

**Tracker ID convention:** When in manual / API mode, generate a `tracker_id` as `<brand-slug>-<YYYY-MM-DD>` where brand-slug is the lowercase brand name with non-alphanumerics replaced by hyphens (e.g., "freshworks" or "the-london-tea-co"), and date is the setup date in ISO format. This makes trackers identifiable across multiple invocations and forms a stable handoff key for memory storage.

### Step 4: Analyze the data (analysis mode)

For each prompt in the user's data:
1. Calculate Citation Rate (% Mentioned over total measurements)
2. Calculate Prominence Score (average prominence rank for Mentioned rows)
3. Calculate Competitor Delta (your citations - avg of competitor citations)
4. Classify prompts into: working / improving / dead / declining

**Output:** Top 5 working prompts, top 5 dead prompts, top 3 declining prompts, and a one-line verdict on overall AEO health.

### Step 5: Run diagnostics (diagnostic mode)

Walk through the 6-step diagnostic from `references/tracker-rubric.md`. Ask the user to confirm each step. Identify the most likely root cause.

### Step 6: Hand off

- **Setup mode:** Recommend running for 4 weeks before re-engaging.
- **Analysis mode with dead prompts:** Hand off to `optise-helix-prompt-pack-builder` refresh mode to swap dead prompts.
- **Analysis mode with negative delta:** Hand off to `optise-helix-fitq-audit` on the target pages of the losing prompts.
- **Analysis mode with buried prominence:** Hand off to `optise-helix-bluf-writer` to rewrite the BLUFs of buried prompts.
- **Diagnostic mode resolves to "you need audits":** Hand off to `optise-helix-fitq-audit` and `optise-helix-race-audit`.

---

## Section 5 — Output Format (with Concrete Examples)

### Standard format (Marketing persona, setup mode)

```markdown
**Built for:** [persona]
**Brand:** [name]
**Tracking start date:** [today]
**Measurement cadence:** weekly

## Tracking template

### CSV column spec
[column list with types and example values]

### Example row
[1 example row of valid data]

### Week-1 instructions
[step-by-step]

### Weekly checklist (every Monday)
[checklist]

### The 3 KPI formulas
[from rubric]

### Healthy benchmarks
[A/B/C/D/F bands]

## Suggested next step
[Hand off]
```

### Example 1 — Setup mode, Freshworks pack

> **Built for:** Marketing / Growth Lead
> **Brand:** Freshworks
> **Competitors tracked:** ServiceNow, Zendesk
> **Tracking start date:** 2026-04-12
> **Measurement cadence:** Weekly (every Monday)
>
> ## Tracking template
>
> ### CSV column spec
>
> | Column | Type | Example | Notes |
> |---|---|---|---|
> | week | date | 2026-04-12 | Always Monday |
> | engine | enum | ChatGPT / Perplexity / Gemini / Claude | All 4 mandatory per row group |
> | prompt | string | "best service desk software for German Mittelstand" | Verbatim from pack |
> | category | enum | Shortlist / Pricing / Implementation / EU Privacy / Integration / Role-based | Optise 6 categories |
> | mentioned | bool | TRUE | Did the answer name your brand? |
> | cited_with_link | bool | TRUE | Did the answer link to your domain? |
> | prominence | int | 2 | 1=first, 2=top-3, 3=late, 4=buried, blank if not mentioned |
> | competitor_1_mentioned | bool | TRUE | ServiceNow |
> | competitor_2_mentioned | bool | FALSE | Zendesk |
> | target_page | string | /alternatives/servicenow | From prompt pack |
> | notes | string | "Cited as #2 of 5 options" | Optional context |
>
> ### Example row
>
> ```csv
> 2026-04-12,ChatGPT,"best service desk software for German Mittelstand",Shortlist,TRUE,TRUE,2,TRUE,FALSE,/alternatives/servicenow,"Cited as #2 of 5 options"
> ```
>
> ### Week-1 instructions
>
> 1. **Open a fresh tab in each AI engine** (logged-out where possible to avoid personalization).
> 2. **Type each prompt verbatim** — exactly as written in the pack. Don't paraphrase.
> 3. **Read the answer carefully** for: (a) brand name mentions (you and competitors), (b) order of mention, (c) whether your domain is linked.
> 4. **Record one row per (prompt × engine) combination.** 25 prompts × 4 engines = 100 rows for week 1.
> 5. **Save with the filename** `aeo-tracker-2026-04-12.csv`. Same filename pattern weekly.
>
> Time investment: 60-90 minutes for the first run, dropping to 30-45 once you build muscle memory.
>
> ### Weekly checklist (every Monday)
>
> - [ ] Pull last week's CSV from the prior file
> - [ ] Add a new "week" column block for this Monday
> - [ ] Run all 25 prompts × 4 engines (or batch — see batching tips below)
> - [ ] Calculate the 3 KPIs (formulas below)
> - [ ] Compare against last week — flag any prompts that gained or lost prominence
> - [ ] Update your team's AEO dashboard with the 3 KPIs only — never the 100-row raw table
>
> ### The 3 KPI formulas
>
> **Citation Rate:**
> ```
> (count of rows where mentioned=TRUE) / (total rows for the week) × 100
> ```
>
> **Prominence Score:**
> ```
> sum of prominence values / count of mentioned rows
> (lower is better; target <2.0)
> ```
>
> **Competitor Delta:**
> ```
> (your citation count) - (avg of competitor 1 and competitor 2 citation counts)
> (positive = winning; zero = parity; negative = losing)
> ```
>
> ### Healthy benchmarks
>
> - **A grade:** Citation Rate >40% — you're winning AEO
> - **B grade:** 20-40% — defensible, expected with a working Trust Centre
> - **C grade:** 10-20% — improving from FITq audits will move you here
> - **D grade:** 5-10% — sporadic, needs structural fixes
> - **F grade:** <5% — functionally invisible
>
> ### Batching tips
>
> - **Run by engine, not by prompt.** Open ChatGPT, run all 25 prompts, then move to Perplexity. Faster than switching engines per prompt.
> - **Use a separate browser profile** for tracking so your normal usage doesn't pollute the personalization layer.
> - **Don't multi-task.** AI engine answers update mid-session — you'll get inconsistent data if you have 4 tabs open simultaneously asking the same question.
>
> ## Suggested next step
>
> Run the tracker for 4 weeks. After week 4, run this skill again in **analysis mode** with your accumulated data. I'll surface working prompts, dead prompts, and what to do next.

### Example 2 — Edge case (no prompt pack)

> You don't have a prompt pack yet, and the tracker is built around tracking specific prompts that buyers actually ask. Without a pack, I'd be tracking guesses — which defeats the purpose.
>
> **What to do first:** Run `optise-helix-prompt-pack-builder` to generate your 25 prompts. That takes ~5 minutes and gives you the input this skill needs.
>
> Then come back here and I'll set up the tracker.

### Example 3 — Analysis mode (4 weeks of data)

> **Analysis of your 4-week tracking data**
>
> **Current AEO health:** Citation Rate 18.4% — **Grade C**. You're occasionally cited, improving from a fixable position.
>
> **3-KPI snapshot:**
> | KPI | Week 1 | Week 4 | Trend |
> |---|---|---|---|
> | Citation Rate | 12.0% | 18.4% | ↑ +6.4 pts |
> | Prominence Score | 2.8 | 2.4 | ↑ improving |
> | Competitor Delta | -3 | +1 | ↑ now winning |
>
> ## Top 5 working prompts (highest citation × prominence)
>
> 1. **"Freshservice EU data residency"** — cited in 7/8 weeks across all 4 engines, prominence 1.4 (first or near-first). **Don't break this.** This is your Trust Centre paying off.
> 2. **"best service desk for German Mittelstand"** — cited in 5/8 across all 4 engines, prominence 2.0.
> 3-5. [other working prompts]
>
> ## Top 5 dead prompts (0% citation after 4 weeks)
>
> 1. **"Freshworks customer reviews 2026"** — 0/16 measurements. **Recommend swap.** This is generic and probably outranked by G2 directly.
> 2. **"Freshworks history and founders"** — 0/16. **Recommend swap.** Wrong intent (buyers don't ask about company history).
> 3-5. [other dead prompts]
>
> ## Top 3 declining prompts
>
> 1. **"Zendesk vs Freshworks"** — was citing in week 1-2, now down to 1/8 in week 4. **Recommend FITq audit on `/compare/zendesk`.** Likely Zendesk shipped a comparison page that displaced you.
>
> ## Suggested next steps
>
> 1. **Swap the 5 dead prompts** via `optise-helix-prompt-pack-builder` refresh mode. Pick 5 new prompts in the same categories.
> 2. **Run `optise-helix-fitq-audit` on `/compare/zendesk`** to find what's letting Zendesk's page outrank yours.
> 3. **Re-run this analysis after 4 more weeks** to verify the swap and audit fixes worked.

### Example 4 — Manual / JSON mode

**Input:**
```json
{
  "mode": "setup",
  "brand": "Freshworks",
  "competitors": ["ServiceNow", "Zendesk"],
  "prompts": [
    {"text": "best service desk for German Mittelstand", "category": "shortlist"},
    {"text": "is Freshworks GDPR compliant", "category": "eu_privacy"}
  ]
}
```

**Output:**
```json
{
  "tracker_id": "freshworks-2026-04-12",
  "csv_columns": [
    {"name": "week", "type": "date"},
    {"name": "engine", "type": "enum", "values": ["ChatGPT", "Perplexity", "Gemini", "Claude"]},
    {"name": "prompt", "type": "string"},
    {"name": "category", "type": "enum", "values": ["shortlist", "pricing", "implementation", "eu_privacy", "integration", "role_based"]},
    {"name": "mentioned", "type": "bool"},
    {"name": "cited_with_link", "type": "bool"},
    {"name": "prominence", "type": "int", "range": [1, 4], "nullable": true},
    {"name": "competitor_1_mentioned", "type": "bool"},
    {"name": "competitor_2_mentioned", "type": "bool"},
    {"name": "target_page", "type": "string"},
    {"name": "notes", "type": "string", "optional": true}
  ],
  "kpi_formulas": {
    "citation_rate": "(rows where mentioned=true) / (total rows) * 100",
    "prominence_score": "sum(prominence) / count(mentioned=true rows); lower is better; target <2.0",
    "competitor_delta": "(your citations) - avg(competitor citations)"
  },
  "weekly_cadence": "Every Monday",
  "minimum_runs_before_analysis": 4,
  "generated_at": "2026-04-12T13:25:00Z"
}
```

---

## Section 6 — Edge Case Handling

### Universal
- **First-time user:** 3-sentence explanation of AEO tracking. Offer to set up.
- **Returning user:** Check memory for prior tracker setup. Offer to load.
- **Rushed user:** Output minimal 5-column CSV template only. Skip rubric and instructions.
- **Frustrated user, "tracker isn't working":** Run diagnostic mode (Step 5).
- **Out-of-scope:** If user asks for general AEO advice → defer to a different skill. If user asks to write the prompts → defer to `optise-helix-prompt-pack-builder`.

### Data
- **Full data (pack + brand + 2 competitors):** Highest quality template.
- **Pack + brand only (no competitors):** Generate template, but Competitor Delta column will be unfillable. Ask once: "Without competitors, you can track Citation Rate and Prominence but not Delta. Want to add 1-2 competitors or proceed without?"
- **No pack:** Halt, recommend prompt-pack-builder.
- **Conflicting data:** If the user's pack has different prompts than memory, confirm which to use.
- **Stale tracking data (>3 months):** AI engine indexes have shifted. Recommend a fresh week-1 measurement to recalibrate.
- **Malformed analysis data:** When the user provides analysis-mode data missing required columns (week, engine, prompt, mentioned, prominence, competitor mentions), halt and request the missing column rather than inferring. Output the column spec from Section 5 Example 1 so the user knows what's expected. Never silently ignore missing columns or fill with defaults.
- **Historical data request:** Decline. Explain forward-looking only.

### Platform
- **Connected mode:** Use memory for prior pack and tracking data.
- **Manual / API:** JSON in/out, no conversational framing.
- **Mixed mode:** Use what memory has, ask for missing fields.

### Context
- **Normal:** Full template.
- **Crisis / urgent:** Minimal 5-column CSV.
- **Regulated vertical:** Add compliance-prompt tracking column. Score Cat 4 prompts separately because they have higher procurement stakes.
- **Single-prompt mode:** Generate tracker for 1 prompt with the same 3 KPIs. Useful for experiments.

### Composition rules
- **Rushed + No competitors:** Generate the minimal template with a "Competitor Delta = pending" placeholder. Don't halt.
- **Analysis mode + dead prompts >50% of pack:** Don't recommend incremental swaps — recommend a full pack regeneration via `optise-helix-prompt-pack-builder` new mode.
- **Analysis mode + improving across all 3 KPIs:** Lead with the win. Don't manufacture problems.
- **CEO + Setup mode:** Skip the formula explanations. Output only: 3 KPIs (1 sentence each), the cadence, and "review weekly for 4 weeks then come back."
- **Manual mode + any persona:** Manual wins.
- **Analysis mode + Dead prompts >50% + Regulated vertical:** Recommend full pack regeneration AND a FITq audit on the Trust Centre simultaneously. In regulated verticals, dead compliance prompts often indicate the Trust Centre itself is invisible — fixing the pack alone won't help if the underlying page is broken. Hand off to BOTH `optise-helix-prompt-pack-builder` (new mode) AND `optise-helix-fitq-audit` (on the Trust Centre URL).

---

## Section 7 — Anti-Hallucination Rules

All 9 base rules from `references/anti-hallucination-base.md` apply. Additionally:

**Domain rule 1:** Never invent historical citation data. AEO tracking is forward-looking from setup date. If a user asks "which prompts cited me last month," explain that AI engine citation history is not retroactively available for individual brands.

**Domain rule 2:** Never invent benchmarks. The A/B/C/D/F bands in `references/tracker-rubric.md` come from Optise customer data and are the only defensible benchmarks. Don't make up "industry average" numbers.

**Domain rule 3:** Never recommend tracking more than 3 KPIs. The 3-KPI rule is the discipline. Adding "engagement", "sentiment", "share of voice", "competitive intent" produces dashboards no one acts on.

**Domain rule 4:** Never claim a prompt is "working" or "dead" before 4 weeks of data. The minimum sample is 4 weeks × 4 engines = 16 measurements per prompt for any classification.

**Domain rule 5:** Never invent prominence values. If the user's data has missing prominence for a Mentioned=Y row, flag it: "row [X] has mentioned=true but no prominence — please re-measure."

**Domain rule 6:** Never recommend swapping a prompt without checking the source category. Dead prompts get replaced in the SAME category — never replaced with prompts from a different category, because that breaks the pack's category balance.

---

## Section 8 — Trigger Phrases

### Explicit triggers
- "set up AEO tracking"
- "track AI search citations"
- "AEO measurement"
- "weekly tracker"
- "track which prompts are working"
- "citation rate tracking"
- "Optise tracker"
- "Optise AEO tracker"

### Contextual triggers
- User has just run `optise-helix-prompt-pack-builder` and asks "what next"
- User mentions tracking, measurement, weekly review AND AI engines
- User has 4+ weeks of citation data and asks for analysis
- User asks "how do I know if AEO is working"

### Do NOT trigger when
- User asks for a prompt pack → defer to `optise-helix-prompt-pack-builder`
- User asks for a page audit → defer to `optise-helix-fitq-audit`
- User asks for general AEO strategy → out of scope
- User asks for tracking historical data → decline (Domain rule 1)

### Handoff to other skills
- Setup complete → "run for 4 weeks then come back for analysis"
- Analysis with dead prompts → `optise-helix-prompt-pack-builder` refresh mode
- Analysis with negative delta → `optise-helix-fitq-audit` on target pages
- Analysis with buried prominence → `optise-helix-bluf-writer` for new BLUFs
- Diagnostic resolves to "needs audits" → `optise-helix-fitq-audit` and `optise-helix-race-audit`
