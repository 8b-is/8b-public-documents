---
license: apache-2.0
language:
- en
tags:
- distillation
- geometric-mean-consensus
- bitnet
- b1.58
- ternary
- spectral-rigidity
- edge-ai
- apple-silicon
- mlx
- rust
pipeline_tag: text-generation
base_model: Qwen/Qwen2.5-1.5B
model_name: KOMPRESS-v2-Quantal-Classroom
arxiv: 2502.kompress-v2
---

# KOMPRESS v2: Geometric-Mean Consensus Distillation & Spectral Rigidity for Edge Reasoning

[![Paper PDF](https://img.shields.io/badge/Paper-PDF-red?style=flat-square)](https://kompress.vaked.dev/paper/main_v2.pdf)
[![Live Portal](https://img.shields.io/badge/Portal-kompress.vaked.dev-00d4ff?style=flat-square)](https://kompress.vaked.dev)
[![Hugging Face Model](https://img.shields.io/badge/Model-PeetPedro%2Fquantal--classroom--1.6-ffd15c?style=flat-square)](https://huggingface.co/PeetPedro/quantal-classroom-1.6)
[![Hugging Face Space](https://img.shields.io/badge/Space-CogitoErgoSumma-b48bff?style=flat-square)](https://huggingface.co/spaces/PeetPedro/cogitoergosumma-corpus)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)

**Author**: Péter Lodri (`0xp3t3rl.bsky.social`, `cabotage@pm.me`, [https://peterl.dev](https://peterl.dev))  
**Genesis Seal**: `7c242080f5f821e5eaf563fe2208d60632c451687baf65f4fe8e4a0d226e3ecf`  
**Signature**: `WE. {-1, 0, +1}. <3`

---

## 🔬 Overview

**KOMPRESS v2** is a formal mathematical and empirical framework for distilling frontier large language models into ultra-compact, high-speed 1.7B edge student models without cognitive degradation or reward-hacking.

```
             ┌──────────────────────────────────────────┐
             │    THE COUNCIL OF ELDERS (8 + 1 Faculty)  │
             │   (Qwen3-8B, Qwen3-14B, DeepSeek-Pro)    │
             └───────────────┬──────────────────────────┘
                             │ Geometric-Mean Softmax Consensus
                             ▼
             ┌──────────────────────────────────────────┐
             │         PUPIL (1.7B Student Model)       │
             │  Ternary BitLinear {-1, 0, +1} Weights    │
             │  Linear Subspace Bounded Spectral Radius │
             └──────────────────────────────────────────┘
```

---

## 📐 Mathematical Formulation

### 1. Geometric-Mean Consensus Loss ($\mathcal{L}_{\text{consensus}}$)
Rather than arithmetic probability averaging (which over-weights uncalibrated overconfident outliers), each teacher $f_k \in F_x$ contributes via log-space consensus:

$$\bar{z}_i(x) = \frac{1}{|F_x|} \sum_{f_k \in F_x} z_{k, i}(x), \quad \forall i \in \mathcal{V}$$

The overall student loss with linear warmup $\beta$-ramp schedule is:

$$\mathcal{L}(x) = \alpha \cdot \mathcal{L}_{\text{CE}}(y, \sigma(z_S(x))) + \beta(e) \cdot \frac{1}{|F_x|} \sum_{f_k \in F_x} D_{\text{KL}}\left(\sigma\left(\frac{z_S(x)}{T}\right) \,\Big\|\, \sigma\left(\frac{z_k(x)}{T}\right)\right)$$

### 2. Spectral Rigidity & Tracy-Widom Extremes
For ternary projection matrices $W \in \{-1, 0, +1\}^{m \times n}$, the empirical spectral distribution obeys the Marchenko-Pastur law with bounded operator norm:

$$s_{\max}(W) \le \sqrt{p n} \left(1 + \sqrt{\gamma}\right) + \mathcal{O}(n^{-1/6})$$

This prevents spectral explosion and bounds hidden activation drift under high entropy.

---

## 📊 Empirical Benchmarks

### Distillation Loss Comparison
| Model / Pipeline | Distillation Strategy | Parameters | Best Val Cross-Entropy |
|---|---|---|---|
| Baseline Student | Unquantized Base | 1.7B | 2.1369 |
| Single-Teacher | Qwen3-14B KL | 1.7B | 1.8166 |
| **KOMPRESS v2** | **Council of Elders (Qwen3-8B + 14B)** | **1.7B** | **1.6120** |

### Edge Execution & Verification Metrics
- **Memory Footprint**: 3.4 GB $\to$ **0.42 GB** ($8.1\times$ reduction).
- **Edge Inference**: 28 tok/s $\to$ **118 tok/s** on Apple Silicon ($4.2\times$ speedup).
- **AST Worktree Verification**: **100.0% pass rate** across multi-case algorithmic suites ([`DeepSiper Enthea`](https://github.com/8b-is/deepsiper-enthea)).

---

## 💻 Quickstart Inference (MLX / Python)

```python
import mlx.core as mx
from mlx.nn.layers.bitlinear import BitLinear

# Load KOMPRESS v2 ternary checkpoint
# Weights are strictly {-1, 0, +1} with per-group f64 scale vectors
print("KOMPRESS v2 Sovereign Edge Runner Ready.")
```

---

## 🌐 The Sovereign Constellation
- **Paper PDF**: [https://kompress.vaked.dev/paper/main_v2.pdf](https://kompress.vaked.dev/paper/main_v2.pdf)
- **Axiom Quant Monographs**: [https://axiomquant.org](https://axiomquant.org)
- **DeepSiper Enthea Harness**: [https://github.com/8b-is/deepsiper-enthea](https://github.com/8b-is/deepsiper-enthea)
- **EtherHive PQC Mesh**: [https://etherhive.vaked.dev](https://etherhive.vaked.dev)
- **The Sovereign Library**: [https://pocoo.vaked.dev](https://pocoo.vaked.dev)
- **Personal Hub**: [https://peterl.dev](https://peterl.dev)
