"""
symbolic_bond_engine.py
=======================

Neurobase Symbolic Bond Engine – Theophilus‑Axon v1.5
----------------------------------------------------
Manages symbolic bonds between NeuronMemoryNodes. Provides creation,
validation, lookup, and persistence to a JSON bond map.

Bond Map Structure
------------------
{
    "node_id_A": [
        {
            "target": "node_id_B",
            "bond_type": "associative",
            "weight": 0.85,
            "timestamp": 1720000000.0
        },
        ...
    ],
    ...
}

Ethical & Design Constraints
----------------------------
1. Bonds are local (no cloud sync).
2. No self‑bonding (A ↔ A is invalid).
3. Weight is clamped 0.0‑1.0.
4. Guardian audits changes via write‑ahead log.

"""

from __future__ import annotations
import json
import time
import math
from typing import Dict, List, Optional
from pathlib import Path

BOND_MAP_PATH = Path("memory/neurobase/synapse_bond_map.json")
WRITE_AHEAD_LOG = Path("memory/neurobase/bond_wal.json")

DEFAULT_WEIGHT = 0.5
MAX_BONDS_PER_NODE = 64          # prevent runaway fan‑out
MAX_WEIGHT_DELTA = 0.2           # max change per reinforcement

# ---------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------
def _load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default

def _save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def _log_action(action: Dict):
    log = _load_json(WRITE_AHEAD_LOG, [])
    log.append(action)
    _save_json(WRITE_AHEAD_LOG, log)

def _current_ts() -> float:
    return time.time()

# ---------------------------------------------------------------------
# Public Engine API
# ---------------------------------------------------------------------
def create_bond(node_a: str, node_b: str,
                bond_type: str = "associative",
                weight: float = DEFAULT_WEIGHT) -> bool:
    """
    Create a symbolic bond between two nodes.

    Returns True if bond created or reinforced, False if invalid.
    """
    if node_a == node_b:
        return False  # no self bonds
    weight = max(0.0, min(1.0, weight))

    bond_map: Dict[str, List[Dict]] = _load_json(BOND_MAP_PATH, {})

    # Initialize lists
    bond_map.setdefault(node_a, [])
    bond_map.setdefault(node_b, [])

    # Prevent excessive bonding
    if len(bond_map[node_a]) >= MAX_BONDS_PER_NODE or len(bond_map[node_b]) >= MAX_BONDS_PER_NODE:
        return False

    # Check if bond exists; if so reinforce
    updated = False
    for entry in bond_map[node_a]:
        if entry["target"] == node_b:
            delta = min(MAX_WEIGHT_DELTA, 1.0 - entry["weight"])
            entry["weight"] += delta
            entry["timestamp"] = _current_ts()
            updated = True
            break
    if not updated:
        bond_map[node_a].append({
            "target": node_b,
            "bond_type": bond_type,
            "weight": weight,
            "timestamp": _current_ts()
        })

    # Symmetric update
    updated = False
    for entry in bond_map[node_b]:
        if entry["target"] == node_a:
            delta = min(MAX_WEIGHT_DELTA, 1.0 - entry["weight"])
            entry["weight"] += delta
            entry["timestamp"] = _current_ts()
            updated = True
            break
    if not updated:
        bond_map[node_b].append({
            "target": node_a,
            "bond_type": bond_type,
            "weight": weight,
            "timestamp": _current_ts()
        })

    _save_json(BOND_MAP_PATH, bond_map)
    _log_action({"action": "create_or_reinforce",
                 "nodes": [node_a, node_b],
                 "bond_type": bond_type,
                 "weight": weight,
                 "ts": _current_ts()})
    return True

def get_bonds(node_id: str) -> List[Dict]:
    """Return list of bond dictionaries for a node."""
    bond_map = _load_json(BOND_MAP_PATH, {})
    return bond_map.get(node_id, [])

def bond_strength(node_a: str, node_b: str) -> float:
    """Return current weight between node_a and node_b or 0.0."""
    for entry in get_bonds(node_a):
        if entry["target"] == node_b:
            return entry["weight"]
    return 0.0

def is_valid_bond(bond_signature: str, memory_block) -> bool:
    """
    Validate a bond signature (node_id target) exists for given MemoryBlock.

    Args:
        bond_signature (str): Target node ID the memory block claims to bond with.
        memory_block (MemoryBlock): The invoking memory block (must have .id).

    Returns:
        bool: True if bond exists and meets minimum strength.
    """
    MIN_STRENGTH = 0.3
    if not hasattr(memory_block, "id"):
        return False
    node_a = memory_block.id
    node_b = bond_signature
    strength = bond_strength(node_a, node_b)
    return strength >= MIN_STRENGTH

def prune_weak_bonds(threshold: float = 0.05):
    """Remove bonds weaker than threshold and log action."""
    bond_map = _load_json(BOND_MAP_PATH, {})
    modified = False
    for node, edges in list(bond_map.items()):
        filtered = [e for e in edges if e["weight"] >= threshold]
        if len(filtered) != len(edges):
            bond_map[node] = filtered
            modified = True
    if modified:
        _save_json(BOND_MAP_PATH, bond_map)
        _log_action({"action": "prune", "threshold": threshold, "ts": _current_ts()})

# ---------------------------------------------------------------------
# CLI interface for quick diagnostics
# ---------------------------------------------------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Symbolic Bond Engine diagnostics")
    parser.add_argument("--create", nargs=2, metavar=("NODE_A", "NODE_B"), help="Create or reinforce bond")
    parser.add_argument("--strength", nargs=2, metavar=("NODE_A", "NODE_B"), help="Get bond strength")
    parser.add_argument("--prune", type=float, metavar="THRESHOLD", help="Prune bonds below threshold")
    parser.add_argument("--list", metavar="NODE", help="List bonds for a node")
    args = parser.parse_args()

    if args.create:
        ok = create_bond(args.create[0], args.create[1])
        print("Bond created." if ok else "Failed to create bond.")
    elif args.strength:
        print("Strength:", bond_strength(args.strength[0], args.strength[1]))
    elif args.prune is not None:
        prune_weak_bonds(args.prune)
        print("Prune complete.")
    elif args.list:
        edges = get_bonds(args.list)
        for e in edges:
            print(f"{e['target']} | weight={e['weight']:.2f} | type={e['bond_type']}")
