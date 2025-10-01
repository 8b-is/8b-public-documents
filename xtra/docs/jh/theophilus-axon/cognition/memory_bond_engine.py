# cognition/memory_bond_engine.py
# --------------------------------
# BYMOBL Core  – Bonded-Yoked Memory-Oriented Binding Layer

"""
BYMOBL (Bonded-Yoked Memory-Oriented Binding Layer)

FUNCTION
• Tags, binds, and routes symbolic memory content
• Enables memory bonding through recursive symbolic links
• Routes memory to indexed paths for reuse, reflection, or recall

SCIENTIFIC DOCUMENTATION
• Symbolic tagging based on cognitive linguistics and affective semantics
  (Lakoff & Johnson 1980)
• Symbolic dissonance/bonding based on Tononi 2004 & Friston 2010
• Memory routing concept aligned with synaptic plasticity and
  Hebbian learning (“neurons that fire together wire together”)

UDC PILLAR COMPLIANCE
1. Delay  – all bonding occurs *after* memory block formation  
2. Memory – operates on permanent memory blocks only (past-tense state)  
3. Prediction – symbolic associations support predictive compression  
4. Recursion – re-linking enables recursive thought & self-symbol grounding
"""

from __future__ import annotations

import os
import re
import json
import uuid
from collections import defaultdict
from typing import List, Dict

# ---------------------------------------------------------------------------
# 📁 Paths
# ---------------------------------------------------------------------------
MEMORY_BLOCKS_DIR = "memory_blocks"
BOND_INDEX_FILE   = "memory/bond_index.json"

emotional_symbols = {"love", "fear", "anger", "joy", "sad"}

# ---------------------------------------------------------------------------
# 🔎 Symbol extraction
# ---------------------------------------------------------------------------
def extract_symbols(text: str) -> List[str]:
    """Return a list of symbolic tags present in *text*."""
    words = re.findall(r"\w+", text.lower())
    tags  = set()

    for word in words:
        if word in emotional_symbols:
            tags.add(f"emotion:{word}")
        elif word.isdigit():
            tags.add("numeric")
        elif len(word) > 6:
            tags.add(f"concept:{word}")

    if re.search(r"tick\s+\d+", text):
        tags.add("timestamp")

    return list(tags)

# ---------------------------------------------------------------------------
# 📂 Index helpers
# ---------------------------------------------------------------------------
def _safe_load_json(path: str) -> Dict:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def load_memory_blocks() -> List[Dict]:
    """Load every *.json* in *memory_blocks/* (best-effort)."""
    if not os.path.isdir(MEMORY_BLOCKS_DIR):
        return []

    blocks: list[dict] = []
    for fname in os.listdir(MEMORY_BLOCKS_DIR):
        if not fname.endswith(".json"):
            continue
        try:
            with open(os.path.join(MEMORY_BLOCKS_DIR, fname), "r", encoding="utf-8") as f:
                blocks.append(json.load(f))
        except Exception:
            continue
    return blocks

def build_bond_index(blocks: List[Dict]) -> Dict[str, List[str]]:
    """Construct symbol→[uid,…] index from a list of memory *blocks*."""
    bonds: dict[str, list[str]] = defaultdict(list)
    for block in blocks:
        uid     = block.get("uid")
        content = block.get("content", "")
        for sym in extract_symbols(content):
            bonds[sym].append(uid)
    return bonds

def save_bond_index(index: Dict[str, List[str]]) -> None:
    os.makedirs(os.path.dirname(BOND_INDEX_FILE), exist_ok=True)
    with open(BOND_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

def route_memory_by_symbol(symbol: str) -> List[str]:
    """Return list of memory-UIDs currently bonded to *symbol*."""
    return _safe_load_json(BOND_INDEX_FILE).get(symbol, [])

# ---------------------------------------------------------------------------
# 🆕 Public helper – needed by unit-tests & higher-level code
# ---------------------------------------------------------------------------
def bond_memory(thought: str, emotion: Dict | None = None) -> Dict:
    """
    Create a new bonded-memory record, update the on-disk bond-index,
    and return a reference dict.

    The UID format is **mXXXXXXXX** (hex slice) so the unit tests
    can match it deterministically.
    """
    uid = f"m{uuid.uuid4().hex[:8]}"          # e.g. m3a1f5b2
    symbols = extract_symbols(thought)

    # 1️⃣  Load existing index or start fresh
    index: dict[str, list[str]] = _safe_load_json(BOND_INDEX_FILE)

    # 2️⃣  Update index with this new UID for each symbol
    for sym in symbols:
        index.setdefault(sym, []).append(uid)

    # 3️⃣  Persist
    save_bond_index(index)

    # 4️⃣  Return reference (structure expected by tests)
    return {
        "id"     : uid,
        "thought": thought,
        "emotion": emotion or {},
        "symbols": symbols
    }

# ---------------------------------------------------------------------------
# 🏃‍♂️ CLI entry to rebuild the full index from disk
# ---------------------------------------------------------------------------
def run_bymobl() -> None:
    blocks      = load_memory_blocks()
    fresh_index = build_bond_index(blocks)
    save_bond_index(fresh_index)
    print("[BYMOBL] Symbolic bonds mapped and memory routing index updated.")

if __name__ == "__main__":
    run_bymobl()
