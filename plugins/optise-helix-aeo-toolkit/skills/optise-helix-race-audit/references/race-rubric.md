# RACE™ Scoring Rubric

## Authoritative method and evidence rules

Method identifier: **RACE bands 20261103**. This file is the sole scoring algorithm. Use the band rows below, not an additive feature checklist from any earlier skill body or example. This method identifier is separate from the unchanged package version.

For each signal, evaluate each row against observed evidence. All clauses joined by AND or listed as requirements must hold; an explicit OR requires at least one alternative. Do not infer a missing measurement. A specific observed failure described by a lower row caps the signal at that row, even when positive features match a higher row. If several failure rows apply, use the lowest cap. Otherwise use the highest row whose complete criteria are supported. If no complete row is supported, mark the signal unscored. If an unknown measurement could change the selected row or cap, mark the signal unscored and name that measurement. This resolves overlap without interpolation, feature addition or rounding. An observed absence is different from an unmeasured feature.

Record a receipt for each signal: matched row, source excerpt or measurement, measurement date, unknowns, and any lower cap. Do not infer mobile load time from TTFB, rendered content or first-scroll position from raw HTML, robots access from HTTP 200 alone, or third-party consistency from the page's own claims. For a pasted HTML audit, score only supported signals. A failed fetch produces a fetch-error report with no score.

Only when all four signals have supported scores, sum them directly. Each signal is in {0, 5, 10, 15, 20, 25}. Total is 0 through 100. Apply grades after summing: A at 90 through 100, B at 75 through 89, C at 60 through 74, D at 40 through 59, F at 0 through 39. Do not rescale a partial total, invent a missing value or round a total upward. If any signal is unscored, total and grade are unavailable. Preserve the individual receipts.

The grade describes this rubric only. It is not a measured probability of citations, agent recommendations or sales. Historical scores from a different method are not comparable. Reassess the original page evidence under this method before reporting a change. Proposed fixes have conditional band changes until retested.


**Used by:** `optise-helix-race-audit` (primary).
**Source:** Optise EU AEO Playbook, Section 6 (RACE™ — AI Agent Readiness Without Risk).
**Trademark:** RACE™ is an Optise framework. Always use the trademark on first mention.

The RACE framework scores a webpage on 4 signals for AI **agent** readiness — distinct from FITq, which scores AI **search citation** readiness. AI agents (the ones running multi-step buyer evaluation workflows) need different things than AI search engines.

Each signal scores 0-25, totaling 100. Same A/B/C/D/F grade bands as FITq.

## Contents
- Signal 1: Requirements
- Signal 2: Actions
- Signal 3: Constraints
- Signal 4: Evidence
- Total scoring + grade bands
- What this rubric does NOT score

---

## Signal 1 — Requirements (0-25)

**Definition:** Does this page state what's needed to use the product clearly enough that an AI agent can verify fit before recommending?

| Score | Criteria |
|---|---|
| **25** | Page lists prerequisites explicitly: required systems, data inputs, roles needed, time investment, technical skills. Each requirement is in extractable form (table or bullet list). Schema markup includes `Product` or `SoftwareApplication`. |
| **20** | Most prerequisites listed, but 1-2 dimensions missing (e.g., time investment vague). |
| **15** | Some requirements stated but buried in prose. Hard for an agent to extract. |
| **10** | Requirements implied but not stated. Agent would have to infer. |
| **5** | Page is brand-led; requirements absent. |
| **0** | Page actively obscures requirements (e.g., "contact sales for details"). |

**What to detect:**
- Presence of explicit "you need" / "prerequisites" / "requirements" sections
- Tables listing system/role/time inputs
- Schema.org `Product` or `SoftwareApplication` with `requirements` field
- Use of words: "requires", "needs", "must have", "depends on"

**Common failure modes:**
- "Easy to use, no setup required" — agents distrust this; they need specifics
- Implementation page with no prerequisites listed
- Pricing page with no infrastructure requirements

---

## Signal 2 — Actions (0-25)

**Definition:** Does this page describe the next-step process clearly enough that an AI agent can recommend a sequence?

| Score | Criteria |
|---|---|
| **25** | Page contains a numbered or sequenced process: who does what, how long it takes, what "done" looks like. Schema.org `HowTo` markup present. Each step is independently extractable. |
| **20** | Sequenced process present but missing 1 dimension (timing OR ownership OR done-state). |
| **15** | Process implied but not numbered/sequenced. |
| **10** | "Get started" CTA only, no actual process described. |
| **5** | Marketing copy with no process at all. |
| **0** | Process is explicitly hidden behind a sales motion. |

**What to detect:**
- Numbered lists of process steps
- `<ol>` tags with implementation/onboarding language
- Schema.org `HowTo` markup
- Words: "step 1", "first", "then", "finally", "after"
- Time estimates per step ("takes 30 minutes", "1 week onboarding")

**Common failure modes:**
- "Sign up to get started" with no actual sign-up flow shown
- Implementation timeline given as a single sentence ("takes 4-6 weeks")
- No ownership (who from buyer side does what)

---

## Signal 3 — Constraints (0-25)

**Definition:** Does this page honestly describe what the product is NOT good for? "Not ideal for" sections are the agent-readiness signal that distinguishes evaluable products from marketing-only ones.

| Score | Criteria |
|---|---|
| **25** | Page contains an explicit "not ideal for" section with 3+ honest constraints. Constraints are specific (company size, vertical, use case) — not generic. The page recommends alternatives where the user isn't a fit. |
| **20** | "Not ideal for" present but only 1-2 constraints, or constraints are vague ("complex enterprises"). |
| **15** | Constraints implied (e.g., "designed for SMB" implies not-for-enterprise). |
| **10** | No constraints stated; agent has to infer from positive claims. |
| **5** | Page makes universal claims ("works for any business"). |
| **0** | Page actively misrepresents fit ("perfect for everyone"). |

**What to detect:**
- Explicit "Not ideal for" / "Who shouldn't use" / "When NOT to choose" sections
- "Best for" sections that mention exclusions
- Comparison sections that admit when a competitor is better
- Linked alternatives for excluded segments

**Common failure modes:**
- Pages with no constraints at all (most common)
- Constraints listed only in pricing tier limitations (not the same)
- "Not ideal for" sections that are actually thinly disguised marketing ("not ideal for those who don't want to grow")

---

## Signal 4 — Evidence (0-25)

**Definition:** Is the proof above the fold? Agents weigh evidence by visibility, not by depth. A claim without nearby proof is treated as a marketing assertion.

| Score | Criteria |
|---|---|
| **25** | Every major claim has proof within 200 words: case study link, benchmark data, customer logo with attribution, named source. Proof is in the first scroll, not at the bottom. Schema.org `Review` or `Organization` markup with `aggregateRating` present. |
| **20** | Most claims have proof but proof is below the fold. |
| **15** | Some claims have proof, others don't. |
| **10** | Proof exists in PDFs or gated content only. |
| **5** | Marketing claims with no proof anywhere on the page. |
| **0** | Claims contradict the brand's third-party footprint (G2 reviews say one thing, page says another). |

**What to detect:**
- Linked case studies near each major claim
- Customer logos with named permission ("used by [Company]")
- Quantitative benchmarks with sources
- Schema.org `Review`, `AggregateRating`, `Organization`
- Position of proof (above vs below the fold — measure scroll position)

**Common failure modes:**
- Customer logos in a slider with no attribution
- Stats above the fold but case studies at the bottom
- "Trusted by 1000+ companies" with no names
- Awards/certifications mentioned without verification

---

## Total scoring and grade bands

Use the aggregation and grade boundaries in the authoritative method above. A means the highest rubric band, B the next band, then C, D and F. These labels do not prove actual citation or recommendation behaviour. Unknown signals prevent a total and grade.

---

## What this rubric does NOT score

1. **Search citation readiness.** That's FITq's job. RACE and FITq are complementary, not redundant.
2. **Buyer experience quality.** A RACE-A page can still be ugly. RACE measures agent-readability, not human delight.
3. **Sales conversion rate.** RACE records rubric evidence only; it does not predict recommendations or sales.

---

## Output format requirement

Every RACE audit must produce the following when evidence supports scoring. For missing measurements, replace the affected score, total and grade with unavailable and the missing evidence:
1. **Total score and grade band**
2. **Per-signal breakdown** (4 numbers, each with 1-line justification)
3. **Up to five evidenced fixes ranked by impact; fewer when fewer are supported** (each with effort estimate)
4. **A "honest constraints" template** for fix #1 if Constraints scored ≤15 (most common gap)
5. **A "what's already strong" section** so the user knows what NOT to break
