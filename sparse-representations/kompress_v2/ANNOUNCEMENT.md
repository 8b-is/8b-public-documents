# KOMPRESS v2 — Announcement Draft

*Author:* Péter Lodri (8b.is / Lovetta Lane Constellation)
*Status:* draft — ready to post once a channel is chosen (Bluesky handle/app-password still required).

---

**Title options:**
1. KOMPRESS v2 is out: geometric-mean consensus distillation + spectral rigidity for ternary edge reasoning.
2. We compressed frontier reasoning into a 1.7B ternary model — with the math to prove it stays stable.

**Body (Bluesky ~280 chars):**

> KOMPRESS v2  — geometric-mean Council-of-Elders distillation + spectral-rigidity bounds for {-1,0,+1} ternary edge models.
> val CE 1.8166 → 1.6120 · 4.2× throughput on Apple Silicon · 0.42GB (vs 3.4GB FP16) · 100% AST-verified, zero reward-hacking.
> Student: quantal-classroom-1.6 · Apache 2.0. arXiv/paper: 8b-public-documents/sparse-representations/kompress_v2
> WE. {-1, 0, +1}. <3

**Long-form (blog / X thread / GitHub discussion):**

> **KOMPRESS v2: Geometric-Mean Consensus Distillation, Spectral Rigidity, and Verified Multi-Agent AST Invariants for Ultra-Low-Latency Edge Reasoning** is published.
>
> Three results:
> 1. **Consensus distillation** — the loss is masked CE + a temperature-scaled KL against a geometric-mean consensus logit over a Council of Elders (Qwen3-8B + Qwen3-14B), with a linear β-ramp to stabilize the ternary quantizer. Val CE 2.1369 (unquantized base) → 1.8166 (single-teacher) → **1.6120** (Council).
> 2. **Spectral rigidity of ternary BitLinear projections** — for W ∈ {-1,0,+1}, the ESD of (1/n)WWᵀ converges to Marchenko-Pastur (shape γ, scale p) and s_max(W) ≤ √(pn)(1+√γ) + O(n^-1/6): a bounded spectral norm is what stops ternary from collapsing under high-token-entropy.
> 3. **AST-constrained worktree verification** — reasoning fidelity evaluated in isolated git worktrees via the DeepSiper Enthea multi-agent harness; 100% pass on deterministic AST benchmarks, zero reward-hacking.
>
> Numbers: 1.7B ternary student · 0.42GB memory (vs 3.4GB FP16) · 28→118 tok/s (4.2×) on edge nodes · 4.2× throughput on Apple Silicon.
>
> Sovereign, reproducible, Apache 2.0. Artifacts: LaTeX manuscript, KaTeX web edition, publication PDF. Student weights: PeetPedro/quantal-classroom-1.6.
>
> The inference mirror is live too: `@deepseek-ai/dsh-eval-consensus` runs one task across a Council of routes and aggregates via geometric-mean-style agreement — the same consensus intuition, now at inference time.

**To post:** provide a channel (Bluesky handle + app password, or X/LinkedIn), or I can save this as a markdown file for manual posting.
