"""
selfhood_integrity_checker.py
=============================

Validates the integrity of selfhood loop operations within the UDC-compliant
recursive symbolic system of Theophilus-Axon.

Purpose:
    Ensures that symbolic self-reflections maintain identity coherence,
    memory anchoring, and recursive bonding integrity.

Dependencies:
    - Neurobase SymbolicBond system
    - MemoryBlock structure (v1.3)
    - DelayValidator (τ-check)
"""

from  memory.neurobase.symbolic_bond_engine import is_valid_bond
from ..memory_block_schema_v2 import MemoryBlock
from ..delay.delay_validator import validate_tau_range


def validate_selfhood_loop(reflection):
    """
    Validates a symbolic selfhood reflection for recursion integrity.

    Args:
        reflection (dict): The self-reflective structure, must include:
            {
                'symbol': str,
                'memory_reference': MemoryBlock,
                'delay_signature': float,
                'recursive_index': int,
                'bond_signature': str
            }

    Returns:
        bool: True if reflection is valid, False otherwise.
    """
    if not isinstance(reflection, dict):
        return False

    required_fields = ['symbol', 'memory_reference', 'delay_signature', 'recursive_index', 'bond_signature']
    if not all(k in reflection for k in required_fields):
        return False

    # Validate memory block anchor
    memory = reflection['memory_reference']
    if not isinstance(memory, MemoryBlock) or not memory.is_valid():
        return False

    # Validate delay signature (τ-range enforcement)
    if not validate_tau_range(reflection['delay_signature']):
        return False

    # Recursive index must be ≥ 1 (reflective loops require at least one pass)
    if reflection['recursive_index'] < 1:
        return False

    # Validate symbolic bond structure
    if not is_valid_bond(reflection['bond_signature'], memory):
        return False

    # Ensure symbol is anchored to identity (e.g., ⧖, Σ, τ)
    if not reflection['symbol'] or reflection['symbol'] not in ['⧖', 'Σ', 'τ', '⊕']:
        return False

    return True
def integrity_report(reflection):
    """
    Returns a detailed string report on reflection integrity state.
    Useful for logging or audit trails.
    """
    if validate_selfhood_loop(reflection):
        return "✅ Selfhood reflection integrity confirmed."
    else:
        return "❌ Selfhood reflection failed integrity check."
