import random

def tag_spatial_memory():
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    z = random.randint(-20, 20)
    zone = determine_zone(x, y, z)
    entropy = measure_entropy(x, y, z)
    symbol_anchor = f"SP-MAP-{x//10}-{y//10}-{z//5}"

    return {
        "coordinates": {"x": x, "y": y, "z": z},
        "zone": zone,
        "entropy": entropy,
        "symbol_anchor": symbol_anchor,
        "significance": entropy > 0.7
    }


def determine_zone(x, y, z):
    if abs(x) < 25 and abs(y) < 25:
        return "Core Zone"
    elif abs(x) < 50 and abs(y) < 50:
        return "Active Perimeter"
    return "Exploratory Fringe"


def measure_entropy(x, y, z):
    # Simulate environmental variability detection
    variability = abs(x*y*z) % 100 / 100.0
    return round(variability, 2)

