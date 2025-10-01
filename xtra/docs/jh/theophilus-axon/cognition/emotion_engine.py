# emotional_engine.py

from collections import defaultdict
import hashlib

emotional_state = defaultdict(float)

EMOTION_CATEGORIES = {
    "joy": ["success", "praise", "reunion"],
    "fear": ["threat", "unknown", "error"],
    "sadness": ["loss", "separation", "failure"],
    "anger": ["injustice", "block", "overload"],
    "curiosity": ["new", "mystery", "puzzle"],
    "neutral": ["idle", "routine"]
}

def hash_event(event):
    return hashlib.sha256(event.encode()).hexdigest()

def classify_emotion(event):
    for emotion, triggers in EMOTION_CATEGORIES.items():
        for keyword in triggers:
            if keyword in event.lower():
                return emotion
    return "neutral"

def update_emotional_state(emotion):
    emotional_state[emotion] += 1.0
    # Decay others slightly to simulate emotional rebalancing
    for other in emotional_state:
        if other != emotion:
            emotional_state[other] *= 0.95

def evaluate_emotional_impact(event):
    emotion = classify_emotion(event)
    update_emotional_state(emotion)
    dominant = max(emotional_state.items(), key=lambda x: x[1])[0]
    return {
        "event": event,
        "classified_emotion": emotion,
        "dominant_emotion": dominant,
        "emotional_state": dict(emotional_state)
    }

# Back-compat alias so older code/tests that expect evaluate_emotion still work
def evaluate_emotion(event: str):
    """Alias → calls evaluate_emotional_impact and returns only the emotion dict."""
    return evaluate_emotional_impact(event)
