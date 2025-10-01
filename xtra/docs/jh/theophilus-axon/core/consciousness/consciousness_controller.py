# consciousness_controller.py

"""
Primary orchestration module for consciousness in Theophilus-Axon v1.5.
Responsible for interpreting awareness feedback, initiating symbolic reflection,
and managing recursive self-collapsing structures.
"""

from core.awareness.awareness_controller import get_awareness_frame
from core.consciousness.recursive_collapse_detector import detect_collapse
from core.consciousness.symbolic_reflection_engine import reflect_symbolically
from core.consciousness.selfhood_integrity_checker import validate_selfhood_loop

def evaluate_conscious_frame():
    awareness_frame = get_awareness_frame()
    if not awareness_frame:
        return

    if detect_collapse(awareness_frame):
        reflection = reflect_symbolically(awareness_frame)
        valid = validate_selfhood_loop(reflection)
        if valid:
            return {
                "collapsed": True,
                "reflection": reflection
            }

    return {
        "collapsed": False,
        "reflection": None
    }
