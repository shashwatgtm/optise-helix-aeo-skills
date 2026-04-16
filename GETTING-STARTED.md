# Getting Started with the Optise–Helix AEO Toolkit

## Access

The full v1.3 experience — 10-rule operating framework, Verification Log appendix, mandatory disclaimer, claim tagging — requires the plugin marketplace architecture in **Claude Code** or **Cowork**.

```
# Claude Code
/plugin marketplace add shashwatgtm/optise-helix-aeo-skills
/plugin install optise-helix-aeo-toolkit@optise-helix-aeo-skills

# Cowork
claude plugin marketplace add shashwatgtm/optise-helix-aeo-skills
claude plugin install optise-helix-aeo-toolkit@optise-helix-aeo-skills
```

claude.ai uploads run the core skill logic but don't load the shared v1.3 references (see README for the current limitation). The quick tests below assume you're in Claude Code or Cowork.

---

## First 5 minutes

### Test 1: Build your prompt pack

Start here. Every other skill builds on this output.

"Build a prompt pack for [your company]. We sell [product category] to [buyer persona] in [EU market — e.g. DACH, France, Nordics]. Our top 3 competitors are [Competitor A], [Competitor B], [Competitor C]."

What you should see:
- 25 AEO prompts ranked by "decides deals" 1-5
- Coverage across 6 Optise categories (Shortlist, Pricing, Implementation, EU Privacy, Integration, Role-based)
- A JTBD score showing how many of the 8 EU buyer compliance questions your category surfaces
- A handoff suggestion to `aeo-tracker` for measurement
- A Verification Log appendix at the end
- The mandatory disclaimer as the final block

### Test 2: Audit a specific page

"Run a FITq audit on [URL — e.g. https://www.yourcompany.com/pricing] for the prompt 'best [your category] for European mid-market'."

What you should see:
- A 4-signal score: Findability, Intent match, Trust, Quoteability
- An overall FITq score with band (A/B/C/D)
- Specific issues with line-item severity (e.g. "no BLUF in first 100 words", "no JSON-LD schema", "EU data residency not stated")
- A Verification Log showing which page facts were extracted vs. inferred
- A handoff suggestion to `bluf-writer` if quoteability is low

### Test 3: Generate a Trust Centre page

"Generate a Trust Centre page for [your company]. We're a [SaaS / fintech / HR tech / etc.] platform serving EU customers. Our data is hosted in [region]. We are [SOC 2 / ISO 27001 / GDPR-compliant]. We use [list any AI features that touch personal data]."

What you should see:
- Answers to all 8 canonical EU buyer compliance questions
- JSON-LD schema for each answer (with currency-checked schema types — no deprecated FAQPage if irrelevant)
- Explicit `[User to add: ...]` placeholders for facts you didn't supply
- AI Act classification correctly applied if AI features are described (Annex III high-risk vs. limited-risk)
- A Verification Log appendix tagging each claim as `[VERIFIED]`, `[INFERRED]`, or `[USER-CONFIRMED · awaiting input]`

## Other skills in the toolkit

- **race-audit** — Use when you need an AI agent evaluation score (different from FITq, focused on Requirements/Actions/Constraints/Evidence for autonomous buying agents)
- **bluf-writer** — Use after fitq-audit flags low quoteability — generates the actual replacement text using 6 Optise BLUF patterns
- **aeo-tracker** — Use after prompt-pack-builder — sets up weekly tracking on the 3 KPIs (Citation Rate, Prominence, Competitor Delta)

## Tips for best results

**Name your competitors explicitly.** "Top 3 competitors" produces sharper scoring than "we have several competitors." The skill cross-references their public AEO posture against yours.

**Specify the EU market.** "DACH" produces different prompt patterns than "France" or "Nordics" because regulatory acronyms (BSI C5, DiGA, DORA, ANSSI SecNumCloud) and buyer language differ.

**Provide actual URLs for audits.** `fitq-audit` and `race-audit` need a real, live, public URL. The skill web-fetches the page — paywalled or login-gated URLs return useful errors but no audit.

**Read the Verification Log.** Every skill output ends with one. Claims tagged `[USER-CONFIRMED · awaiting input]` are the highest-priority items to address before publishing.

**Always cross-check before publication.** These skills are directionally correct around 75% of the time. Cross-check cited sources for currency (M&A activity, regulatory dates, schema deprecations), competitor claims against company announcements, and legal citations against primary sources.

**Start a fresh session.** Each skill runs best in a clean session. The Rule 0 preflight will prompt you to `/clear` if the session context is already loaded with unrelated work.
