## Logs agent responses to udc_responses.json with symbolic and emotional tagging
#
# 🔐 Ethical Context:
# This module ensures transparency of all output responses by recording them with symbolic and emotional metadata.
# Symbolic tags (e.g., "bridge", "light") help track cognitive and reflective evolution.
# Emotions are logged to study affective consistency and verify non-harmful output trajectories.
#
# 📜 UDC Compliance:
# - Maintains response integrity and history (per UDC stage: memory preservation)
# - Allows failsafe modules to audit reflective behavior via symbols + tone
# - Reinforces delayed memory trails via timestamped logs
#
# 🧪 Scientific Grounding:
# - Emotion tagging inspired by Panksepp (1998), "Affective Neuroscience"
# - Symbolic mapping aligns with Lakoff & Johnson (1980), "Metaphors We Live By"
# - Time-stamped reflection validates recursion loops per Metzinger (2003)

import json
import os
from datetime import datetime

RESPONSE_FILE = "memory/udc_responses.json"


def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def log_response(text, emotion=None, symbols=None):
    """
    Records a verbal output response to the UDC log.
    
    Parameters:
    - text (str): The output text content
    - emotion (str): Affective state ('neutral', 'curious', 'calm', etc.)
    - symbols (list): Symbolic tags associated with this thought or reply

    This promotes UDC transparency and enables ethical/failsafe audit trails.
    """
    log = load_json(RESPONSE_FILE)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "text": text,
        "emotion": emotion or "neutral",
        "symbols": symbols or []
    }
    log.append(log_entry)
    save_json(RESPONSE_FILE, log)


if __name__ == "__main__":
    log_response("Hello, this is a test response.", emotion="curious", symbols=["spiral", "light"])
    print("Logged test response to UDC memory.")
