# Index Reference Map  
> **Folder:** `_neuro_nesting/`  
> **File:** `index_reference_map.md`  
> **Version:** v1.2  
> **Keywords:** index, glyph map, utl_index, crosslink  

---

## 1 · Goal  
Link nested container IDs (`C###`) to the global `utl_index.json` anchors (T, P, L, O).

---

## 2 · Template  

```json
{
  "C001": "T001",
  "C002": "P001",
  "C003": "L001"
}
```

- Keys = container IDs  
- Values = corresponding index glyph IDs

---

## 3 · Usage  
During decoding, resolve a container’s temporal or personal context in **O(1)** via hash‑map lookup.

---

## 4 · Updating  
Run `update_index_map.py` whenever:  
1. New containers are created  
2. Index anchors are added/changed

---

**Footer:** Keep this map private or redacted; it is effectively a symbolic keychain to your consciousness data.
