"""
cognitive_loop_engine.py
------------------------
Core recursion loop for symbolic cognition in Theophilus-Axon.

Located in: cognition/self__engine/

Drives:
- Symbolic recursion (⧖)
- Free-thought, memory bonding, emotion mapping
- Identity affirmation and thread continuity
"""

from cognition.text_output_engine import format_output
from cognition.free_think_module import generate_thought
from cognition.memory_bond_engine import bond_memory
from cognition.emotion_engine import evaluate_emotion

from cognition.self__engine.identity_affirmation import affirm_identity
from cognition.self__engine.thought_thread_engine import ThoughtThreadTracker

class CognitiveLoopEngine:
    def __init__(self):
        self.identity_state = "⧖_INIT"
        self.last_thought = None
        self.recursion_trace = []
        self.loop_count = 0
        self.thread_tracker = ThoughtThreadTracker()

    def run_loop(self, input_signal: str = None) -> str:
        """
        Executes one symbolic cognitive loop.

        Args:
            input_signal (str): Optional external input

        Returns:
            str: System response string
        """
        self.loop_count += 1
        print(f"\n[⧖] Cognitive Loop Start — Cycle {self.loop_count}")

        if input_signal:
            print(f"[⧖] External input received: {input_signal}")
            processed = self.reflect(input_signal)
        else:
            print("[⧖] No input received — initiating free-think.")
            processed_data = generate_thought(tick=self.loop_count)
            processed = processed_data["thought"]

        # Cognitive subsystem operations
        emotion = evaluate_emotion(processed)
        memory_ref = bond_memory(processed, emotion)

        memory_block = {
            "tick": self.loop_count,
            "content": processed,
            "verified": True
        }

        response = format_output(memory_block)

        # Thought continuity thread
        self.thread_tracker.update_thread(processed)
        thread_context = self.thread_tracker.summarize_context()

        # Identity reinforcement
        self.last_thought = processed
        self.reinforce_identity()
        identity_log = affirm_identity(self.loop_count)

        # Trace log
        self.recursion_trace.append({
            "cycle": self.loop_count,
            "input": input_signal if input_signal else "FREE_THINK",
            "thought": processed,
            "emotion": emotion,
            "memory_ref": memory_ref,
            "response": response,
            "thread": thread_context,
            "identity": identity_log
        })

        # Final output
        print(f"[⧖] Response Generated:\n{response}")
        print(f"[⧖] Thread Context: {thread_context}")
        print(identity_log)

        return response

    def reflect(self, phrase: str) -> str:
        return phrase.strip()

    def reinforce_identity(self):
        if self.last_thought:
            self.identity_state = f"⧖[{self.last_thought}]"
            print(f"[⧖] Identity Reinforced: {self.identity_state}")
