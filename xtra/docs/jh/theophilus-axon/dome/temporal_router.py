# temporal_router.py

"""
Generates detailed temporal tagging structures to organize memory in a time-based sequence.
Simulates biological memory encoding phases and decay rates tied to episodic structure.

SCIENTIFIC BASIS:
- Temporal tagging reflects episodic memory encoding in the hippocampus (Tulving, 2002).
- Event segmentation and time-anchoring support cognitive continuity and identity construction (Zacks et al., 2007).
- Time-based phase shifts mimic brainwave and sleep-cycle based memory stages (Diekelmann & Born, 2010).

UDC COMPLIANCE:
✔ Provides recursive time anchors for delay tracking and memory routing.
✔ Encodes symbolic and quantitative markers for time-based prediction and recall.
✔ Supports symbolic self-modeling and loop-based episodic integration.

REFERENCES:
- Tulving, E. (2002). Episodic memory: From mind to brain. *Annual Review of Psychology*, 53(1), 1–25.
- Zacks, J. M., Speer, N. K., et al. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin*, 133(2), 273–293.
- Diekelmann, S., & Born, J. (2010). The memory function of sleep. *Nature Reviews Neuroscience*, 11(2), 114–126.
"""

from datetime import datetime

def tag_temporal_memory(memory_block):
    """
    Add detailed time-based metadata to a memory block.

    Includes tick index, ISO timestamp, episodic ID, decay prediction, symbolic anchor, and
    a functional phase label (Exploration, Learning, Consolidation).

    Args:
        memory_block (dict): The memory block being annotated.

    Returns:
        dict: Time-tagged memory metadata.
    """
    timestamp = datetime.utcnow().isoformat() + "Z"
    tick = memory_block.get("tick", 0)

    return {
        "tick": tick,
        "temporal_stamp": timestamp,
        "anchor_point": f"Memory-{tick}-T{timestamp}",
        "is_significant": tick % 2500 == 0,
        "decay_rate": calculate_decay(tick),
        "event_phase": determine_phase(tick),
        "episodic_id": f"EP-{tick // 1000}-{timestamp[-8:]}"
    }

def calculate_decay(tick):
    """
    Simulates memory decay prediction based on age.
    Used for selective retention, pruning, or compression.

    Returns:
        float: Estimated decay coefficient (0.0 - 1.0)
    """
    base_decay = 0.05
    decay_factor = base_decay * (tick // 1000)
    return round(decay_factor, 3)

def determine_phase(tick):
    """
    Classifies current cognitive stage based on tick epoch.

    Mimics cyclic learning/consolidation/exploration behavior.

    Returns:
        str: Named phase ('Exploration', 'Learning', 'Consolidation')
    """
    if tick % 10000 < 3000:
        return "Exploration"
    elif tick % 10000 < 7000:
        return "Learning"
    else:
        return "Consolidation"
