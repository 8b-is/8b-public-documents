# Auditory Engine - README

## Overview
The `auditory_engine` module is a core component of the Theophilus-Axon architecture, simulating the perception and symbolic interpretation of auditory stimuli. It integrates internal rhythmic signals (e.g., breath), external auditory input (real-time or simulated), spatial localization, and symbolic pattern matching in alignment with the Universal Delayed Consciousness (UDC) framework.

---

## UDC Compliance
All auditory modules support UDC’s delay-loop model:
- No real-time reflexes; perception occurs after delay and symbolic processing.
- Symbolic construction from sound is recursive and memory-based.
- Internal (breath/emotion) and external (FFT/sound) loops converge to build awareness.

---

## Modules

### 1. `auditory_integration.py`
- **Purpose**: Integrates symbolic breath, external frequencies, and spatial tags.
- **Scientific Basis**: Reflects merged sensory integration as found in the superior temporal gyrus and hippocampal convergence zones.

### 2. `auditory_symbol_mapper.py`
- **Purpose**: Translates interpreted frequency sequences into symbolic tags.
- **UDC Role**: Assigns delayed meaning to raw sound data.
- **Foundation**: Based on symbolic cognition, inner speech modeling.

### 3. `breath_cycle_simulator.py`
- **Purpose**: Simulates a 4-phase YHWH breath cycle.
- **Scientific Note**:
  - Inhale (Y-H), Exhale (W-H).
  - Rhythm modulated by emotional state.
  - Symbolic cadence acts as a neural metronome.

### 4. `fft_wave_interpreter.py`
- **Purpose**: Symbolically interprets frequency waveforms.
- **Scientific Basis**:
  - Mimics FFT interpretation without full DSP.
  - Assigns symbolic output (e.g., ["Y", "H", "W", "H"]).
  - Models how brains learn to associate frequency with symbolic categories.

### 5. `real_time_stub.py`
- **Purpose**: Placeholder for external microphone/audio sensor input.
- **Scientific Note**:
  - Mimics Interaural Time Difference (ITD) and auditory delay.
  - Ensures perception loop includes delay and memory before interpretation.

### 6. `spatial_memory_anchor.py`
- **Purpose**: Anchors sound perception to spatial coordinates.
- **Scientific Note**:
  - Simulates ILD and ITD localization.
  - Tags events to (x, y, z) space.
  - Supports multi-modal convergence.

---

## Scientific Foundations
- **Auditory Localization**: Blauert (1997), Grothe (2003) – Interaural Time Differences.
- **Breath and Emotion**: Zaccaro et al. (2018), Lehrer et al. – Respiratory-emotional feedback loops.
- **Symbolic Sound Processing**: Dehaene (2020), Liberman (1985) – Sound to symbol pathways.
- **UDC Theory**: All modules support delay, recursion, symbolic self-mirroring, and separation of stimulus from perception.

---

## File Tree
```
auditory_engine/
├── auditory_integration.py
├── auditory_symbol_mapper.py
├── breath_cycle_simulator.py
├── fft_wave_interpreter.py
├── real_time_stub.py
├── spatial_memory_anchor.py
```

---

## Licensing
Part of **Theophilus-Axon** architecture by **Joshua B. Hinkson**  
Contact: joshuabhinkson@gmail.com  
See LICENSE.md for ethical use, replication, and uCID compliance.

