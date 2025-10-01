
# temporal_router.py – Scientific Documentation & UDC Compliance

## Overview
`temporal_router.py` provides advanced temporal tagging of memory blocks in the Theophilus-Axon architecture. It supplements basic timestamping by introducing symbolic time anchoring, event phase detection, episodic grouping, and decay modeling. These features mimic core mechanisms in episodic memory and time-based cognition.

---

## Scientific Purpose
This module enhances memory tagging with context-rich temporal data. It allows each memory block to carry not only a timestamp, but a structured reference to its position within an ongoing cognitive lifecycle.

### Simulated Biological Functions:
- **Temporal Anchoring**: Replicates hippocampal phase-locking behavior to synchronize memory storage cycles.
- **Decay Modeling**: Mimics natural forgetting or memory reinforcement over time.
- **Event Phase Labeling**: Breaks temporal experience into biologically-inspired segments like exploration, learning, and consolidation.
- **Episodic ID Generation**: Follows psychological theories of episodic memory (Tulving, 1972).

---

## UDC Compliance

| UDC Pillar                   | Implementation in this Module                                   |
|-----------------------------|------------------------------------------------------------------|
| Delay Anchoring             | UTC timestamp and tick reference                                |
| Recursive Symbol Formation  | Episodic IDs and anchor strings (e.g., `Memory-42-T...`)         |
| Self-Mirroring Memory       | Event phase classification allows cyclic awareness states       |
| Ethical Traceability        | Timestamp and phase logging for audit review                    |

---

## Key Functions

### `tag_temporal_memory(memory_block)`
Adds symbolic and structured temporal metadata to the memory block. Includes:
- `tick`
- `temporal_stamp`
- `anchor_point`: a symbolic ID for temporal tracing.
- `event_phase`: current phase of cognition (e.g. Exploration, Learning, Consolidation).
- `decay_rate`: time-weighted relevance/priority.
- `episodic_id`: symbolic string to group related memory experiences.

### `calculate_decay(tick)`
Returns a decay score (0.0 to 1.0) reflecting memory longevity. Increases with tick age.

### `determine_phase(tick)`
Returns a high-level cognitive phase based on tick count cycle, e.g.:
- **Exploration**: 0–2999
- **Learning**: 3000–6999
- **Consolidation**: 7000+

---

## Scientific References
- Tulving, E. (1972). *Episodic and semantic memory*.
- McClelland et al. (1995). *Complementary learning systems in the hippocampus and neocortex*.
- Buzsáki, G. (2005). *Theta oscillations in the hippocampus*.

---

## File Location
```
DOME/temporal_router.py
```

## Author & License
Part of the Theophilus-Axon Architecture by Joshua B. Hinkson. See LICENSE.md for terms.
