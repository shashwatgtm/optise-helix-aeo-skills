# Optise–Helix AEO Toolkit

**Authors:** Optise + Helix GTM Consulting
**Released:** April 17, 2026 (alongside the Optise EU AEO Playbook 2026 Edition)
**License:** Proprietary
**Version:** 1.3

A toolkit of 6 Claude Skills that helps B2B teams selling into Europe make their websites visible, citable, and evaluable to AI search engines (ChatGPT, Perplexity, Gemini, Claude) and AI agents doing buyer evaluation.

---

## How to access this toolkit

### Recommended: Claude Code or Cowork (full v1.3 functionality)

Both Claude Code and Cowork use the same plugin marketplace architecture, which loads the shared v1.3 verification framework (10 operating-principles rules, Verification Log appendix, mandatory disclaimer, claim tagging).

**In Claude Code:**

```
/plugin marketplace add shashwatgtm/optise-helix-aeo-skills
/plugin install optise-helix-aeo-toolkit@optise-helix-aeo-skills
```

**In Cowork:**

```
claude plugin marketplace add shashwatgtm/optise-helix-aeo-skills
claude plugin install optise-helix-aeo-toolkit@optise-helix-aeo-skills
```

This is the path we test, validate, and support for production use. Recommended for sophisticated marketers, GTM consultants, and knowledge workers running Cowork.

### claude.ai upload (lighter experience, current limitation)

You can also upload individual skills to claude.ai via **Settings → Skills → Upload custom skill**. The uploader expects a ZIP containing one skill folder (with SKILL.md at its root).

**Current limitation:** the v1.3 shared operating-principles and plugin-specific-rules files live at the plugin level (`plugins/optise-helix-aeo-toolkit/references/`), outside the individual skill folders. The skill's core logic runs on claude.ai, but the shared v1.3 references are structured for plugin-aware loaders (Claude Code and Cowork) rather than claude.ai's per-skill ZIP upload.

For the full v1.3 experience today, use Claude Code or Cowork. Pre-built claude.ai-optimized bundles are under consideration for a future release.

---

## What's inside

```
plugins/optise-helix-aeo-toolkit/
  skills/
    optise-helix-prompt-pack-builder/
    optise-helix-fitq-audit/
    optise-helix-race-audit/
    optise-helix-bluf-writer/
    optise-helix-eu-trust-centre/
    optise-helix-aeo-tracker/
  references/
    operating-principles.md          (10 verification rules - shared across all skills)
    plugin-specific-rules.md         (AEO-domain framework rules)
.claude-plugin/
  marketplace.json
```

## What each skill does

| Skill | Purpose | When to use it |
|---|---|---|
| **prompt-pack-builder** | Generates 25 AEO prompts across 6 Optise categories, ranked by "decides deals" 1-5 | Start here when you need to know what European B2B buyers actually ask AI engines about your category |
| **fitq-audit** | Scores a webpage on Findability, Intent match, Trust, Quoteability (FITq) for AI search citation readiness | When you need to know why ChatGPT, Perplexity, or Gemini isn't citing your page |
| **race-audit** | Scores a webpage on Requirements, Actions, Constraints, Evidence (RACE) for AI agent evaluation readiness | When you need to know if AI agents doing buyer evaluation will recommend your page |
| **bluf-writer** | Writes 40-60 word answer blocks (BLUFs) using 6 proprietary Optise patterns | When the FITq audit says "no BLUF in first 100 words" and you need the actual replacement text |
| **eu-trust-centre** | Generates Trust Centre pages answering the 8 canonical EU buyer compliance questions with JSON-LD schema | When you need a Trust Centre page or are auditing one that's missing answers |
| **aeo-tracker** | Sets up weekly AEO citation tracking using the 3-KPI Optise rubric | When you have a prompt pack and need to measure whether your AEO work is paying off |

---

## What to expect from outputs (Claude Code / Cowork)

When running through the plugin architecture, these skills are AI-assisted and **directionally correct around 75% of the time**. Every skill output ends with:

- **A mandatory disclaimer** — reminding you that outputs need verification before publication
- **A Verification Log appendix** — showing which facts were web-verified, which were inferred from public sources, and which still need your confirmation

Treat skill outputs as a structured first draft from a domain-aware analyst, not as press-ready copy. Always cross-check:

- **Cited sources** for currency (especially M&A activity, regulatory dates, schema deprecations)
- **Competitor claims** against the company's own announcements
- **Legal citations** (AI Act articles, GDPR clauses, residency claims) against primary sources
- **URLs** referenced as canonical — paths and slugs change

The Verification Log appendix tells you exactly which claims are tagged `[VERIFIED]`, `[INFERRED]`, or `[USER-CONFIRMED · awaiting input]` so review is fast.

---

## The methodology

This toolkit is built on the Optise EU AEO Playbook 2026 Edition. Key concepts:

- **FITq** — Findability, Intent match, Trust, Quoteability (the 4-signal AI search citation rubric)
- **RACE** — Requirements, Actions, Constraints, Evidence (the 4-signal AI agent evaluation rubric)
- **BLUF** — Bottom Line Up Front, the 40-60 word answer block that AI engines extract
- **The 6 prompt categories** — Shortlist, Pricing, Implementation, EU Privacy, Integration, Role-based
- **The 8 EU buyer questions** — The canonical compliance taxonomy EU procurement reviewers check
- **The 3 KPIs** — Citation Rate, Prominence, Competitor Delta (the only metrics that matter)

---

## English only at v1

All skills generate English-language output. Multilingual prompt and Trust Centre generation is deferred to a future release. The skills cover EU markets (DACH, Nordics, France, Benelux, Southern Europe) using English-language prompt patterns with local regulatory acronyms preserved where they add search value (BSI C5 testat, BfArM, DiGA, DORA stay in their original form because that is how local buyers actually type them).

---

## Anti-hallucination

Every skill is designed to never invent the user's data. When the user has not supplied a required fact (a price, a certification, a subprocessor name, a data residency region), the skill outputs an explicit `[User to add: ...]` placeholder rather than generating a plausible-looking fabrication. This is especially critical for the Trust Centre skill, where fabricating data residency claims can expose companies to legal liability under GDPR.

The 10 operating-principles rules (in `references/operating-principles.md`, loaded by Claude Code and Cowork) further enforce: source-tier discipline, schema currency checks, legal-citation accuracy, prediction discipline, and a mandatory verification order before any recommendation is made.

---

## Authorship and credit

Both Optise and Helix GTM Consulting are credited as authors of every skill in this toolkit.

- **Optise** owns the methodology IP — the FITq and RACE frameworks, the 6 prompt categories, the 8 EU buyer questions, the 3 KPI tracker rubric, the 6 BLUF patterns, the not-ideal-for templates.
- **Helix GTM Consulting** owns the consulting build order, the 30/60/90 plan, the persona detection rules, and the cross-skill chain logic.

Both authors are required to be retained in the frontmatter of every SKILL.md if these skills are forked or extended. Commercial redistribution, white-labeling, or rebranding requires written permission from both organizations — see LICENSE.

---

## Support

For methodology questions: Ómar Thor Ómarsson, CEO, Optise — omar@optise.com

For toolkit and build questions: Shashwat Ghosh, Cofounder and Fractional CMO, Helix GTM Consulting — shashwat@hyperplays.in
