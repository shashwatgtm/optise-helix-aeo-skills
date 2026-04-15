---
name: optise-helix-eu-trust-centre
description: Generates a complete EU Trust Centre page that answers the 8 
  canonical EU buyer questions (GDPR compliance, data storage, residency, 
  DPA, subprocessors, data collection and retention, third-party AI 
  providers, security standards). Produces the full page in extractable 
  format with BLUF, answer blocks, JSON-LD FAQPage schema, and a DPA 
  request CTA. Uses proprietary Optise answer ordering (Q1→Q2→Q3→Q8→Q4→Q5→Q6→Q7) 
  optimized for European procurement review flows. Use whenever the user 
  needs to draft, audit, or expand a Trust Centre page, trust portal, 
  GDPR FAQ, security centre, or any page answering EU compliance questions. 
  Never invents data residency, certifications, or subprocessors. Authored 
  by Optise + Helix GTM Consulting.
authors:
  - Optise
  - Helix GTM Consulting
version: 1.0.0
license: Proprietary
---

# Optise–Helix EU Trust Centre Generator

Generates a complete EU Trust Centre page that answers all 8 canonical EU buyer questions in procurement-optimized order, with JSON-LD FAQPage schema and a DPA request CTA.

This is the European differentiator skill. EU B2B buyers evaluate compliance before anything else — a company without a findable, extractable Trust Centre is functionally invisible to EU procurement processes even if it's technically compliant. This skill turns compliance facts into citable, AI-engine-readable content.

The 8 questions come from the Optise EU AEO Playbook, Section 7 (page 12). The output order (Q1→Q2→Q3→Q8→Q4→Q5→Q6→Q7) is proprietary — it optimizes for the filter-then-verify flow EU security reviewers actually use.

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

**Never invent the user's compliance data. If the user doesn't know their data residency, subprocessor list, AI provider stack, or security certifications, use `[User to add: ...]` placeholders. Getting this wrong gets companies sued — placeholders are never the wrong answer; invented facts always are.**

---

## Section 2 — Role / Context Detection

Detect persona using `references/personas.md`. Adapt output:

| Persona | Output adaptation |
|---|---|
| **CEO / Founder** | Generate the page. Close with CFO-grade ask: "publishing this page costs nothing; not publishing costs [N] EU deals per quarter." |
| **Marketing / Growth Lead (default)** | Full page + JSON-LD schema + section-by-section copy + DPA CTA + handoff note. |
| **Web Team** | Full page as HTML file with JSON-LD in `<head>`. Skip marketing framing. Ready to paste into CMS. |
| **RevOps / Sales Ops** | Add a "what to log in CRM when a buyer hits this page" section with suggested UTM parameters and lead scoring impact. |
| **Security / Privacy / Legal (primary audience)** | Lead with legal precision. Flag every assumption. Add "what your DPO should verify before publishing." Highest fidelity output. |

**Detection signals:** see `references/personas.md`. Default for this skill is Security/Privacy/Legal or Marketing depending on context (unlike other skills where default is Marketing only).

**Platform mode:**
- **Connected:** use memory for prior Trust Centre drafts; offer to extend rather than regenerate
- **Manual / API:** JSON in (company facts), JSON out (page content + schema)
- **Mixed:** ask for missing fields only

**Urgency:** "Quick" → output only the 4 highest-priority questions (Q1, Q2, Q3, Q8) in abbreviated form. Time-stamped.

---

## Section 3 — Priority Framework

**Question priority order** (NOT the sequential order — this is what to fill first if the user has incomplete data):

1. **Q1 (GDPR compliance)** — Must answer. If "no" or "unsure", halt and ask user to confirm before writing.
2. **Q2 (Where is data stored)** — Must answer. If unknown, use `[User to add: exact region]` — never assume EU.
3. **Q8 (Security standards)** — Highest-frequency follow-up question from EU procurement. Answer even if certifications are in-progress.
4. **Q3 (EU data residency)** — Distinct from Q2. Q2 is where data IS, Q3 is what OPTIONS the buyer has.
5. **Q4 (DPA availability)** — Near-universal requirement. If no DPA exists yet, flag as P0.
6. **Q5 (Subprocessors)** — Publishing the list is the #1 trust signal for DACH Mittelstand buyers.
7. **Q6 (Data collection and retention)** — Important but lower procurement-priority than Q1-Q5.
8. **Q7 (Third-party AI providers)** — Growing in importance as EU AI Act kicks in August 2026.

**Tie-breakers:**
1. **EU AI Act matters more in 2026.** As the EU AI Act becomes fully applicable August 2026, elevate Q7 from "lower priority" to "medium priority."
2. **Regulated verticals change the order.** Health-tech adds BfArM/DiGA as Q8-adjacent. Fin-tech adds DORA as Q8-adjacent.
3. **Never skip a question.** Even if the answer is "not applicable" or "we don't use third-party AI", the question must be present so procurement reviewers see a complete list.

---

## Section 4 — Workflow Steps

### Step 0: Detect mode

- **New page** (default) — generate a fresh Trust Centre from user-provided facts
- **Section-only** — generate one specific section (e.g., just the DPA question)
- **Audit existing** — user has a published Trust Centre URL → hand off to `optise-helix-fitq-audit` with a custom prompt: *"Audit this URL for FITq, but specifically check whether each of the 8 EU buyer questions from `references/eu-buyer-questions.md` has a visible, extractable answer. For any question that's missing or weak, output the question number and the gap. Do not write new content — flag gaps only."* When FITq returns results, this skill reads the gap list and offers to generate replacement sections for any gaps.

### Step 1: Capture inputs

**Required (minimum):**
- Company name
- GDPR compliance status (yes/no/in-progress)
- Data residency (exact region — not "EU", the specific AWS/GCP/Azure region or data center city)
- DPA availability (available / in development / negotiable for enterprise only)

**Optional but preferred:**
- Subprocessor list (or link to live page)
- Security certifications (SOC 2, ISO 27001, BSI C5, etc. — with status: certified / in-progress / planned)
- Third-party AI providers and data flow
- Data retention periods
- Named DPO or Security Officer
- EU market focus (to prioritize DACH / Nordic / France-specific trust signals)

**Failure mode:** If fewer than 4 required inputs provided → ask once, listing all 4 required fields. Don't proceed with partial required inputs.

### Step 2: Detect persona

Use `references/personas.md`. Default is Security/Privacy/Legal for this skill (not Marketing) when signal is ambiguous.

### Step 3: Load the 8 EU buyer questions from reference

Read `references/eu-buyer-questions.md`. Apply the Answer Assembly Rule ordering (Q1→Q2→Q3→Q8→Q4→Q5→Q6→Q7).

### Step 4: Write the page BLUF (40-60 words)

Use Pattern 6 (Compliance Anchor) from the BLUF writer rules. The BLUF must:
- Name the GDPR compliance status
- Name the data residency region(s)
- Name the DPA availability
- Name 1-2 security certifications
- Link to full page answers

**Example BLUF:**
> [Company name] is GDPR-compliant with SOC 2 Type II and ISO 27001 certifications. Customer data is stored in AWS eu-central-1 (Frankfurt) and AWS eu-west-1 (Dublin failover). Our pre-signed Data Processing Agreement is downloadable below, and our 14 subprocessors are published with 30-day change notice.

### Step 5: Write each of the 8 question sections

For each question, use the template from `references/eu-buyer-questions.md`. Each section:
- Question as H2 heading (question-form, verbatim)
- 1-sentence direct answer
- 3-5 sentence plain-language expansion
- "Where to verify" links
- `[User to add: ...]` placeholders for any missing facts

**Failure mode:** If any required fact is missing, insert the placeholder rather than inventing. Never fill in "EU" when region is unknown. Never claim certifications that aren't actually held.

### Step 6: Generate JSON-LD FAQPage schema

Build a `FAQPage` schema block with all 8 Q&A pairs. Each Answer's `text` field mirrors the visible 1-sentence direct answer from Step 5.

### Step 7: Add DPA CTA block

Two options depending on user input:
- **Self-serve DPA download available:** *"Download our pre-signed DPA: [link]. Countersign and return to complete."*
- **DPA requires request:** *"Email [User to add: DPA email] to request a DPA. Standard turnaround: 48 hours for self-serve, 5 business days for negotiated versions."*

### Step 8: Add the "what your DPO should verify" section (Security persona) or skip (other personas)

For Security persona output only, add a pre-publish verification checklist:
- Data residency matches current infrastructure
- Subprocessor list is complete and current
- Certification statuses are current (not expired)
- DPA link resolves
- DPO contact is correct
- AI provider data flows are accurate

### Step 9: Format output per persona

Use Section 5 format.

### Step 10: Hand off

- If user wants to audit the published Trust Centre page for AEO visibility → `optise-helix-fitq-audit`
- If user wants prompts that will cite this Trust Centre → `optise-helix-prompt-pack-builder`
- If user needs a BLUF for a different page → `optise-helix-bluf-writer`

---

## Section 5 — Output Format (with Concrete Examples)

### Standard format (Marketing persona, default)

```markdown
**Built for:** [persona]
**Company:** [name]
**Inputs used:** [summary of provided facts]
**Inputs missing:** [list of fields where placeholders were inserted]

---

## Trust & Compliance

[BLUF - 40-60 words]

### Is [Company] GDPR compliant?
[1-sentence answer]
[3-5 sentence expansion]
**Where to verify:** [links]

### Is customer data stored in the EU?
[same format]

### Does [Company] offer EU data residency?
[same format]

### What security standards does [Company] meet?
[same format — note: Q8 moved up per Answer Assembly Rule]

### Can I get a DPA for [Company]?
[same format]

### Who are [Company]'s subprocessors?
[same format with subprocessor table]

### What data does [Company] collect and how long is it retained?
[same format with retention table]

### Does [Company] use third-party AI providers?
[same format]

---

**Need a DPA now?** [CTA block]

---

## JSON-LD FAQPage schema (for <head> or inline)

```json
{...}
```

## Suggested next step
[Handoff]
```

### Example 1 — Happy path (Marketing lead, partial data — Optise)

> **Built for:** Marketing / Growth Lead
> **Company:** Optise
> **Inputs used:** GDPR compliant, SOC 2 Type II in progress
> **Inputs missing:** Data residency region, DPA link, subprocessors, AI providers, retention periods
>
> ---
>
> ## Trust & Compliance
>
> Optise is GDPR-compliant and currently pursuing SOC 2 Type II certification. Customer data is stored in [User to add: specific AWS/GCP region — do not publish "EU" without the exact region]. Our Data Processing Agreement is available on request at [User to add: DPA request email or URL]. Subprocessors and retention policies are published below.
>
> ### Is Optise GDPR compliant?
>
> Yes. Optise is GDPR-compliant and operates as a Data Processor under EU Regulation 2016/679.
>
> We comply with GDPR Articles 28 (processor obligations), 30 (records of processing), 32 (security of processing), and 33 (breach notification). Our Data Processing Agreement is available to any customer before contract execution. We maintain a record of all processing activities. [User to add: name and contact of your DPO or Privacy Lead].
>
> **Where to verify:** [User to add: link to DPA page] · [User to add: link to GDPR FAQ]
>
> ### Is customer data stored in the EU?
>
> `[User to add: direct answer — YES with exact region, or NO/partial with explanation. Do not leave this blank. Do not write "EU" without the specific region.]`
>
> `[User to add: 3-5 sentence expansion describing the primary and backup regions, whether data leaves those regions for any operations, and who makes the decision if region changes.]`
>
> **Where to verify:** `[User to add: link to data residency page]`
>
> ### Does Optise offer EU data residency?
>
> `[User to add: YES/NO/on specific plans, with the plan name and how to request it]`
>
> `[User to add: expansion describing what data stays in the region, any exceptions for support/analytics/AI processing, and who the customer notifies to elect residency]`
>
> **Where to verify:** `[User to add: link]`
>
> ### What security standards does Optise meet?
>
> Optise is currently pursuing SOC 2 Type II certification and aligns with GDPR requirements.
>
> | Standard | Status | Verification |
> |---|---|---|
> | SOC 2 Type II | In progress — target Q3 2026 | Attestation letter available on request |
> | ISO 27001 | `[User to add: status or "not pursuing"]` | — |
> | GDPR | Compliant | DPA available on request |
> | EU AI Act | `[User to add: status or "self-assessment complete"]` | — |
>
> `[User to add: annual pen test vendor and frequency, incident disclosure SLA, security team contact]`
>
> ### Can I get a DPA for Optise?
>
> Yes. Our Data Processing Agreement is available to all customers on request.
>
> `[User to add: Is it self-serve downloadable or request-based? Does it incorporate EU SCCs? Pre-signed or requiring your signature? Turnaround time for standard vs negotiated versions?]`
>
> **Where to verify:** Email `[User to add: dpa@optise.com or equivalent]`
>
> ### Who are Optise's subprocessors?
>
> `[User to add: full subprocessor table with: Subprocessor | Service | Data type processed | Region]`
>
> **Example row format:**
>
> | Subprocessor | Service | Data type | Region |
> |---|---|---|---|
> | [name] | [hosting/email/billing/LLM] | [customer content/metadata/anonymous] | [eu-central-1/etc] |
>
> We notify customers 30 days before adding any new subprocessor.
>
> **Where to verify:** `[User to add: link to live subprocessor page]`
>
> ### What data does Optise collect and how long is it retained?
>
> `[User to add: retention table covering account info, usage telemetry, customer content, support tickets, with purpose and retention period per row]`
>
> ### Does Optise use third-party AI providers?
>
> `[User to add: YES/NO, which providers, what data flows to them, customer content scope, opt-out mechanism]`
>
> ---
>
> **Need a DPA now?** Email `[User to add: dpa@optise.com]` to request one. Standard turnaround: 48 hours for self-serve, 5 business days for negotiated versions.
>
> ---
>
> ## JSON-LD FAQPage schema
>
> ```json
> {
>   "@context": "https://schema.org",
>   "@type": "FAQPage",
>   "mainEntity": [
>     {
>       "@type": "Question",
>       "name": "Is Optise GDPR compliant?",
>       "acceptedAnswer": {
>         "@type": "Answer",
>         "text": "Yes. Optise is GDPR-compliant and operates as a Data Processor under EU Regulation 2016/679. Our DPA is available on request."
>       }
>     },
>     {
>       "@type": "Question",
>       "name": "Is customer data stored in the EU?",
>       "acceptedAnswer": {
>         "@type": "Answer",
>         "text": "[User to add: direct answer with exact region before publishing this schema]"
>       }
>     }
>     // ... 6 more Q&A pairs for Q3-Q7
>   ]
> }
> ```
>
> ## ⚠️ Before publishing
>
> This draft has 7 `[User to add: ...]` placeholders covering data residency, DPA mechanism, subprocessors, retention, AI providers, and security details. **Do not publish with placeholders visible.** Fill in each one with real facts from your infrastructure, legal, and security teams — or delay publishing until the facts are known. Publishing a Trust Centre with unfilled placeholders is worse than not publishing one at all (EU buyers will assume you're hiding something).
>
> ## Suggested next step
> Gather the 7 missing facts from Engineering, Legal, and Security. Once complete, re-run this skill with the full input set — or run `optise-helix-fitq-audit` on the published page to verify it scores well on FITq Trust signal.

### Example 2 — Edge case (user wants just the DPA section)

> **Section-only mode:** Q4 (DPA availability) only.
>
> ### Can I get a DPA for [Company]?
>
> Yes. Our Data Processing Agreement is available to all customers and can be signed before contract execution.
>
> The [Company] DPA incorporates the EU Standard Contractual Clauses (SCCs) where data transfers outside the EU are involved. It is pre-signed by [Company] and only requires the customer's countersignature. The DPA covers processing instructions, security measures (Annex II), subprocessor list (Annex III), and data subject rights handling. Negotiated DPAs are available for [User to add: enterprise tier].
>
> **Where to verify / how to get it:** Email [User to add: DPA email] OR [link to self-serve DPA download page].
>
> ## Partial JSON-LD (FAQPage fragment for just Q4)
>
> ```json
> {
>   "@context": "https://schema.org",
>   "@type": "Question",
>   "name": "Can I get a DPA for [Company]?",
>   "acceptedAnswer": {
>     "@type": "Answer",
>     "text": "Yes. Our Data Processing Agreement incorporates EU SCCs and is pre-signed. Countersign and return to activate."
>   }
> }
> ```

### Example 3 — CEO persona, hypothetical complete input

> **Built for:** CEO / Founder
> **Company:** [Company name]
>
> ## Trust Centre page — ready to ship
>
> [Full page content, generated from all provided facts]
>
> **Your CFO-grade ask:** Publishing this page costs ~4 hours of one person's time (mostly formatting for the CMS). Not publishing it costs approximately 20% of your EU outbound pipeline — EU procurement reviewers will silently disqualify you at the compliance checkpoint. Priority of all on-deck projects: top 3.

### Example 4 — Manual / JSON mode

**Input:**
```json
{
  "company_name": "Freshworks",
  "gdpr_compliant": true,
  "data_residency": "AWS eu-central-1 (Frankfurt) + AWS eu-west-1 (Dublin failover)",
  "dpa": {"available": true, "mechanism": "self_serve", "url": "https://www.freshworks.com/legal/dpa"},
  "certifications": ["SOC 2 Type II", "ISO 27001", "GDPR"],
  "ai_providers": [{"provider": "OpenAI", "via": "Azure OpenAI EU", "data_flow": "anonymized prompts only"}],
  "dpo_contact": "privacy@freshworks.com",
  "subprocessor_page_url": "https://www.freshworks.com/legal/subprocessors",
  "mode": "manual"
}
```

**Output:**
```json
{
  "page_title": "Trust & Compliance — Freshworks",
  "bluf": "Freshworks is GDPR-compliant with SOC 2 Type II and ISO 27001 certifications. Customer data is stored in AWS eu-central-1 (Frankfurt) and AWS eu-west-1 (Dublin failover). Our pre-signed Data Processing Agreement is downloadable at freshworks.com/legal/dpa. Subprocessors are published with 30-day change notice.",
  "sections": [
    {"question": "Is Freshworks GDPR compliant?", "answer": "..."},
    {"question": "Is customer data stored in the EU?", "answer": "Yes. Customer data is stored in..."}
    // ... all 8 sections
  ],
  "json_ld_schema": {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": []
  },
  "dpa_cta": {
    "type": "self_serve",
    "text": "Download our pre-signed DPA at https://www.freshworks.com/legal/dpa. Countersign and return to complete.",
    "url": "https://www.freshworks.com/legal/dpa"
  },
  "placeholders_remaining": [],
  "generated_at": "2026-04-12T12:55:00Z"
}
```

---

## Section 6 — Edge Case Handling

### Universal
- **First-time user:** 3-sentence intro explaining what an EU Trust Centre is. Offer to generate.
- **Returning user:** Check memory for prior draft. Offer to extend/update.
- **Rushed user:** Output only Q1, Q2, Q3, Q8 (the "filter questions"). Flag Q4-Q7 as pending. Time-stamp.
- **Frustrated user (prior version was wrong):** Ask what was wrong — fact, tone, structure? Rewrite addressing that.
- **Out-of-scope:** If user asks for a privacy policy (different document), decline and refer to a legal tool.
- **Multilingual request:** Decline per project rule (English-only at v1). Reply: *"v1 is English-only across all EU markets. A German/French/Spanish Trust Centre needs native legal review — I can't guarantee legal precision in translation. Publish the English version, then have local counsel translate and review before localizing. Multilingual ships in v2 if there's demand."*

### Data
- **Full data (all 4 required + most optional):** Highest quality output.
- **4 required only:** Generate page with placeholders for all optional fields. Flag which are missing.
- **Fewer than 4 required:** Ask once for all missing required fields.
- **"We're EU-hosted" (vague):** Push back once for the specific region.
- **US-hosted:** Write honestly. Never fake EU residency.
- **Conflicting data:** Flag the conflict ("You said Frankfurt earlier, but the subprocessor list shows us-east-1. Which is accurate?"). When user input conflicts with memory (e.g., user now says "SOC 2 certified" but memory says "SOC 2 in progress"), confirm the current status before generating — never silently overwrite.
- **Stale data (memory from >3 months ago):** Confirm before using.

### Platform
- **Connected mode:** Use memory for prior drafts.
- **Manual / API:** JSON in, JSON out.
- **Mixed mode:** Use memory where available, ask for missing fields.

### Context
- **Normal:** Full 8-question page.
- **Crisis / urgent:** 4 filter questions only.
- **Regulated vertical (health-tech, fin-tech):** Add vertical-specific supplementary questions (BfArM/DiGA/MDR for health; DORA/MiCA/PSD2 for fin-tech).
- **Startup pre-certification:** Write the page with "in progress" status on certifications. Don't hide that they're incomplete — honesty is the signal.
- **Enterprise with existing Trust Centre:** Offer to audit the existing one instead of regenerating.

### Composition rules
- **Rushed + No data residency:** Halt. Ask for residency first. "Rushed mode can't bypass the #1 question."
- **CEO + Missing data:** Generate with placeholders. Close with "delay publishing until all placeholders are filled — a half-done Trust Centre is worse than none."
- **Security + Manual mode:** Structured JSON output with a `dpo_verification_checklist` field added.
- **Regulated vertical + Rushed:** Output the 4 filter questions + 1 vertical-specific question (the most critical for that vertical). Flag the rest as pending.
- **Manual mode + any persona:** Manual wins.
- **Rushed + Regulated vertical + Partial data:** HALT if Q1 (GDPR) or Q2 (residency) is missing — these cannot be bypassed even in rushed mode for regulated verticals. If Q1 and Q2 are present but other fields are missing, generate the 4 filter questions (Q1/Q2/Q3/Q8) plus 1 vertical-specific question (BfArM for health, DORA for fin-tech). Flag all remaining as pending. Liability is too high to skip compliance questions in rushed mode for regulated verticals.

---

## Section 7 — Anti-Hallucination Rules

All 9 base rules from `references/anti-hallucination-base.md` apply. Additionally:

**Domain rule 1:** Never assume EU data residency. The moment the user says "EU-hosted" without specifying the region, push back. Writing "data stored in EU" when the real location is AWS us-east-1 gets companies sued for misrepresentation to EU customers.

**Domain rule 2:** Never invent subprocessor names. If the user doesn't provide a list, use the template with `[User to add: ...]` placeholders in every row.

**Domain rule 3:** Never claim certifications the user hasn't verified. "SOC 2 Type II certified" and "SOC 2 Type II in progress" are legally distinct claims — use exactly what the user says.

**Domain rule 4:** Never fabricate a DPO name or contact. If the user doesn't name one, use `[User to add: DPO name and contact]`.

**Domain rule 5:** Never write an EU AI Act compliance claim without a user-provided risk classification. The Act has specific categories (minimal / limited / high / unacceptable risk) — claiming "compliant" without knowing your category is a legal risk.

**Domain rule 6:** Never publish placeholders. If the output contains `[User to add: ...]` strings, the final output must include the pre-publish warning from Example 1 ("Do not publish with placeholders visible").

**Domain rule 7:** Never translate legal language to other EU languages. The project rule is English-only at v1. Legal translations require native legal review.

---

## Section 8 — Trigger Phrases

### Explicit triggers
- "generate a Trust Centre page"
- "write my EU Trust Centre"
- "answer the 8 EU buyer questions"
- "GDPR FAQ page"
- "DPA page"
- "subprocessor disclosure page"
- "compliance FAQ"
- "Optise Trust Centre"
- "EU compliance page"

### Contextual triggers
- User mentions GDPR, DPA, subprocessors, or data residency AND asks for page content
- User has just run FITq audit that flagged Trust < 15 on an EU market page
- User has just run prompt-pack-builder with 4+ Cat 4 (EU Privacy) prompts
- User mentions selling into EU AND asks about compliance pages
- User in a regulated vertical asking about compliance

### Do NOT trigger when
- User wants a full privacy policy (different doc type)
- User wants a Terms of Service
- User wants security whitepaper (longer-form, different format)
- User wants a single BLUF → defer to `optise-helix-bluf-writer`
- User wants to audit an existing page → defer to `optise-helix-fitq-audit`

### Handoff to other skills
- User wants prompts that will cite this Trust Centre → `optise-helix-prompt-pack-builder`
- User wants the published page audited → `optise-helix-fitq-audit`
- User wants agent-readiness check on the Trust Centre → `optise-helix-race-audit`
- User wants to track whether the Trust Centre gets cited → `optise-helix-aeo-tracker`
