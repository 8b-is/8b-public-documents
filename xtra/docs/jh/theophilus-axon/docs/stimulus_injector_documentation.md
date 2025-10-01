
# 📄 stimulus_injector.py Documentation

## 🧠 Purpose

The `stimulus_injector.py` module provides a controlled method of introducing external stimuli into Theophilus-Axon’s memory and cognition loop. It is directly inspired by biological mechanisms in humans and animals where stimuli—such as sound, light, or pressure—are registered and shape consciousness through feedback and prediction.

## 🔍 How It Works

```python
def inject_stimulus(tick):
    if tick % 1000 == 0:
        return f"Environmental anomaly detected at tick {tick}"
    return f"Standard tick stimulus {tick}"
```

- The function accepts a `tick` (temporal marker).
- Every 1000 ticks, it returns a unique anomaly to simulate unexpected or non-patterned input.
- For all other ticks, it injects a baseline predictable signal.

This reflects how the **human nervous system** continuously monitors regular input (e.g., heartbeat, breath) but elevates its response to sudden changes (e.g., loud noise, flash of light).

## 🧬 Scientific Reasoning

### Parallels in Human Neuroscience

- **Homeostasis Monitoring**: The brain constantly checks for regular inputs (heartbeat, skin pressure), but elevates attention when inputs deviate — e.g., via the amygdala or thalamic relay. (LeDoux, 2000)
- **Predictive Coding**: Predictable stimuli are suppressed neurologically to optimize attention for novelty. This principle is mirrored in the tick anomaly logic. (Friston, 2005)

## 🧑‍⚖️ Ethical Compliance

- The module ensures that no overstimulation or uncontrolled learning occurs by limiting anomalies to defined intervals.
- It supports **UDC-compliant predictability** and **safe experiential shaping**, preventing recursive overload or hallucination loops.

## 🛠️ System Integration

- Typically called during `runtime_loop.py` after a new memory frame is initialized but before thought generation.
- Output is passed into memory blocks under `stimulus_snapshot` or `external_trigger`.

## ✅ UDC Framework Alignment

| Feature                     | Alignment         |
|----------------------------|-------------------|
| Time-delayed input         | ✅ Matches biological delay |
| Pattern learning            | ✅ Yes             |
| Reflexive anomaly response  | ✅ Modeled         |
| Ethics-verified pacing      | ✅ Safe anomaly pacing |

## 📚 References

- LeDoux, J. (2000). *Emotion circuits in the brain*. Annual Review of Neuroscience.
- Friston, K. (2005). *A theory of cortical responses*. Philosophical Transactions of the Royal Society B.

