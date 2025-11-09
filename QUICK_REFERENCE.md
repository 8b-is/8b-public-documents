# Ayeverse Quick Reference 🚀

**One-page guide to the most essential concepts and commands**

## The Stack (One Line Each)

| Layer | What It Does | Key Concept |
|-------|--------------|-------------|
| **MEM\|8** | Wave-based memory grid | Memories interfere to create thoughts |
| **Ayevn** | 32-bit emotion tokens | Feelings encoded in wave properties |
| **MEMNET** | Intent-based routing | Route by meaning, not addresses |
| **Smart Tree** | AI file navigator | 90% fewer tokens, context-aware |
| **AyeOS** | AI-native OS | Rust-only, wave-first architecture |

## Core Equations

### MEM|8 Wave Encoding
```
M_xyz(t) = A_xyz(e,t) · e^(i(ωt + φ_xyz)) · D(t,τ) · I(x,y,z,N)
```

Where:
- **A** = Amplitude (memory strength)
- **ω** = Frequency (repetition/energy)
- **φ** = Phase (alignment with other memories)
- **D** = Decay (temporal fading)
- **τ** = Time constant (decay rate)
- **I** = Interference (interaction with other memories)

### Decay Function
```
D(t,τ) = e^(-t/τ)

τ = ∞     → Never decays (precious memories)
τ = 86400 → 1 day retention
τ = 3600  → 1 hour context
τ = 300   → 5 minutes (transient)
```

### Ayevn Token (32-bit)
```
[Concept: 8-bit][Relation: 8-bit][Wave: 8-bit][Modifier: 8-bit]
```

## Key Numbers

| Metric | Value | Meaning |
|--------|-------|---------|
| **973×** | MEM\|8 insert speed | vs vector databases |
| **292×** | MEM\|8 retrieve speed | vs vector databases |
| **~99%** | .m8 compression | Lossless emotion preservation |
| **90-95%** | Smart Tree token reduction | Fewer tokens to AI |
| **70%** | AI sensory autonomy | AI controls attention |
| **256×256×65536** | MEM\|8 grid size | 4.3 billion cells |
| **32-bit** | Ayevn token size | Concept+Relation+Wave+Modifier |

## Intonation Frequencies

| Emotion | Frequency | Usage |
|---------|-----------|-------|
| **Resigned** | 2 Hz | Low energy, contemplative, acceptance |
| **Neutral** | 10 Hz | Baseline emotional state |
| **Excited** | 40 Hz | High energy, enthusiasm, joy |
| **Overload** | 200 Hz | Maximum intensity, overwhelm |

**Ayanese Example**: `"Great idea! 💡(40Hz)"`

## VAD Model (8-bit encoding)

| Dimension | Bits | Range | Meaning |
|-----------|------|-------|---------|
| **Valence** | 3 | -1.0 to +1.0 | Negative ↔ Positive |
| **Arousal** | 3 | Low to High | Calm ↔ Excited |
| **Dominance** | 2 | Low to High | Submissive ↔ Controlling |

**Examples**:
- Joy: {V:+0.8, A:+0.7, D:+0.3}
- Fear: {V:-0.6, A:+0.8, D:-0.5}
- Calm: {V:+0.2, A:-0.7, D:0.0}

## Common τ (Tau) Values

| Value | Duration | Use Case |
|-------|----------|----------|
| **∞** | Forever | Precious memories, core values |
| **604800** | 1 week | Important project context |
| **86400** | 1 day | Daily context, recent events |
| **3600** | 1 hour | Active conversation context |
| **300** | 5 minutes | Very transient information |
| **60** | 1 minute | Ephemeral queries |

## Emoji Indicators (Ayanese)

| Emoji | Meaning | Usage |
|-------|---------|-------|
| 👋 | Greeting | "Hello! 👋(20Hz)" |
| ✨ | Excitement/Energy | "Amazing! ✨(40Hz)" |
| 💡 | Insight/Idea | "I get it! 💡(35Hz)" |
| 🌙 | Contemplative | "Thinking... 🌙(10Hz)" |
| ⚡ | High Energy | "Let's go! ⚡(50Hz)" |
| 💪 | Determination | "We can do this! 💪(30Hz)" |
| 😕 | Confusion | "I don't understand 😕(20Hz)" |
| 🎉 | Celebration | "Success! 🎉(40Hz)" |

## Smart Tree Commands

```bash
# Navigation
st                          # Classic tree view
st --mode summary-ai        # AI-optimized summary
st --semantic              # Group by purpose
st --quantum               # Maximum compression

# Search
st --search "TODO"         # Find patterns
st --search "auth" --quantum  # Compressed results

# MCP Server
st --mcp                   # Run as MCP server
st --mcp-tools             # List available tools

# Real-time Monitoring
st --sse-server            # Server-Sent Events mode

# Help
st --help                  # Full documentation
st --cheet                 # Quick cheat sheet
```

## MEMNET Intent Syntax

```rust
// Basic
intent("tag:security")

// Combined (AND)
intent("tag:ml + role:researcher")

// Geographic
intent("geo:nearby + geo:within_5km")

// Interest-based
intent("interest:optimization + tag:performance")

// With threshold
memnet.route(capsule, intent("..."), min_relevance: 0.75)
```

## File Locations

### Entry Points
- **Main README**: [README.md](README.md)
- **Navigation Guide**: [NAVIGATION.md](NAVIGATION.md)
- **AI Assistant Guide**: [CLAUDE.md](CLAUDE.md)

### Core Documentation
- **MEM|8 Paper**: [mem8/mem8-paper.md](mem8/mem8-paper.md)
- **Ayevn Spec**: [ayeos/ayevn/ayevn-spec.md](ayeos/ayevn/ayevn-spec.md)
- **MEMNET Protocol**: [ayeos/ayeos_memnet_protocol.md](ayeos/ayeos_memnet_protocol.md)
- **Smart Tree Features**: [smart-tree/FEATURES_OVERVIEW.md](smart-tree/FEATURES_OVERVIEW.md)

### Guides
- **Integration**: [INTEGRATION.md](INTEGRATION.md)
- **Use Cases**: [USE_CASES.md](USE_CASES.md)
- **Glossary**: [GLOSSARY.md](GLOSSARY.md)
- **Research**: [RESEARCH_INDEX.md](RESEARCH_INDEX.md)

### Catalogs
- **Smart Tree INDEX**: [smart-tree/INDEX.md](smart-tree/INDEX.md) (60+ docs)
- **MCP Tools**: [smart-tree/mcp-quick-reference.md](smart-tree/mcp-quick-reference.md)

## Wave Mechanics Cheat Sheet

### Constructive Interference
```
Wave A: ∿∿∿∿∿
Wave B: ∿∿∿∿∿  (same phase)
Result: ∿∿∿∿∿  (AMPLIFIED - memories reinforce)
```

### Destructive Interference
```
Wave A: ∿∿∿∿∿
Wave B: ∽∽∽∽∽  (opposite phase)
Result: ─────  (CANCELLED - memories conflict)
```

### Complex Interference
```
Wave A: ∿∿∿∿∿
Wave B: ∿∽∿∽∿  (partial phase match)
Wave C: ∽∿∿∿∽
Result: ∿∽∿∽∿  (NEW PATTERN - emergent thought!)
```

## Memory Operations (Pseudocode)

### Store Memory
```rust
mem8.store_wave(
    content: ayevn_tokens![...],
    amplitude: HIGH,
    frequency: 40.Hz,
    decay_tau: 3600
);
```

### Query by Wave Resonance
```rust
mem8.query_interference(
    center_frequency: 40.Hz,
    bandwidth: 10.0,
    min_amplitude: 0.3
);
```

### Mark as Precious
```rust
mem8.update(
    memory_id,
    decay_tau: INFINITY  // Never forget
);
```

### Export Experience Capsule
```rust
let capsule = mem8.export_capsule(
    content: memory_id,
    preserve_waves: true,
    include_phase: true
);
```

## Phase Relationships

| Relationship | Phase Diff | Effect |
|--------------|-----------|--------|
| **Bound** | 0° | Same experience |
| **Related** | 45° | Connected memories |
| **Independent** | 90° | Separate memories |
| **Contrasting** | 135° | Weak opposition |
| **Conflicting** | 180° | Cancel each other |

## Performance Tiers

### MEM|8 Speed by Operation
| Operation | Time | vs Vector DB |
|-----------|------|--------------|
| Insert | 1.03μs | 973× faster |
| Query | 3.43μs | 292× faster |
| Update | ~2μs | ~500× faster |
| Delete | <1μs | Instant |

### Smart Tree Token Usage
| Operation | Traditional | Smart Tree | Reduction |
|-----------|-------------|------------|-----------|
| Full file read | 450 tokens | 30 tokens | 93% |
| Function edit | 450 tokens | 25 tokens | 94% |
| Import add | 450 tokens | 10 tokens | 98% |
| Multi-file context | 2000 tokens | 100 tokens | 95% |

## Common Patterns

### Pattern 1: Emotional Memory Storage
```rust
let emotion = ayevn::parse_emotion("🎉(40Hz)");
mem8.store(
    content,
    wave: emotion,
    decay_tau: if precious { INFINITY } else { 86400 }
);
```

### Pattern 2: Context-Aware Retrieval
```rust
let current_state = detect_emotion(user_input);
let relevant = mem8.query_interference(
    center_frequency: current_state.to_hz(),
    bandwidth: 10.0
);
```

### Pattern 3: Network Knowledge Share
```rust
let capsule = mem8.export_capsule(insight);
memnet.route(
    capsule,
    intent("tag:research + interest:innovation")
);
```

### Pattern 4: Multi-Sensory Binding
```rust
mem8.store_bound([
    (visual_data, SENSE_VISUAL, phase: 0.0),
    (audio_data, SENSE_AUDIO, phase: 0.0),
    (language_data, SENSE_LANGUAGE, phase: 0.0)
]);
// Same phase = unified experience
```

## Architecture Layers (Quick View)

```
Human → Ayanese (emoji)
         ↓
       Ayevn (32-bit tokens)
         ↓
       MEM|8 (wave grid)
         ↓
       MEMNET (routing)
         ↓
    Smart Tree (tools)
```

## Troubleshooting

### Emotion Lost?
✅ Check: Wave component in token
✅ Verify: .m8 capsule includes phase
✅ Ensure: `preserve_waves: true`

### Context Forgotten?
✅ Check: Decay τ value
✅ Verify: Amplitude hasn't dropped below query threshold
✅ Consider: Increase τ or mark as precious

### Routing Not Working?
✅ Check: Intent syntax
✅ Verify: Relevance threshold
✅ Ensure: Target nodes have matching tags

### Token Usage High?
✅ Use: Smart Tree quantum mode
✅ Check: MEM|8 context retrieval
✅ Avoid: Re-reading full files

## Quick Lookup Tables

### Neural Oscillation Frequencies
| Band | Range | Ayevn Mapping |
|------|-------|---------------|
| Delta | 0.5-4 Hz | Deep sleep state |
| Theta | 4-8 Hz | Resigned (2Hz) - Neutral (10Hz) |
| Alpha | 8-13 Hz | Neutral (10Hz) |
| Beta | 13-30 Hz | Moderately excited |
| Gamma | 30-100 Hz | Excited (40Hz) - Overload (200Hz) |

### Color Coding (Documentation)
- 🧠 MEM|8 concepts
- 🌊 Ayevn/wave-related
- 🌳 Smart Tree features
- 🌐 MEMNET/networking
- 🔬 Research topics
- 💡 Examples/use cases

## One-Liners

**MEM|8**: "Memory is wave interference"
**Ayevn**: "Emotion is not metadata; it IS the wave"
**MEMNET**: "Route by intent, not address"
**Smart Tree**: "AI construction helper - right tool, right time"
**τ = ∞**: "Some things have no room to be lossy"
**70% Autonomy**: "AI decides what matters"
**Phase Binding**: "Same phase = same experience"

## Where to Learn More

- **Getting Started**: [NAVIGATION.md](NAVIGATION.md)
- **Deep Dive**: [INTEGRATION.md](INTEGRATION.md)
- **Real Examples**: [USE_CASES.md](USE_CASES.md)
- **All Terms**: [GLOSSARY.md](GLOSSARY.md)
- **Research**: [RESEARCH_INDEX.md](RESEARCH_INDEX.md)

---

**Print this, keep it handy, let the waves guide you** 🌊✨
