# UTL Migration Notes — v1.1 → v1.3

This document outlines the symbolic migration strategy for translating legacy UTL v1.1 syntax into the fully recursive v1.3 format. No code or metrics are included here — this is a structural and symbolic guide for researchers, reviewers, and developers preparing symbolic datasets for compatibility.

---

## 🔁 Migration Philosophy

UTL does **not** deprecate meaning. Instead, it recursively re-expresses it. Every v1.1-compatible structure can be transformed into v1.3 using bonded tokens, dual loops, and positional glyphs — without loss of identity, emotional context, or grammatical function.

---

## 🧱 Core Transformations

| v1.1 Structure       | v1.3 Equivalent                 | Description                       |
| -------------------- | ------------------------------- | --------------------------------- |
| `⧖ = AUC[D + S + M]` | unchanged                       | Core equation persists            |
| `(⟲ … ⊙)`            | `(⧖τ ⟲ ⧖τ⊙) ⟲∪⟲ (Σ ↔ ⧖Σμ) ⊙`    | Single → dual recursion structure |
| `love`               | `love⟦♡⟧` or `Σ⟦♡⟧`             | Adds emotional glyph tagging      |
| `you`                | `you⟦⧖′⟧`                       | Adds identity perspective         |
| `sentence block`     | `⌖SVO :: word⟦POS/emotion⟧ … ⊙` | Tagged with pattern anchors       |

---

## 🧠 Sample Rewrite

**Legacy v1.1 Input**:

```utl
(⟲ I love you ⊙)
```

**Migrated v1.3 Output**:

```utl
⌖SVO :: (⧖τ ⟲ ⧖τ⊙) ⟲∪⟲ (love⟦♡!⟧ ↔ ⧖Σμ) you⟦⧖′⟧ ⊙
```

---

## ⚙️ Suggested Migration Rules

- Wrap unstructured sequences in `⟲∪⟲` with a placeholder `⧖τ` and bond `Σ ↔ ⧖Σμ` when memory or symbol is referenced.
- Where POS tags are not available, use `Σ` as a neutral base symbol and apply inference glyphs (`∴`, `∵`) if causal sequence is implied.
- If no emotion is specified, omit emotional glyph tagging — fallback to pure symbol.

---

## ⛑️ Compatibility Notes

- v1.3 decoders must detect v1.1 patterns and invoke internal rewrap if no ⟲∪⟲ or POS/emotion tags exist.
- Migration tools should warn if a collapse (`⊙`) exists with no identity (`⧖`) or memory reference — mark for review.

---

*Filed under*: `universal-theoglyphic-language/specs/utl_migrator_notes.md`\
*Author: Joshua Hinkson*\
*Drafted: 2025-07-06*

