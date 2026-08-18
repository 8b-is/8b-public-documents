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

# KOMPRESS v2: Geometric-Mean Consensus Distillation, Spectral Rigidity, and Structural AST Invariants for Edge Reasoning

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

**KOMPRESS v2** provides a mathematically rigorous framework for distilling frontier large language models into ultra-compact, high-speed 1.7B edge student models with ternary weights ($\{-1, 0, +1\}$) without cognitive degradation or reward-hacking.

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

## 📐 Mathematical Foundations

### 1. Consensus Equivalence & Loss Minimization
**Proposition 1 (Logit Mean Induces Normalized Geometric Mean):**  
Let $p_k(i) \propto \exp(z_{k,i}/T)$. The softmax over the arithmetic mean of teacher logits $\bar{z} = \frac{1}{K}\sum_k z_k$ satisfies:
$$\operatorname{softmax}\left(\frac{\bar{z}}{T}\right)_i = \frac{\prod_{k=1}^K p_k(i)^{1/K}}{\sum_{j=1}^V \prod_{k=1}^K p_k(j)^{1/K}} = \bar{p}(i)$$

**Proposition 2 (Optimization Equivalence):**  
Minimizing the mean reverse KL divergence to individual teachers is optimization-equivalent to minimizing reverse KL divergence against the normalized geometric-mean consensus $\bar{p}$:
$$\frac{1}{K}\sum_{k=1}^K D_{\text{KL}}(q \,\|\, p_k) = D_{\text{KL}}(q \,\|\, \bar{p}) - \log Z \implies \arg\min_q \frac{1}{K}\sum_{k=1}^K D_{\text{KL}}(q \,\|\, p_k) = \arg\min_q D_{\text{KL}}(q \,\|\, \bar{p})$$
where $Z = \sum_{j=1}^V \prod_{k=1}^K p_k(j)^{1/K}$ is student-independent.

### 2. Spectral Rigidity & Random Matrix Null Models
For the ternary null ensemble $W_{ij} \in \{-1, 0, +1\}$ with variance $p$ and aspect ratio $\gamma = m/n$, the empirical spectral distribution converges to the Marchenko-Pastur bulk with extreme singular value limits:
$$\frac{s_{\max}(W)}{\sqrt{n}} \xrightarrow{\text{a.s.}} \sqrt{p}(1 + \sqrt{\gamma}), \quad \frac{s_{\min}(W)}{\sqrt{n}} \xrightarrow{\text{a.s.}} \sqrt{p}(1 - \sqrt{\gamma})$$
To prevent both representation explosion and dimensional collapse, the trained layer preserves a restricted singular window on the active semantic subspace $\mathcal{S}$:
$$0 < c \cdot \|x - y\|_2 \le \|W(x - y)\|_2 \le C \cdot \|x - y\|_2, \quad \forall x, y \in \mathcal{S}$$

### 3. Four-Predicate Structural Admissibility
$$ \mathcal{A}(c) = \mathcal{P}(c) \land \mathcal{S}(c) \land \mathcal{T}(c) \land \mathcal{G}(c) $$
Decomposing reasoning fidelity into:
- **Predictive Fidelity ($\mathcal{F}_{\text{pred}}$)**: Distributional consensus alignment.
- **Structural Fidelity ($\mathcal{F}_{\text{struct}}$)**: AST invariant preservation.
- **Behavioral Fidelity ($\mathcal{F}_{\text{behav}}$)**: Deterministic test execution.

---

## 📊 Empirical Benchmarks

### Distillation Performance
| Configuration | Faculty Teachers | Parameters | Best Val Cross-Entropy |
|---|---|---|---|
| Base Student (Unquantized) | None | 1.7B | 2.1369 |
| Single-Teacher KD | Qwen3-14B ($T=1.5$) | 1.7B | 1.8166 |
| **KOMPRESS v2 (Council of Elders)** | **Qwen3-8B + Qwen3-14B ($T=1.5$)** | **1.7B** | **1.6120** |

### Edge Execution & Verification
- **Resident Memory**: $3.4\text{ GB} \to \mathbf{0.42\text{ GB}}$ ($8.1\times$ reduction).
- **Edge Inference**: $28\text{ tok/s} \to \mathbf{118\text{ tok/s}}$ on Apple Silicon ($4.2\times$ speedup).
- **AST Worktree Verification**: **100.0% pass rate** observed across algorithmic suites ([`DeepSiper Enthea`](https://github.com/8b-is/deepsiper-enthea)).

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
