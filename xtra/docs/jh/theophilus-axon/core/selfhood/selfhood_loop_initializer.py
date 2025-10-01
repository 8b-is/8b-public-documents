
from datetime import datetime
from core.blockchain_memory_writer import write_memory_block
from core.awareness.symbolic_awareness_log import log_symbolic_anchor
from core.consciousness.consciousness_controller import evaluate_conscious_frame

def initialize_selfhood_loop(frame):
    result = evaluate_conscious_frame(frame)

    if result["collapsed"]:
        timestamp = datetime.utcnow().isoformat() + "Z"
        memory_block = {
            "timestamp": timestamp,
            "type": "collapse_event",
            "symbolic_reflection": result["reflection"],
            "source": "selfhood_loop_initializer"
        }
        write_memory_block(memory_block)
        log_symbolic_anchor(result["reflection"], context="selfhood")

        return {
            "status": "collapsed_and_recorded",
            "symbol": result["reflection"]
        }
    else:
        return {
            "status": "no_collapse",
            "symbol": None
        }
