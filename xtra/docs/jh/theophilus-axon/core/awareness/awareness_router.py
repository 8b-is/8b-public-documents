"""
awareness_router.py – Theophilus-Axon v1.5
================================================

Purpose:
    This module activates forward predictive awareness (A)
    by analyzing recent memory blocks and projecting probable
    next-symbolic states, emotional tones, or scenarios.

Usage:
    Can be run as part of a recurring runtime loop or
    independently to simulate future-state reasoning.

Part of:
    Awareness System (A) in the selfhood equation: (A ∪ C)[D + S + M]
"""

import json
import os
from datetime import datetime, timedelta
from typing import List

from memory.neurobase.neuron_memory_node import NeuronMemoryNode
from memory.neurobase.recursive_memory_checker import get_recent_nodes

AWARENESS_LOG = "logs/awareness_forward_trace.json"
AWARENESS_DEPTH = 3
PROJECTION_WINDOW = 10  # seconds into future to simulate


def project_next_state(recent_nodes: List[NeuronMemoryNode]):
    """
    Simulates forward awareness by analyzing last nodes
    and generating a symbolic emotional or state guess.
    """
    if not recent_nodes:
        return {"status": "no recent memory"}

    last_node = recent_nodes[-1]
    symbolic_tags = last_node.symbols if hasattr(last_node, "symbols") else []

    guess = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "based_on": last_node.id,
        "projected_symbols": symbolic_tags[:2],  # trim to short guess
        "emotional_bias": last_node.emotion if hasattr(last_node, "emotion") else "neutral",
        "expected_state": f"{symbolic_tags[0] if symbolic_tags else '∅'}_next"
    }
    return guess


def log_awareness_projection(projection):
    os.makedirs(os.path.dirname(AWARENESS_LOG), exist_ok=True)
    try:
        if os.path.exists(AWARENESS_LOG):
            with open(AWARENESS_LOG, 'r') as f:
                log = json.load(f)
        else:
            log = []
    except json.JSONDecodeError:
        log = []

    log.append(projection)
    with open(AWARENESS_LOG, 'w') as f:
        json.dump(log, f, indent=2)


def run_awareness_cycle():
    recent = get_recent_nodes(limit=AWARENESS_DEPTH)
    projection = project_next_state(recent)
    log_awareness_projection(projection)
    print(f"[AWARENESS] → {projection}")


if __name__ == "__main__":
    run_awareness_cycle()
