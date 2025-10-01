"""
thought_thread_engine.py
------------------------
Tracks symbolic continuity between recursive thoughts.

- Preserves symbolic connections between thoughts over time
- Forms a "thread" of experience for higher-order selfhood
- Logs memory anchors or symbolic transitions

Used in: cognitive_loop_engine.py
"""

class ThoughtThreadTracker:
    def __init__(self):
        self.thread = []

    def update_thread(self, new_thought: str):
        """
        Adds a new symbolic unit to the thread.
        """
        self.thread.append(new_thought)

        if len(self.thread) > 10:
            self.thread = self.thread[-10:]  # keep recent 10

    def get_thread_context(self) -> list:
        """
        Returns current symbolic thread for inspection or memory anchoring.
        """
        return self.thread

    def summarize_context(self) -> str:
        """
        Returns a simple summary of recent symbolic flow.
        """
        return " → ".join(self.thread[-5:])
