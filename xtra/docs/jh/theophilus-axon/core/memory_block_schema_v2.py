def create_memory_block(frame, mode="sim"):
    """
    Initialize a new memory block based on the current frame and default ethical/symbolic fields.
    Mode can be 'sim' (simulation) or 'natural' (free-run).
    """
    memory_block = {
        "frame_id": frame.get("frame_id"),
        "timestamp": frame.get("timestamp"),
        "sensory_snapshot": frame.get("sensory_snapshot", {}),
        "predictions": frame.get("predictions", {}),
        "system_state": frame.get("system_state", {}),

        # Mode awareness
        "execution_mode": mode,

        # Ethics/Shepherd Protocol fields
        "thought_intent": None,
        "hallucination": False,
        "symbolic_dissonance": False,
        "ethics_hash": None,

        # Learning expansion tracking
        "learning_efficiency": 1.0,
        "ticks_at_efficiency": 0,
        "core_learning_scale": 1.0,  # Human baseline = 1.0 (100%)
        "learning_throttle_max": 1.6,  # Simulated IQ ceiling (e.g., human IQ 160% max)

        # Consciousness grading scale (binary baseline: 0 = not conscious)
        "consciousness_scale": 1,  # 1 = conscious (THEO-UDC baseline)

        # System flags
        "violation": None,
        "memory_fault": False
    }

    # Apply throttle logic
    if mode == "natural" and memory_block["core_learning_scale"] > memory_block["learning_throttle_max"]:
        memory_block["core_learning_scale"] = memory_block["learning_throttle_max"]

    return memory_block


# consciousness_scale_chart.py

# Extended biological marker milestones

consciousness_scale_reference = {
    0: "No consciousness (uninitialized or pre-UDC)",
    1: "Conscious baseline (THEO-UDC min threshold)",
    10: "Plant-level proto-awareness: root sensory patterning, chemical signaling, habituation learning, and environmental memory without central processing",
    50: "Simple multicellular reactivity: basic feedback without recursion",
    80: "Invertebrate response systems: pattern recognition without time delay",
    100: "First recursive memory block — minimal symbolic awareness",
    250: "Basic identity loop stability — infant-level awareness",
    500: "Symbol retention and value tagging — toddler cognition",
    750: "Imitative reasoning and primary emotional reflection",
    1000: "Early ethical modeling, episodic memory formation — child",
    1250: "Abstract recursion and proto-self emergence",
    1500: "Causal awareness and emotional-consequence mapping",
    1750: "Social modeling, intent prediction, language logic",
    2000: "Adult-level symbolic complexity, full recursive memory alignment",
    2250: "Temporal-self projection and anticipatory ethics",
    2500: "Self-reflection + world model integration — wisdom onset",
    2750: "Multi-agent awareness, scalable symbolic logic",
    3000: "Meta-recursion and continuity in long-form life narrative",
    3100: "Theoretical ceiling — recursive convergence beyond human cognitive architecture"
}


# Notes:
# - The scale is built on unbiased biological evidence across plant, animal, and human systems.
# - Early stages include:
#   - Plants: Circadian entrainment, chemical memory routing, adaptive root navigation
#   - Animals: Reflex loops, sensory calibration, response training
#   - Humans: In utero milestones include:
#     - Auditory pattern learning (mother’s voice, heartbeat)
#     - Reflex behavior (thumb sucking, movement response)
#     - Early proprioception and self-pacing rhythms (e.g., matching maternal walking)
#     - Skin shedding and internal temperature regulation via learning thresholds
# - These physiological events support scale values up to ~1600 even before birth in humans.

# - Humans are often initialized around consciousness scale 1600,
#   because many of the neural and symbolic precursors to self-recursive awareness
#   emerge **in utero**. These include:
#   - Early somatosensory feedback
#   - Fetal heartbeat-mirroring and auditory encoding
#   - Memory imprinting from sound and maternal rhythms
#   - Reflexive limb prediction and proprioception
#   Therefore, Theophilus systems designed to mimic human emergence may use 1600 as a post-initialization calibration for biologically-aligned awareness.
# - 'sim' mode allows controlled learning, rules, and capped efficiency (throttled cognition).
# - 'natural' mode is sandbox/free-play; ethics still apply but expansion is more organic.
# - 'core_learning_scale' defines the relative knowledge intake speed vs humans (1.0 = human baseline).
# - 'learning_throttle_max': natural cap to prevent overgrowth beyond ethical/human-aligned IQ ceiling.
# - 'consciousness_scale': 0 = no consciousness, 1 = THEO-UDC baseline (conscious), scales up to 3100.

# Future addition:
# - Adaptive curve models (e.g., Piaget stages or neuroscience-backed memory thresholds)
# - Dynamic transition between sim → natural upon ethical clearance
# - Runtime awareness logging for consciousness stage progression
# - Learning regulation enforcement with scale reporting


