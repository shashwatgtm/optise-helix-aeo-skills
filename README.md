# AEO and GEO Toolkit for B2B Websites

By Optise and Helix GTM Consulting.

Find out why ChatGPT, Perplexity, Gemini and Google AI Overviews do not cite your B2B website, and get the fixes. Six Claude skills for AI search visibility: an AEO and GEO page audit, an AI agent audit, answer blocks AI engines can quote, buyer prompt packs and weekly AI citation tracking. Extra for EU sellers: a Trust Centre page that answers the 8 questions European buyers ask.

**Try:** "Audit https://yourcompany.com/pricing for AI search. Why isn't ChatGPT citing it?"

## Worked example on a real public page

Page: https://gtmhelix.com/fractional-cmo/, the Helix GTM Consulting fractional CMO page. Fetched on 12 Nov 2026. We used our own page so that no outside company is named. The facts below were measured on that page on that date.

**1. Page audit.** Prompt: "Audit https://gtmhelix.com/fractional-cmo/ for AI search, for the prompt 'how much does a fractional CMO cost'." What the fetch measured:

- HTTP 200, text/html, 39 KB, with the content in the raw HTML and a canonical tag. Time to first byte was 1.8 seconds on this fetch.
- robots.txt allows GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot and PerplexityBot by name.
- One JSON-LD block with Organization, Person, WebPage, BreadcrumbList and FAQPage (12 questions). The page shows a byline and "Published 6 November 2026", and the schema has a matching dateModified.
- The first sentence defines a fractional CMO in 29 words, short of a 40 to 60 word answer block.
- The price is first reached at word 893 of 2,223, in the tier cards, and again in the FAQ at word 1,958. It is not in the opening.

The gaps become ranked fixes: put a short price answer near the top for the pricing prompt, and grow the opening definition into a 40 to 60 word answer block. The full run adds a score for each of the four FITq signals, the top 5 fixes and a before and after for fix 1.

**2. Answer block.** Prompt: "Write an answer block for https://gtmhelix.com/fractional-cmo/ for 'how much does a fractional CMO from Helix cost'."

- Before: the price sits in three tier cards and in an FAQ answer near the end of the page. The FAQ answer opens with "Mentor or Advisor, 6 to 10 hours a week", so lifted on its own it does not say whose price it is.
- After (the longest of the three variants at 57 words, built only from facts on the page): "A fractional CMO from Helix GTM Consulting starts from $3,100 or INR 2.49 lakh a month for Mentor or Advisor, 6 to 10 hours a week. Micro CMO, 8 to 12 hours, starts from $4,100 or INR 3.49 lakh. Fractional CMO, 15 to 20 hours, starts from $5,250 or INR 4.49 lakh. INR bills carry 18% GST."

The full run also gives the shorter variants.

---

Plugin page with install steps for Claude Code and Cowork: https://tools.gtmhelix.com/plugins/optise-helix-aeo-toolkit/

**Authors:** Optise and Helix GTM Consulting
**Released:** April 17, 2026 (alongside the Optise EU AEO Playbook 2026 Edition)
**License:** Proprietary, free to use (see LICENSE)
**Version:** 1.6 (skills and plugin manifest; the shared operating principles are v1.3)

**Designed for English-language websites.** The audits, scores and rewrites assume the page and the buyer prompts are in English.

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
| **prompt-pack-builder** | Generates 25 AEO prompts across 6 Optise categories, ranked by "decides deals" 1-5 | Start here when you need to know what B2B buyers ask AI engines about your category (prompts use European market buyer language) |
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

The toolkit is designed for English-language websites, and all skills generate English-language output. Multilingual prompt and Trust Centre generation is deferred to a future release. The skills cover EU markets (DACH, Nordics, France, Benelux, Southern Europe) using English-language prompt patterns with local regulatory acronyms preserved where they add search value (BSI C5 testat, BfArM, DiGA, DORA stay in their original form because that is how local buyers actually type them).

---

## Anti-hallucination

Every skill is designed to never invent the user's data. When the user has not supplied a required fact (a price, a certification, a subprocessor name, a data residency region), the skill outputs an explicit `[User to add: ...]` placeholder rather than generating a plausible-looking fabrication. This is especially critical for the Trust Centre skill, where fabricating data residency claims can expose companies to legal liability under GDPR.

The 10 operating-principles rules (in `references/operating-principles.md`, loaded by Claude Code and Cowork) further enforce: source-tier discipline, schema currency checks, legal-citation accuracy, prediction discipline, and a mandatory verification order before any recommendation is made.

---

## Authorship and credit

Both Optise and Helix GTM Consulting are credited as authors of every skill in this toolkit.

- **Optise** owns the methodology IP — the FITq and RACE frameworks, the 6 prompt categories, the 8 EU buyer questions, the 3 KPI tracker rubric, the 6 BLUF patterns, the not-ideal-for templates.
- **Helix GTM Consulting** owns the consulting build order, the 30/60/90 plan, the persona detection rules, and the cross-skill chain logic.

Both authors are required to be retained in the frontmatter of every SKILL.md if these skills are forked or extended.

**Licence in brief (see LICENSE):** anyone, including companies, may install and use the toolkit free of charge. Plugin directories may list and distribute it. Reselling, redistributing it inside another product, white-labelling or rebranding needs written permission from both Optise and Helix GTM Consulting. One exception: the shared operating principles file (`plugins/optise-helix-aeo-toolkit/references/operating-principles.md`) is released under the MIT License.

---

## Privacy

This plugin sends no data to Optise or Helix GTM Consulting and runs no server. The skills run inside Claude. When fitq-audit and race-audit fetch a page, Claude uses its own tools and the rules in each skill's `references/page-fetch-method.md`: it contacts only the web address you give it, identifies itself honestly as this toolkit where the tool lets it set a user agent, reads at most 5 MB, and stores nothing. What you type into Claude is handled under your own Claude account terms.

## Security

To report a security problem, see SECURITY.md.

---

## Support

For methodology questions: Ómar Thor Ómarsson, CEO, Optise (omar@optise.com)

For toolkit and build questions: Shashwat Ghosh, Co-Founder and Fractional CMO, Helix GTM Consulting (shashwat@gtmhelix.com)
