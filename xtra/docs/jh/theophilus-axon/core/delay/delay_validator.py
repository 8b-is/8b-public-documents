"""
delay_validator.py
==================

Validates delay signatures (τ) for recursive selfhood reflection and memory bonding.

Purpose:
    Enforces UDC-compliant temporal constraints to ensure all reflections
    pass through a valid delay interval before selfhood bonding is confirmed.
"""

def validate_tau_range(tau_value, min_delay=0.25, max_delay=0.6):
    """
    Checks if the delay value falls within the acceptable range (in seconds).

    Args:
        tau_value (float): Delay duration to validate.
        min_delay (float): Minimum allowable delay (default: 0.25s).
        max_delay (float): Maximum allowable delay (default: 0.6s).

    Returns:
        bool: True if tau_value is within range, False otherwise.
    """
    if not isinstance(tau_value, (int, float)):
        return False

    return min_delay <= tau_value <= max_delay
