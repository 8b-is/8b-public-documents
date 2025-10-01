def inject_stimulus(tick):
    if tick % 1000 == 0:
        return f"Environmental anomaly detected at tick {tick}"
    return f"Standard tick stimulus {tick}"
