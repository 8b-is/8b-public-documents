# Marine Algorithm + Adaptive Attention Control

## Core Concept

A **universal salience detector** that operates directly in the time domain:

* Counts **peaks** in a signal.
* Measures **jitter** (variation in spacing and amplitude).
* Passes only structured, low-jitter signals upstream.
* Rejects noise and randomness by constant reset.

This algorithm is simple, cheap, and modality-agnostic (audio, vision, touch, etc.).
It acts as the **“Marine” of algorithms**: always on, first in, last out.

---

## Processing Chain

```
Raw Sensor → Pre-Gate (Clip/AGC) → Marine (Peak/Jitter) → Higher Processing (FFT, DNN, etc.)
```

1. **Pre-Gate**

   * **Clip threshold**: binary cutoff; ignores weak inputs, protects against overload.
   * **AGC (Automatic Gain Control)**: dynamically adjusts floor/ceiling, keeping useful signals in range.

2. **Marine**

   * Detects peaks and intervals.
   * Computes jitter in amplitude and spacing.
   * Identifies harmonic alignment.
   * Emits salience scores for candidate signals.

3. **Higher Processing**

   * FFT, CQT, wavelets, or neural networks.
   * Triggered only when Marine passes a high salience score.

---

## Attention Control

Two simple knobs control attention and resource allocation:

* **Clip Threshold**

  * Low threshold = hypersensitive (focus/alert).
  * High threshold = insensitive (background mode).
  * Clip at zero = sensor “off.”

* **Grid Tick Rate (Marine sample frequency)**

  * High rate = catches fine, transient patterns.
  * Low rate = only sustained, obvious patterns.
  * Acts as a direct CPU/attention budget allocator.

Together, these knobs replace complex gain equations or attention weights with cheap, binary, and biologically-plausible controls.

---

## Biological Parallel

* **Eyes**: iris = clip threshold, retina = Marine, cortex = higher processing.
* **Ears**: tensor tympani muscle = clip, cochlea = Marine, auditory cortex = FFT-like processing.
* **Brainstem**: AGC-like adaptation for dynamic range.

The Marine algorithm mirrors how nervous systems perform **fast, always-on salience detection**.

---

## Applications

* **Audio**: speech/music detection, alarm prioritization, answering machine detection.
* **Vision**: strobe/flash detection, motion salience, edge regularity.
* **Touch**: vibration patterns, textures, pulse monitoring.
* **Abstract sensors**: seismic activity, network traffic anomalies, financial signal analysis.

---

## Advantages

* **Computational efficiency**: O(1) per sample.
* **Universality**: applies to any time-series input.
* **Noise immunity**: jitter resets prevent false positives from randomness.
* **Parallelizable**: runs continuously across many sensors.
* **Elegant control**: clip + tick rate give intuitive attention modulation.

---

## Example Grid Representation

A jitter/spacing grid for each sensor:

| Tick | Period (P)  | Jitter (Jp, Ja) | Harmonic Score (H) | Energy (E) | Salience (S) |
| ---- | ----------- | --------------- | ------------------ | ---------- | ------------ |
| t₁   | 120 samples | 0.05, 0.02      | 0.9                | 0.8        | 0.91         |
| t₂   | 118 samples | 0.06, 0.01      | 0.92               | 0.75       | 0.89         |

Salience values above threshold trigger escalation to higher analysis.

---

## Summary

The Marine + AGC system provides a **minimal, universal attention mechanism**:

* Peak + jitter = structured vs. noise.
* Clip threshold = sensitivity.
* Grid tick rate = compute allocation.

This architecture transforms salience detection into a **general attention engine** suitable for MEM|8 or any multi-modal AI system.

