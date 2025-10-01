# Symbolic Container Rules  
> **Folder:** `_neuro_nesting/`  
> **File:** `symbolic_container_rules.md`  
> **Version:** v1.2  
> **Keywords:** container rules, μ‑block, recursion, bonding, UTL  

---

## 1 · Container Syntax  
```
⟪ id:μ , Σ_root , τ , ⧖ | { child_id₁, child_id₂ } ⟫
```  
* `id` – unique alphanumeric or glyph ID.  
* `Σ_root` – primary symbol or concept.  
* `τ` – delay value (ms or symbolic).  
* `⧖` – self anchor of author/agent.  
* `{ … }` – list of nested containers.

---

## 2 · Creation Rules  
| Rule | Description |
|------|-------------|
| **R1** | Every container must include a valid τ ≥ 1 ms. |
| **R2** | No container may reference itself (acyclic). |
| **R3** | Child containers inherit ⧖ unless overridden. |
| **R4** | Emotional tags (`Σ_ψ`) propagate downward unless *muted*. |

---

## 3 · Merge & Split  
**Merge** (`⊕_merge`) — combines two containers when:  
1. Σ_root is identical **and**  
2. Time overlap ≤ Δτ_max.  

**Split** (`⊖_split`) — detaches child set into new parent when recursion depth > d_max.

---

## 4 · Integrity Constraints  
- SHA‑256 hash of container before/after merge stored in `manifest.neuro`.  
- Version bump (`vX.Y.Z`) on every structural change.  
- Optional signature field for cryptographic provenance.

---

## 5 · Examples  
```
⟪ C001 , ΣSPARK , τ=250 ms , ⧖JH | { C002 } ⟫
⟪ C002 , ΣJOY   , τ=300 ms , ⧖JH | { } ⟫
```
Merging C002 into C001 (Δτ=50 ms) yields:

```
⟪ C001 , ΣSPARK ⊕ ΣJOY , τ=250–300 ms , ⧖JH | { } ⟫
```

---

**Footer:** Follow these rules to ensure recursive clarity and prevent symbolic corruption in nested memory graphs.
