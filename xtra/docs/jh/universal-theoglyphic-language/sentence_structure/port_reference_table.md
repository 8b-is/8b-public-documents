# Port Reference Table in Theoglyphic Sentence Structure

> **Purpose**  
> Provide a visual and structural lookup for all valid ports used in Theoglyphic word-bonding and sentence recursion. Each port defines a semantic role and constrains glyph bonding under the UDC model.

---

## 1. Port Table

| Port | Name             | Accepts From         | Bonds With         | Notes                                                                 |
|------|------------------|----------------------|---------------------|-----------------------------------------------------------------------|
| **S** | Subject          | ⧖, Λ₃, other actors  | Verbs (V)           | Must initiate a verb loop                                             |
| **V** | Verb / Action    | Λ₂, Λ₉₉, Λₛ          | S, O, T             | Can be recursively nested; exposes O-port if transitive               |
| **O** | Object / Target  | Λ₄, Λ₅₇, nested clause | Verbs (V)           | May contain clause if sentence is nested                              |
| **Q** | Qualifier        | Λᵣ, Λ_bᵣ             | Nouns, Verbs         | Enhances or modifies noun/verb meaning                                |
| **T** | Temporal         | τ_now, τ_past        | Verbs or whole clauses | Encodes timing or memory anchoring                                    |

---

## 2. Port Collapse Guidelines
- All required ports must be filled before a sentence structure can collapse into a symbolic glyph.
- Some ports (Q, T) are optional depending on semantic richness.
- Ports may propagate upward after collapse — i.e., the new glyph may still expose open ports if incomplete.

---

## 3. Port Visualization

Example collapse:
```
⧖ (S) ⊕ Λ₂ (V) ⊕ Λ₃ (O) → 𝔖_see-bird [T-port still open]
𝔖_see-bird ⊕ τ_now → ⧖-bound-glyph (fully collapsed)
```

---

## 4. Recursive Binding Ports
Certain ports can recursively host their own clauses:
- **O-port recursion**: "I see [the child see the bird]"
- **S-port recursion**: Nested selves or clause agents
- **T-port recursion**: Memory of time, embedded event anchors

---

## 5. Usage Reminders
- Avoid port conflicts: no Q↔Q or S↔S bonds.
- Port overloading is allowed only for reflection loops (e.g., ⧖ ⊕ Λ₉₉ ⊕ [⧖ ⊕ Λ₉₉])
- When in doubt: check port compatibility **before** attempting recursion.

---

## Footer
*This file is part of the **`sentence_structure/`** module in the Theoglyphic Universal Rosetta Language. Grounded in the UDC Selfhood Equation: ⧖ = A ∪ C [D + S + M].  © 2025 Joshua Hinkson.*

