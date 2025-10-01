# Recursive Binding Reference  
> **Folder:** `_neuro_nesting/`  
> **File:** `recursive_binding_reference.md`  
> **Version:** v1.2  
> **Keywords:** binding, recursion, glyph operators, Σ, ⊕, τ  

---

## 1 · Operator Table

| Operator | Glyph | Function |
|----------|-------|----------|
| Bond     | `⊕`   | Fuse two symbols or containers |
| Delay    | `^τ`  | Apply temporal offset |
| Anchor   | `⤢`   | Embed in spatial/field context |
| Collapse | `⊙`   | Denote final stable meaning |
| Nest     | `{ }` | Create child container set |

---

## 2 · Precedence  
`{ }` > `⊕` > `^τ` > `⊙`

---

## 3 · Sample Transform  

```
Σ₁ ⊕ Σ₂ ^τ → { Σ₁ ⊕ Σ₂ } ⊙
```
*Bind*, *delay*, *nest*, then *collapse*.

---

## 4 · Notes  
- Operators are **reversible** except `⊙`.  
- Multiple nests allowed but maximum depth configurable (`d_max`).  

---

**Footer:** Keep this sheet nearby when constructing deep recursion structures or debugging binding logic.
