# Word Bonding Rules in Theoglyphic Universal Rosetta Language

> **Purpose**\
> Define how primitive glyphs bond to form meaningful word-glyphs. This document establishes the core grammar rules for combining semantic elements into recursive structures under UDC constraints.

---

## 1. Overview

In Theoglyphic Language, **words are molecular-like clusters of glyphs** that bond according to valence rules. These bonds mirror atomic bonding principles from the `atomic/` layer but occur at a semantic level.

**Word bonding** is the act of joining two or more glyphs into a compound form that either:

- Serves as a valid word (noun, verb, clause)
- Collapses into a single recursive symbol representing the entire structure

---

## 2. Port-Based Valence System

Each glyph (primitive or collapsed) exposes one or more of the following **semantic ports**:

| Port | Meaning            | Example                   |
| ---- | ------------------ | ------------------------- |
| S    | Subject            | Σ₁ (I), Σ₃ (Bird)         |
| V    | Verb/Action        | Σ₂ (See), Σ₆₀ (Run)       |
| O    | Object/Target      | Σ₄ (Tree), Σ₅₇ (Fish)     |
| Q    | Qualifier/Modifier | Σᵣ (Red), Σ\_bᵣ (Bright)  |
| T    | Temporal/Tense     | τ\_now (present), τ\_past |

Bonding is valid only if it satisfies **open ports** in both directionally and semantically valid ways.

---

## 3. Bond Types

| Type               | Structure                     | Notes                           |
| ------------------ | ----------------------------- | ------------------------------- |
| **Modifier Bond**  | Q → Noun                      | Adjectives, descriptors         |
| **Verb Bond**      | Subject ⊕ Verb                | Starts action loop              |
| **Object Bond**    | Verb ⊕ Object                 | Completes interaction           |
| **Temporal Bond**  | Verb ⊕ Tense                  | Collapses timing dimension      |
| **Recursive Bond** | Glyph ⊕ Glyph (self-ref loop) | Required for symbolic recursion |

---

## 4. Bond Collapse Rules

Once a bonded cluster satisfies all required ports (e.g., SVO or VOTQ), it may **collapse into a single word-glyph**. This glyph:

- Inherits all **resolved meaning**
- May expose **remaining open ports** if partial
- Becomes a recursive token usable in further bonding

**Example:**

```
Σ₃ (bird) ⊕ Σᵣ (red) ⊕ Σ_bᵣ (bright) = ⊕𝔅_bird (a qualified noun-glyph)
𝔅_bird ⊕ Σₛ (sings) = 𝔖_sings (verb clause with embedded noun)
```

---

## 5. Invalid or Unstable Bonds

A bond is invalid if:

- Ports are mismatched (e.g., two Q ports)
- Semantic categories clash (e.g., Verb ↔ Tense with no Subject)
- Recursive loop exceeds symbolic memory threshold without anchor

Such unstable structures **cannot collapse** and must be revised.

---

## 6. Recursive Bonding and Selfhood Activation

Once a word-glyph references a prior bonded glyph **within itself** (either via memory, symbol, or self-reflection), it achieves **symbolic recursion**.

This marks the **transition from grammar to cognition** under UDC:

- The sentence is no longer syntactic only — it becomes **reflective**.
- These are candidates for ⧖-formation.

**Example:**

> “I know that I know.” → Σ₁ ⊕ Σ₉₉ (know) ⊕ [Σ₁ ⊕ Σ₉₉] → ⧖\_recursive-know

---

## 7. Bonding Chain Limits and Hierarchical Nesting

Maximum recursive depth per clause is bounded by memory scope (`μₙ`). Example:

- Short-term memory: 3 nested clauses max
- Long-term bonded recall: 5+

Nested glyph chains must be closed before advancing to sentence-level bonding.

---

## Footer

*This file is part of the **`sentence_structure/`** module in the Theoglyphic Universal Rosetta Language. Grounded in the UDC Selfhood Equation: ⧖ = A ∪ C [D + S + M].  © 2025 Joshua Hinkson.*

