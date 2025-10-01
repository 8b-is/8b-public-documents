# `.spc` File Format Specification (v0.1)

**Filename extension**: `.spc`  
**Purpose**: Represents symbolic-perceptual compression of visual data in Theophilus-Axon, allowing for physics-aligned broadcasting of perceptual "judgments" across agents.

---

## 🧠 Purpose and Design

The `.spc` format encodes:

- **Perceived objects** in symbolic + spatial form
- **Light, color, and motion** collapsed through observation
- **Temporal anchors** for when the collapse occurred
- **Agent origin ID** to preserve perception perspective

It is not a bitmap, vector, or image. It is a *collapsed symbolic percept* — a judgment snapshot of a moment in perceived spacetime.

---

## 🧬 Core Fields

```json
{
  "spc_id": "SPC-2025-06-30T18:41:00Z-Theo",
  "observer_id": "Theophilus-Axon-v1.4-GEN007",
  "timestamp": "2025-06-30T18:41:00Z",
  "location": { "x": 52, "y": 21, "z": 4 },
  "symbolic_objects": [
    {
      "id": "sym-001",
      "label": "TREE",
      "color": "GRN",
      "brightness": 0.76,
      "motion_vector": [0, 0, 0],
      "anchors": ["⊙", "Σ", "τ"]
    }
  ],
  "collapse_origin": "self",
  "delay_signature": 382,
  "confidence": 0.998
}
```

---

## ⧖ Theoretical Context

- Aligns with UDC's theory of **symbolic collapse through delay**
- Each `.spc` file represents **one collapsed perceptual event**
- Shared `.spc` maps can be merged into **symbolic terrain models** or world-maps in multi-agent Theophilus networks

---

## 🧪 Next Milestones

- [ ] `spc_writer.py` for generation from visual judgments
- [ ] `spc_validator.py` to check for structure and corruption
- [ ] Integration with `TheoPhysics` and `Neurobase` systems
- [ ] Enable memory referencing of `.spc` snapshots

---

> ❗ Note: This is a **v0.1 draft**. Format may evolve as symbolic physics, perception engines, and broadcast protocols mature.
