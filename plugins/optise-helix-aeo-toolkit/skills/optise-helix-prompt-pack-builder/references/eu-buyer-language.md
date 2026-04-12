# EU Buyer Language Patterns

**Used by:** `optise-helix-prompt-pack-builder` (primary), `optise-helix-eu-trust-centre` (secondary).
**Source:** Optise EU AEO Playbook, multilingual consistency section + EU buyer prompt examples (Section 10, Step 1).

European B2B buyers do NOT type prompts the same way US buyers do. The differences are linguistic, regulatory, and cultural. A prompt pack that's translated word-for-word from US English will miss real local search intent.

This file gives the prompt-pack-builder the patterns to use when generating prompts for the 5 main European market clusters.

---

## DACH (Germany, Austria, Switzerland)

**Linguistic pattern:** Buyers prefer precise, compound-noun, formal-register prompts. They often include `DSGVO` (the German term for GDPR) instead of GDPR. They ask about subprocessors (Auftragsverarbeiter) and data residency more than any other European market.

**English-language variations they search:**
- `best [category] software for German companies`
- `[tool] DSGVO compliance`
- `is [tool] GDPR compliant Germany`
- `[tool] data centers in Frankfurt`
- `[tool] BDSG compliance` (Bundesdatenschutzgesetz)
- `[tool] for Mittelstand`
- `[tool] SOC 2 ISO 27001 Germany`

**German-language variations:**
- `beste [Kategorie] Software für deutsche Unternehmen`
- `[tool] DSGVO konform`
- `[tool] Auftragsverarbeitung`
- `[tool] AVV Vertrag` (Auftragsverarbeitungsvertrag = DPA)

**Trust signals German buyers look for:** ISO 27001, BSI C5 compliance, hosting in EU (preferably Germany), explicit AVV/DPA, named subprocessors.

---

## Nordics (Sweden, Norway, Denmark, Finland)

**Linguistic pattern:** Nordic buyers search in English more than other European clusters. They lead the EU in AI adoption (Denmark 42%, Finland 38%, Sweden 35% per Eurostat Dec 2025). They ask sustainability and accessibility questions more than other markets.

**English-language variations:**
- `best [category] for Nordic B2B`
- `[tool] used by Swedish companies`
- `[tool] WCAG compliance`
- `[tool] sustainability report`
- `[tool] EU data center`
- `best AI tool for Danish startups`

**Local-language variations (rare but high-intent):**
- Swedish: `bästa [kategori] för svenska företag`
- Norwegian: `beste [kategori] for norske selskaper`
- Danish: `bedste [kategori] til danske virksomheder`
- Finnish: `paras [kategoria] suomalaisille yrityksille`

**Trust signals Nordic buyers look for:** EU hosting, accessibility (WCAG 2.1 AA), sustainability disclosures, public-sector experience.

---

## France

**Linguistic pattern:** French buyers search predominantly in French. They have very specific regulatory triggers (CNIL, RGPD instead of GDPR). They are sensitive to data sovereignty and prefer hosting in France or EU.

**French-language variations:**
- `meilleur logiciel [catégorie] entreprise française`
- `[tool] conforme RGPD`
- `[tool] hébergement France`
- `[tool] CNIL`
- `[tool] souveraineté numérique`
- `[tool] alternative française à [US competitor]`

**English-language variations they also search:**
- `[tool] hosted in France`
- `[tool] French sovereignty cloud`
- `[tool] HDS certification` (Hébergeur de Données de Santé — for health data)

**Trust signals French buyers look for:** CNIL alignment, French or EU hosting, ANSSI security visa for sensitive industries, explicit "souveraineté numérique" framing.

---

## Benelux (Netherlands, Belgium, Luxembourg)

**Linguistic pattern:** Highest English-language search rate in Europe (Netherlands especially). Heavily multinational B2B markets. Buyers care about cross-border data flows because their customers span multiple jurisdictions.

**English-language variations:**
- `best [category] for Dutch B2B`
- `[tool] AVG compliance` (Dutch term for GDPR)
- `[tool] EU cross-border data transfer`
- `[tool] multinational compliance`
- `[tool] SCC implementation` (Standard Contractual Clauses)

**Dutch-language variations:**
- `beste [categorie] voor Nederlandse bedrijven`
- `[tool] AVG conform`

**Trust signals Benelux buyers look for:** SCCs, data transfer impact assessments, EU hosting, multilingual customer support.

---

## Southern Europe (Spain, Italy, Portugal)

**Linguistic pattern:** Lower AI adoption (Italy 19.9%, Spain higher) but growing fast. Local-language search dominates. Price sensitivity is higher than Northern Europe — pricing prompts score very high here.

**Spanish:**
- `mejor software de [categoría] para empresas españolas`
- `[tool] cumplimiento RGPD`
- `[tool] precio España`
- `[tool] hospedaje en Europa`

**Italian:**
- `migliore software [categoria] per aziende italiane`
- `[tool] GDPR conforme`
- `[tool] prezzo Italia`
- `[tool] hosting Europa`

**Portuguese:**
- `melhor software [categoria] para empresas portuguesas`
- `[tool] RGPD conformidade`

**Trust signals Southern European buyers look for:** Local-language support, EU pricing transparency in EUR, EU hosting, references from local market.

---

## Cross-market patterns (use for any EU prompt pack)

**Always include at least one prompt from each of these patterns regardless of target market:**

1. **The "in Europe" qualifier:** Add `in Europe` or `for European companies` to any shortlist prompt — it signals the buyer is filtering for EU compliance and EU residency.
2. **The "alternative to [US tool]" pattern:** EU buyers actively search for EU alternatives to dominant US tools. If the user has a US competitor, generate a prompt around being the EU alternative.
3. **The DPA / data residency double:** Always include both "does [tool] offer a DPA" and "where is [tool]'s data hosted" — they are different searches with different intents.
4. **The EU AI Act question:** As the EU AI Act becomes fully applicable in August 2026, prompts about "is [tool] EU AI Act compliant" are growing in volume. Include at least one.
5. **The subprocessor question:** "Who are [tool]'s subprocessors" is a uniquely European prompt — US buyers don't ask this.

---

## Regulated vertical terminology (health-tech, fin-tech, legal-tech)

When the user is in a regulated vertical, generic GDPR/DPA prompts are necessary but not sufficient. The pack must include vertical-specific compliance prompts using the exact regulatory acronyms buyers in that vertical search for.

### Health-tech (DACH primary, all EU secondary)

**DACH:**
- `[tool] BfArM zertifiziert` — Federal Institute for Drugs and Medical Devices certification
- `[tool] DiGA Verzeichnis` — Digital Health Applications directory (Germany)
- `[tool] KHZG förderfähig` — Hospital Future Act funding eligibility (Germany)
- `[tool] MDR Konformität` — Medical Device Regulation conformity
- `[tool] IVDR konform` — In Vitro Diagnostic Regulation
- `[tool] §75c SGB V` — German social code section on hospital IT security

**France:**
- `[tool] HDS certification` — Hébergeur de Données de Santé (mandatory for health data hosting in France)
- `[tool] CNIL référentiel santé` — CNIL health data reference framework
- `[tool] DMP compatible` — Dossier Médical Partagé compatibility

**EU-wide:**
- `[tool] EHDS compliant` — European Health Data Space (regulation effective 2026)
- `[tool] MDR class IIa` — Medical Device Regulation class
- `[tool] FHIR compatible` — health interoperability standard

### Fin-tech (all EU markets)

**EU-wide:**
- `[tool] DORA compliance` — Digital Operational Resilience Act (effective Jan 2025)
- `[tool] MiCA compliance` — Markets in Crypto-Assets regulation
- `[tool] PSD2 compliant` — Payment Services Directive 2
- `[tool] PSD3 ready` — Payment Services Directive 3 (in development)
- `[tool] AML5 / AML6` — Anti-Money Laundering directives
- `[tool] EBA guidelines` — European Banking Authority

**DACH:**
- `[tool] BaFin lizenz` — German financial regulator licensing
- `[tool] MaRisk konform` — Minimum Requirements for Risk Management

**France:**
- `[tool] ACPR agrément` — French banking authority approval
- `[tool] AMF visa` — French market authority

### Legal-tech / privacy-tech

**EU-wide:**
- `[tool] eIDAS qualified` — Electronic identification and trust services
- `[tool] eIDAS 2.0 ready` — for the EU Digital Identity Wallet
- `[tool] qualified electronic signature` — vs advanced vs simple
- `[tool] EU AI Act high-risk` — for tools used in legal decision-making

### Energy / utilities (Germany specifically)

- `[tool] BSI C5 testat` — German federal information security cloud catalogue (mandatory for critical infrastructure)
- `[tool] KRITIS compliance` — Critical infrastructure regulation
- `[tool] §8a BSIG` — German IT Security Act compliance

### Public sector (all EU)

- `[tool] EVB-IT konform` — German public sector IT contract framework
- `[tool] G-Cloud framework` — UK (relevant for non-EU but UK-adjacent buyers)
- `[tool] OpenPEPPOL compliant` — EU public procurement

---

## How the prompt-pack-builder uses this section

When the user's category indicates a regulated vertical (e.g., "EHR", "patient management", "trading platform", "lending", "compliance management"), the skill should:

1. Include 4-6 vertical-specific compliance prompts in addition to the standard 8 EU buyer questions
2. Score all vertical-specific compliance prompts 5/5 (these are universal disqualifiers in regulated verticals)
3. Add a callout: *"This pack is for a regulated vertical. Compliance prompts dominate. Your Trust Centre is the highest-leverage page in this pack — recommend running `optise-helix-eu-trust-centre` immediately."*

---

## Output formatting rule

When the prompt-pack-builder outputs a prompt that includes a non-English variant, present it as:

```
| Prompt | Category | Decides | Target page | Market |
|---|---|---|---|---|
| [tool] DSGVO konform | EU Privacy | 5/5 | Trust Centre | DACH (DE) |
| best [category] for Nordic B2B | Shortlist | 4/5 | Alternatives page | Nordics (EN) |
```

Always include the market column when EU language variants are present, so the user knows which prompts are for which audience.
