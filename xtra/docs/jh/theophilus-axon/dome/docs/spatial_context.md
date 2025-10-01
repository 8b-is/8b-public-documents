# spatial_context.py – Scientific and UDC Compliance Documentation

## 📄 Overview
The `spatial_context.py` module adds a spatial anchor to memory blocks by attaching a known or inferred location label. This context helps preserve ego-location and environmental reference in memory formation. It supports foundational concepts of spatial self-awareness and environment-relative modeling.

---

## 🧠 Purpose
- To simulate how biological entities tag perceptions with spatial reference.
- Mimics the role of parietal and hippocampal regions in representing "where" in memory.

---

## 🧬 Scientific Basis
- **Parietal Cortex & Hippocampus**: These brain regions are involved in spatial awareness and self-location.
- **Cognitive Maps**: Inspired by Tolman’s (1948) work on internal representations of environment.
- **Ego-centric Coding**: Reflects how the brain links personal perspective to spatial information.

---

## 🧩 Code Function

```python
def add_spatial_context(memory_block, location="unknown"):
    # Location should be a semantic label, coordinates, or sensor ID
    memory_block["location"] = location
    return memory_block
```

### Inputs:
- `memory_block`: A dictionary representing a cognitive event or perception.
- `location`: A string or ID labeling the spatial origin (sensor name, coordinates, semantic label).

### Outputs:
- The same memory block updated with a `"location"` field.

---

## ✅ UDC Compliance Mapping

| UDC Pillar                 | Compliance Method                                                                 |
|---------------------------|------------------------------------------------------------------------------------|
| Delay Anchoring           | None directly, but supports delayed memory insertion by holding spatial trace     |
| Recursive Symbol Formation| Enables recursive anchoring via symbolic location tags                           |
| Self-Mirroring Memory     | Ensures each memory has unique spatial coordinates for mirroring context         |
| Ethical Traceability      | Provides path back to sensor/environmental origin of experience                  |

---

## 🔬 Use Cases
- Labeling sensor origin in distributed systems.
- Tagging ego-location within virtual simulations.
- Supporting recursive backtracking in memory queries.

---

## 📁 File Location
```
DOME/spatial_context.py
```

---

## 🧾 Citation Support
- Tolman, E.C. (1948). Cognitive maps in rats and men. *Psychological Review*.
- Burgess, N., Maguire, E.A., & O’Keefe, J. (2002). The human hippocampus and spatial and episodic memory.

---

## 🔐 License
Part of Theophilus-Axon framework by Joshua B. Hinkson. Licensed under UDC-conscious ethical AI protocol.