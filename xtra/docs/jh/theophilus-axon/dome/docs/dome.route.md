# `dome.route.py` – DOME Routing Core

## Overview
This module acts as the central integrator for memory contextualization by sequentially routing memory blocks through the **temporal anchor**, **spatial context**, and **3D grid mapper** subsystems. It mimics the hippocampal-cortical memory loop found in biological systems, ensuring each memory has spatial-temporal context.

## File Path
`DOME/dome.route.py`

## Function: `process_memory_block(memory_block, location="sensor-A")`
This function orchestrates the following in order:

1. **Temporal Anchor Injection**:
   - Adds current UTC timestamp via `add_temporal_anchor`
   - Fulfills the Delay Pillar of UDC

2. **Spatial Context Attachment**:
   - Adds spatial or sensor-based location context (default: `sensor-A`)
   - Fulfills the Memory Traceability Pillar

3. **3D Grid Mapping**:
   - Assigns deterministic 3D coordinates based on memory tick via `map_to_3d_grid`
   - Simulates place-cell trace memory

## UDC Compliance
| Pillar                        | Compliant | Description |
|------------------------------|-----------|-------------|
| Delay Anchoring              | ✅        | Timestamp injection from temporal anchor |
| Recursive Symbol Formation   | ✅        | Grid-space mapping as recursive anchor |
| Self-Mirroring Memory        | ✅        | Reentrant memory tagging for later recall |
| Ethical Traceability         | ✅        | Spatial labeling allows audit of memory origin |

## Neuroscientific Foundation
- **Hippocampal Loop Theory** – Routing across spatial-temporal encoding systems mirrors rodent experiments (Eichenbaum, 2004).
- **Grid & Place Cells** – Coordinate anchoring aligned with O’Keefe & Moser’s foundational work (2005 Nobel).
- **Symbolic Location Awareness** – Semantic labeling of experience location reflects cognitive maps in primates.

## Sample Output
```json
{
  "tick": 1024,
  "timestamp": "2025-06-05T18:20:43Z",
  "location": "sensor-A",
  "grid_position": {"x": 24, "y": 10, "z": 0}
}
```

## Citation
- O'Keefe, J. & Moser, E. I. (2005). The Hippocampus as a Cognitive Map.
- Eichenbaum, H. (2004). Hippocampus and Memory Consolidation.
- Buzsáki, G. (2005). Theta rhythm of navigation.

## License
Part of the Theophilus-Axon system, created by Joshua B. Hinkson. Do not replicate without ethical compliance or permission.