# tests/manual_thought_injector.py

from cognition.self__engine.cognitive_loop_engine import CognitiveLoopEngine

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python manual_thought_injector.py \"your thought here\"")
        sys.exit(1)

    user_input = sys.argv[1]
    engine = CognitiveLoopEngine()
    response = engine.run_loop(user_input)

    print("\n\U0001F9E0 Final Response:\n", response)