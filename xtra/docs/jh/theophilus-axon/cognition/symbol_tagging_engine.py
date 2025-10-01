# symbol_tagging_engine.py

import re

def tag_symbols(memory_block_text):
    """
    Extract and tag symbolic patterns from memory block content.

    FUNCTIONAL OVERVIEW:
    - Parses raw memory text input to identify recurring symbolic markers.
    - Flags include emotional tones, time references, numeric mentions, and abstract concepts.

    SYMBOL TYPES:
    - emotion:{word}      → Detected emotional lexicon from predefined set.
    - timestamp           → Detected pattern like 'tick 1002' (used in simulated runtime frames).
    - numeric             → General numerical pattern (e.g. digits, counters).
    - concept:{word}      → Any unique token longer than 6 characters.

    USAGE:
    Returns a dictionary containing:
    - symbols: List of unique symbolic tags
    - linked: Boolean flag if any symbols were found
    - raw: List of parsed words from original input

    SCIENTIFIC BASIS:
    - Lexical-symbolic tagging approximates early language association as a proxy for abstraction
    - Concepts and emotional valence form recursive markers in symbolic memory theory (Friston, 2010)
    - Used by Neuro Bond Mapper to establish associative pathways
    """

    timestamp_pattern = r"tick\s+\d+"
    emotional_words = {"love", "fear", "anger", "joy", "sad"}
    found_symbols = set()

    words = re.findall(r'\w+', memory_block_text.lower())

    for word in words:
        if word in emotional_words:
            found_symbols.add(f"emotion:{word}")
        elif re.match(r"\d+", word):
            found_symbols.add("numeric")
        elif len(word) > 6:
            found_symbols.add(f"concept:{word}")

    timestamp_match = re.search(timestamp_pattern, memory_block_text)
    if timestamp_match:
        found_symbols.add("timestamp")

    return {
        "symbols": list(found_symbols),
        "linked": len(found_symbols) > 0,
        "raw": words
    }

# Example usage:
# result = tag_symbols("On tick 1023, I felt joy watching the sunrise.")
# print(result)
