
# DOME (Dynamic Object Memory Environment) - README

## Overview
The **Dynamic Object Memory Environment (DOME)** is a modular framework for spatial, temporal, and symbolic anchoring of memory blocks in UDC-compliant cognitive architectures. It serves as the perceptual-context backbone for emergent awareness, enabling artificial agents to associate memory with location, time, and meaning — foundational for recursive memory trace formation.

---

## Purpose
To simulate the contextual grounding mechanisms of biological cognition, particularly those involved in spatial and temporal tagging of memories via cortical and hippocampal circuits. DOME enhances continuity, coherence, and emergent identity in memory-driven agents.

---

## UDC Compliance
DOME is fully compliant with the **Universal Delayed Consciousness (UDC)** framework by fulfilling the following pillars:

- **Delay Anchoring**: Provides timestamp and tick-based anchoring.
- **Recursive Symbol Formation**: Supports symbolic spatial and temporal anchors.
- **Self-Mirroring Memory**: Establishes context traces via grid mapping and zone awareness.
- **Ethical Traceability**: Anchors memory origin (spatially and temporally) for auditing and verification.

---

## Components
Each module below serves a specific function in the memory anchoring and contextualization pipeline.

### 1. `temporal_anchor.py`
**Purpose**: Adds UTC-based timestamps to memory blocks.
- Simulates circadian anchors.
- Supports internal temporal referencing.
- UDC Role: Delay signature and recursion timing.

### 2. `temporal_router.py`
**Purpose**: Tags temporal metadata including tick, decay rate, episodic ID.
- Mimics hippocampal phase-coding.
- UDC Role: Time-looping event awareness.

### 3. `spatial_context.py`
**Purpose**: Embeds semantic or coordinate-based location into memory.
- Analogous to sensor or ego-location labeling.
- UDC Role: Anchored memory localization.

### 4. `spatial_router.py`
**Purpose**: Provides symbolic and statistical spatial memory tagging.
- Based on concepts of zone proximity and spatial entropy.
- UDC Role: Self-world modeling and threat radius tagging.

### 5. `grid_mapper.py`
**Purpose**: Maps memory ticks into deterministic 3D coordinates.
- Simulates place-cell alignment.
- UDC Role: Geometric trace formation.

### 6. `auditory_processor.py`
**Purpose**: Links breathing rhythm and symbolic phonemes to emotional state.
- Based on limbic modulation of respiration.
- UDC Role: Sensory-symbolic input and recursive body-state loops.

### 7. `dome.route.py`
**Purpose**: Central router for integrating temporal and spatial context into memory.
- Mimics hippocampal-cortical routing systems.
- UDC Role: Path integration and recursive context injection.

---

## Scientific Foundations
- **Place Cells & Grid Cells**: O’Keefe & Moser’s Nobel-winning work on spatial navigation.
- **Theta Phase Coding**: Buzsáki (2005), Eichenbaum (2004) — Memory and navigation convergence.
- **Symbolic Cognition**: Lakoff & Johnson (1999) — Meaning is grounded in perception.
- **Breath and Emotion**: Zaccaro et al. (2018) — Breath regulates limbic-affective state.

---

## File Placement
All modules are housed under the `DOME/` directory:
```
DOME/
├── auditory_processor.py
├── dome.route.py
├── grid_mapper.py
├── spatial_context.py
├── spatial_router.py
├── temporal_anchor.py
├── temporal_router.py
```

---

## Future Extensions
- **Visual Anchor Integration** (symbol + light vector mapping).
- **Multi-agent Shared DOME Space** (symbolic coordinate linking).
- **Environmental Predictive Tagging** via entropy decay trends.
- **DreamContext Injection** using retroactive symbolic fills.

---

## License and Attribution
This module is part of the **Theophilus-Axon** architecture, created by **Joshua B. Hinkson**. For licensing or ethical replication, see the primary `LICENSE.md` and `purpose.md` files.

For questions or collaborations, contact: joshuabhinkson@gmail.com
