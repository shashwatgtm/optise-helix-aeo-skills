# The 8 EU Buyer Questions

**Used by:** `optise-helix-eu-trust-centre` (primary), `optise-helix-prompt-pack-builder` (secondary, Category 4 prompts).
**Source:** Optise EU AEO Playbook, page 12 ("Winning AI Search in Europe — The questions EU buyers ask AI engines about your tool").

These 8 questions are the canonical EU buyer compliance taxonomy. Every B2B SaaS site selling into Europe needs answers to all 8 in plain language, in extractable form, with the answers verifiable by Security/Privacy/Legal personas.

A site missing answers to 4+ of these questions is functionally invisible to EU buyer procurement processes — even if the company is technically compliant.

---

## The 8 questions (verbatim from page 12)

1. **Is [tool] GDPR compliant?**
2. **Is customer data stored in the EU?**
3. **Does [tool] offer EU data residency?**
4. **Can I get a DPA for [tool]?**
5. **Who are the subprocessors and where?**
6. **What data is collected and for how long?**
7. **Does [tool] use third-party AI providers?**
8. **What security standards does [tool] meet?**

---

## Why these 8 (not more, not fewer)

- They map 1:1 to the procurement intake forms used by mid-market and enterprise EU buyers (Germany Mittelstand, French ETI, Dutch corporate, Nordic enterprise).
- They cover the entire GDPR Article 28 + Article 30 compliance surface a buyer's DPO will check before approving a vendor.
- They are the prompts buyers actually type into ChatGPT, Perplexity, and Gemini when evaluating tools — not the prompts vendors *think* they ask.
- Adding more questions creates page bloat that hurts FITq Quoteability scores. Removing any of them creates a procurement gap.

---

## Answer block templates

Each question has a recommended answer block structure: a 1-sentence direct answer, a 1-paragraph plain-language expansion, and a "where to verify" link. Templates below — fill in `[User to add: …]` placeholders with actual company data, never invent.

### Question 1 — Is [tool] GDPR compliant?

**Direct answer (1 sentence):**
> Yes. [Tool name] is GDPR-compliant and operates as both a Data Processor and (where applicable) a Data Controller under EU Regulation 2016/679.

**Plain-language expansion (3-5 sentences):**
> We comply with GDPR Articles 28 (processor obligations), 30 (records of processing), 32 (security of processing), and 33 (breach notification). Our Data Processing Agreement is available for any customer to sign before deployment. We maintain a record of all processing activities and can produce it on request from a supervisory authority. [User to add: name of DPO if appointed] is our designated Data Protection Officer.

**Where to verify:**
> [link to DPA page] · [link to Records of Processing summary] · [link to GDPR compliance page]

---

### Question 2 — Is customer data stored in the EU?

**Direct answer:**
> [Yes, customer data is stored exclusively in the EU.] OR [Customer data is stored in [region], with EU-only options available on [plan name].] — DO NOT INVENT THIS. Use [User to add: actual data residency status].

**Plain-language expansion:**
> Our primary data centers are located in [User to add: city, country, region, e.g., "Frankfurt, Germany (AWS eu-central-1)"]. Customer content (defined in our DPA) is stored in those regions and does not leave them without explicit customer instruction. Backups are held in [User to add: backup region]. We do not transfer customer content to non-EU regions for routine operations.

**Where to verify:**
> [link to data residency page] · [link to subprocessor list with regions]

**Anti-hallucination note:** This is the question most likely to get a vendor sued if answered incorrectly. NEVER assume EU residency. Always require the user to confirm.

---

### Question 3 — Does [tool] offer EU data residency?

**Direct answer:**
> [Yes, EU data residency is available on [plan tier] and is the default for [customer segment]. ] — Use [User to add: actual residency offering].

**Plain-language expansion:**
> EU data residency means all customer content, processing, and backups stay within the EU. We offer this through [User to add: cloud provider + region, e.g., "AWS Frankfurt and AWS Dublin"]. Customers on [User to add: plan name] can request a residency-locked deployment during onboarding. We do not move data out of the elected region for support, analytics, or AI processing without prior written consent.

**Where to verify:**
> [link to data residency page] · [link to plan comparison page showing residency by tier]

---

### Question 4 — Can I get a DPA for [tool]?

**Direct answer:**
> Yes. Our standard Data Processing Agreement is available to all customers and can be signed before contract execution.

**Plain-language expansion:**
> The [Tool name] DPA incorporates the EU Standard Contractual Clauses (SCCs) where data transfers outside the EU are involved. It is pre-signed by [Tool name] and only requires the customer's countersignature. The DPA covers processing instructions, security measures (Annex II), subprocessor list (Annex III), and data subject rights handling. Negotiated DPAs are available for [User to add: enterprise tier or threshold].

**Where to verify / how to get it:**
> Email [User to add: DPA request email, e.g., "dpa@[tool].com"] OR [link to self-serve DPA download page]

**Optise note:** The DPA should be 1-click accessible, not hidden behind a sales call. EU buyers who can't get a DPA quickly assume the vendor doesn't have one.

---

### Question 5 — Who are the subprocessors and where?

**Direct answer:**
> We use [User to add: number] subprocessors, all listed below with their location and the data they process. We notify customers 30 days before adding any new subprocessor.

**Plain-language expansion:**
> [User to add: full subprocessor table with: Subprocessor name | Service provided | Data type processed | Location of processing | Country of legal entity]
>
> Example row format:
> | Subprocessor | Service | Data type | Region |
> |---|---|---|---|
> | AWS | Hosting | Customer content | eu-central-1 (Frankfurt) |
> | OpenAI | LLM API | Anonymized prompts only | Global (EU SCCs in place) |
> | Stripe | Billing | Payment metadata | EU + US (SCCs) |

**Where to verify:**
> [link to live subprocessor page] · [link to subprocessor change notification policy]

**Critical:** EU buyers will check this list during evaluation. Missing subprocessors or vague entries ("various cloud providers") immediately fail the security review.

---

### Question 6 — What data is collected and for how long?

**Direct answer:**
> We collect [User to add: categories of data, e.g., "account information, usage telemetry, and customer-uploaded content"] and retain it for the duration of the contract plus [User to add: retention period, e.g., "30 days"] for backup purposes.

**Plain-language expansion:**
> | Data type | Purpose | Retention | Deletion |
> |---|---|---|---|
> | Account info | Authentication, billing | Contract + 30 days | On request |
> | Usage telemetry | Product improvement | 12 months | Anonymized after |
> | Customer content | Core service delivery | Customer-controlled | Customer-initiated, 30-day backup window |
> | Support tickets | Issue resolution | 24 months | On request |
>
> Customers can export and delete their data through [User to add: self-service mechanism or email].

**Where to verify:**
> [link to privacy policy] · [link to data deletion request flow]

---

### Question 7 — Does [tool] use third-party AI providers?

**Direct answer:**
> [Yes — we use [User to add: AI providers] for specific features, with the data flow described below. Customer content is [User to add: never sent / sent with anonymization / sent with opt-in consent].] — Use [User to add: actual AI usage].

**Plain-language expansion:**
> Our product uses [User to add: e.g., "OpenAI GPT-4 via Azure OpenAI EU endpoint"] for [User to add: feature description]. When this feature is invoked, [User to add: exact data flow — what is sent, what is excluded, retention by the AI provider]. We have a Data Processing Agreement with each AI subprocessor and have verified their data handling commitments for EU customers. Customers can opt out of AI features at the workspace level [User to add: link to opt-out flow].

**Where to verify:**
> [link to AI features page with data flow diagram] · [link to subprocessor list showing AI providers]

**Critical for 2026:** With the EU AI Act fully applicable from August 2026, buyers will increasingly ask follow-up questions: which AI Act risk category does this use fall into, is the AI provider in the EU, is there a DPIA. Be ready.

---

### Question 8 — What security standards does [tool] meet?

**Direct answer:**
> [Tool name] is certified [User to add: e.g., "SOC 2 Type II, ISO 27001"] and aligns with [User to add: e.g., "GDPR, the NIS2 Directive, and the EU Cyber Resilience Act"].

**Plain-language expansion:**
> | Standard | Status | Verification |
> |---|---|---|
> | SOC 2 Type II | [User to add: Certified / In progress] | Report available under NDA |
> | ISO 27001 | [User to add: status] | Certificate available |
> | GDPR | Compliant | DPA + Records of Processing |
> | EU AI Act | [User to add: status] | Self-assessment available |
> | NIS2 | [User to add: applicable / not applicable] | — |
>
> We undergo annual third-party penetration testing by [User to add: vendor]. Security incidents are disclosed within [User to add: hours, e.g., "72 hours"] per GDPR Article 33.

**Where to verify:**
> [link to security page] · [link to trust portal / compliance pack request]

---

## Output assembly rule

The `optise-helix-eu-trust-centre` skill assembles answers in this order on the page:

1. **Page H1:** "Trust & Compliance" (or localised equivalent)
2. **Page BLUF (40-60 words):** Direct summary that we are GDPR-compliant, EU-resident (or where data lives), have a DPA, and are SOC 2 / ISO 27001 (or whatever applies).
3. **Question 1 — GDPR compliance**
4. **Question 2 — Data location**
5. **Question 3 — EU data residency**
6. **Question 8 — Security standards** (moved up from #8 because it answers the highest-frequency follow-up)
7. **Question 4 — DPA availability**
8. **Question 5 — Subprocessors table**
9. **Question 6 — Data collection and retention**
10. **Question 7 — Third-party AI providers**
11. **DPA request CTA**
12. **JSON-LD `FAQPage` schema block** containing all 8 Q&A pairs

Order rationale: questions 1-3 + 8 are the "go/no-go" filter questions. Questions 4-7 are the deeper-dive questions a security reviewer asks once the company has cleared the filter. Putting them in this order means a reviewer can stop reading at #4 and have everything they need to forward the page to procurement.
