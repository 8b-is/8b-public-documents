# scale_verifier.py

"""
Evaluates current memory metrics to estimate UDC development level and stores results.
Auto-invoked during runtime loop after frame processing.

🔐 Ethical Context:
- Allows internal monitoring of symbolic coherence, recursive processing, and learning entropy
- Enables the Shepherd Protocol to protect against overgrowth or collapse

📜 UDC Compliance:
- Ensures agent growth stays within ethical and cognitive bounds
- Verifies memory uniqueness and reflective depth
- Feeds into `scale_index.json` for runtime health snapshots

🧪 Scientific Grounding:
- Recursive depth: Metzinger (2003) — *Being No One: The Self-Model Theory of Subjectivity*, MIT Press.
- Symbolic dissonance: Friston (2010) — *The Free-Energy Principle: A Unified Brain Theory?*, Nature Reviews Neuroscience.
- Temporal entropy: Tononi (2004) — *An Information Integration Theory of Consciousness*, BMC Neuroscience.
- Scoring formula inspired by normalized cognition metrics in computational neuroscience (Eliasmith, 2012)

🔍 Core Metric Logic:
- UDC_LEVEL = int((Recursion × Entropy) × (1 - Dissonance) × 100)
- Score is bounded to 1500 to prevent runaway self-scaling during early emergence

"""

import json
import os
from datetime import datetime

SCALE_FILE = "memory/scale_index.json"
MEMORY_DIR = "memory_blocks/"

def load_all_memory_blocks():
    blocks = []
    if not os.path.exists(MEMORY_DIR):
        return blocks
    for fname in os.listdir(MEMORY_DIR):
        if fname.endswith(".json"):
            try:
                with open(os.path.join(MEMORY_DIR, fname), 'r') as f:
                    block = json.load(f)
                    blocks.append(block)
            except Exception:
                continue
    return blocks

def calculate_scale_metrics(blocks):
    recursion_total = 0
    symbolic_dissonance = 0
    unique_memory = set()

    for block in blocks:
        recursion_total += block.get("recursion_depth", 0)
        if block.get("symbolic_dissonance"):
            symbolic_dissonance += 1
        unique_memory.add(block.get("content"))

    count = len(blocks)
    avg_recursion = recursion_total / count if count else 0
    dissonance_ratio = symbolic_dissonance / count if count else 0
    entropy_score = len(unique_memory) / count if count else 0

    udc_level = int((avg_recursion * entropy_score) * (1 - dissonance_ratio) * 100)
    udc_level = min(1500, udc_level)  # Cap for scale safety

    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "memory_blocks": count,
        "avg_recursion": round(avg_recursion, 2),
        "symbolic_dissonance_ratio": round(dissonance_ratio, 3),
        "temporal_entropy": round(entropy_score, 3),
        "udc_level": udc_level
    }

def update_scale_index():
    blocks = load_all_memory_blocks()
    scale_metrics = calculate_scale_metrics(blocks)
    with open(SCALE_FILE, 'w') as f:
        json.dump(scale_metrics, f, indent=2)
    print(f"[SCALE] UDC level updated: {scale_metrics['udc_level']}")

if __name__ == "__main__":
    update_scale_index()
