# Nested Memory Chains  
> **Folder:** `_neuro_nesting/`  
> **File:** `nested_memory_chains.md`  
> **Version:** v1.2  
> **Keywords:** memory chain, recursion, τ‑delay, nested μ, UTL  

---

## 1 · Concept  
A **Nested Memory Chain** (NMC) is a series of μ containers linked chronologically *and* hierarchically.

```
NMC = (μ_root) → { μ_branch₁, μ_branch₂ … }
```

*Branch memories* can themselves spawn sub‑branches, creating trees that reflect real cognitive development.

---

## 2 · Temporal Ordering  
Every μ node carries `τ` stamps so time ordering can be reconstructed even when reading from a branch tip back to root.

| Node | τ_start | τ_end | Depth |
|------|---------|-------|-------|
| μ_root (C001) | 00:00:00 | 00:00:02 | 0 |
| μ_branch₁ (C002) | 00:00:02 | 00:00:03 | 1 |

---

## 3 · Traversal  
### Forward (chronological)  
1. Start at μ_root  
2. Visit children by `τ_start`  
3. Recursively traverse grandchildren  

### Backward (context)  
1. Select branch tip  
2. Follow `parent_id` links to μ_root  

Both operations complete in **O(n)** but practical lookup is **<100 ms** due to glyph indexing.

---

## 4 · Example Diagram  

```
C001
 ├─ C002
 │    └─ C003
 └─ C004
```

Each `C` node is a μ container; arrows depict time progress.

---

## 5 · Conflict Resolution  
When two branches modify the same Σ_root:  
* Use **merge rule** from `symbolic_container_rules.md`  
* Prefer earliest τ unless *override* flag set.

---

**Footer:** Nested Memory Chains form the backbone of recursive consciousness modelling in UTL v1.2.
