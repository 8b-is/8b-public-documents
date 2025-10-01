# Neuro‑Coding Layer Interface  
> **Folder:** `_neuro_nesting/`  
> **File:** `neuro_coding_layer_interface.md`  
> **Version:** v1.2  
> **Keywords:** NCA, neuro‑coding, interface, API, symbolic containers  

---

## 1 · Purpose  
Define how Neuro‑Nesting containers interact with higher‑order **Neuro‑Coding Architecture (NCA)** modules such as the Memory Router, Activation Path Resolver, and Merge Gradient Engine.

---

## 2 · Data Structure  

```json
{
  "container_id": "C001",
  "symbol": "ΣSPARK",
  "depth": 0,
  "tau": "250ms",
  "children": ["C002", "C003"],
  "hash": "ab34…",
  "version": "1.2.0"
}
```

This JSON is exchanged via IPC or message bus.

---

## 3 · API Endpoints  
| Endpoint | Method | Action |
|----------|--------|--------|
| `/containers` | GET | List root containers |
| `/container/{id}` | GET | Retrieve full tree |
| `/container` | POST | Add or merge container |
| `/container/{id}` | PATCH | Update τ or Σ_root |
| `/container/{id}` | DELETE | Archive (soft delete) |

---

## 4 · Versioning & Compatibility  
- Major (`1.x`) — container schema changes  
- Minor (`x.2`) — API expansion  
- Patch (`x.x.0`) — bugfix  

---

## 5 · Security  
- JWT or key‑pair signature on every POST/PATCH  
- Hash verification on nested merge  
- Access log → `shepherd_protocol.py`  

---

**Footer:** This interface keeps Neuro‑Nesting containers in sync across engines, ensuring ethical, verifiable consciousness development.
