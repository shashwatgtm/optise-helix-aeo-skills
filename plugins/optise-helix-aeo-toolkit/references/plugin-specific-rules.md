# Plugin-Specific Rules — optise-helix-aeo-toolkit

**Scope:** This file applies ONLY to the six skills in the `optise-helix-aeo-toolkit` plugin (optise-helix-prompt-pack-builder, optise-helix-fitq-audit, optise-helix-race-audit, optise-helix-bluf-writer, optise-helix-eu-trust-centre, optise-helix-aeo-tracker). It is read in addition to the shared `operating-principles.md` file in this same `references/` folder, NOT instead of it.

**Read order:** Skills MUST read `operating-principles.md` (shared core) FIRST, then this file. The shared core's 7 universal rules apply to every skill in this plugin.

---

## Status: No plugin-specific rules currently defined

This plugin currently has no plugin-specific operational rules beyond the universal shared-core operating principles. All 7 rules in `operating-principles.md` apply in full. This stub file exists to maintain architectural consistency with other plugins that DO have plugin-specific rules and to provide a clear location for future additions.

**When to add plugin-specific rules to this file:**

Add a new `## Plugin Rule N` section here when:

1. A failure mode emerges that is specific to the AEO methodology (FITq scoring, RACE framework, BLUF copy generation, EU trust-centre compliance, or AEO tracker measurement) and is not adequately covered by the universal shared core
2. A skill in this plugin develops its own domain rule that should apply across multiple skills in the toolkit (e.g., a methodology-wide constraint)
3. The Optise-Helix v2 release introduces new operational requirements that go beyond the shared core

**When to add rules to the SHARED CORE instead of this file:**

Add to `operating-principles.md` (and propagate to all three plugins) when:

1. The rule applies to ANY plugin's skills, not just the AEO toolkit's
2. The rule is a universal rigor / verification / fact-check / output-quality requirement
3. The rule reflects a lesson learned that should be taught to every Claude plugin developer

**When NOT to add rules at all:**

Do NOT add rules here for:

1. Personal preferences (those belong in your global `~/.claude/CLAUDE.md`)
2. Project-specific context (those belong in the project's local `CLAUDE.md`)
3. Cargo-culted rules from other projects that don't apply to this plugin's actual content

---

## Rule format reference

When this stub gets its first real rule, follow the long-format pattern used by the other plugins (`gtm-claude-skills/references/plugin-specific-rules.md` and `b2b-sales-enablement/references/plugin-specific-rules.md`):

```
## Plugin Rule N — [Short title]

**The rule.** [One-sentence imperative statement.]

**Why this matters.** [2-4 sentences explaining the failure mode this prevents.]

**What this means in practice.** [3-5 sentences describing the operational behavior.]

**Never do this.**
- [Specific anti-pattern 1]
- [Specific anti-pattern 2]
- [...]

**Fail-closed behavior.** [What the skill does when it cannot satisfy the rule.]
```

---

**File version:** 1.0 stub (April 2026)
**Authorship:** optise-helix-aeo-toolkit plugin
**Status:** Empty stub for future expansion
**Read order:** AFTER `operating-principles.md` (shared core), BEFORE skill-specific SKILL.md body
