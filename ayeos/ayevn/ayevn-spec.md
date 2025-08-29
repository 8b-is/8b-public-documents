# Ayevn Technical Specification

## Token Architecture

### Core Structure
Ayevn tokens are 32-bit unsigned integers with big-endian byte ordering:

```
┌────────┬────────┬────────┬────────┐
│ Byte 0 │ Byte 1 │ Byte 2 │ Byte 3 │
├────────┼────────┼────────┼────────┤
│Concept │Relation│  Wave  │Modifier│
│  (u8)  │  (u8)  │  (u8)  │  (u8)  │
└────────┴────────┴────────┴────────┘
```

### Component Definitions

#### Concept ID (Byte 0)
- 256 core semantic concepts
- Abstract, emotion-neutral roots
- Examples: CONNECTION, MOVEMENT, CREATION, PERCEPTION

#### Relation ID (Byte 1)
Semantic relationships between tokens:
- `None` (0x00) - Independent token
- `Cause` (0x01) - Causal relationship
- `Effect` (0x02) - Result relationship
- `Contains` (0x05) - Hierarchical inclusion
- `Amplifies` (0x0C) - Strengthens adjacent
- `Transforms` (0x0E) - Modifies meaning

#### Wave ID (Byte 2)
VAD emotional encoding (8 bits total):
```
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ V │ V │ V │ A │ A │ A │ D │ D │
└───┴───┴───┴───┴───┴───┴───┴───┘
  Valence(3)  Arousal(3) Dom(2)
```

- **Valence** (bits 0-2): Pleasure spectrum (0=negative, 7=positive)
- **Arousal** (bits 3-5): Activation level (0=calm, 7=excited)
- **Dominance** (bits 6-7): Control sense (0=submissive, 3=dominant)

#### Modifier ID (Byte 3)
Context flags (8 bits total):
```
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ T │ T │ T │ E │ E │ E │ R │ R │
└───┴───┴───┴───┴───┴───┴───┴───┘
  Temporal(3)  Emotion(3) Render(2)
```

## Wave Encoding System

### Frequency Mapping
Standard emotional frequencies with VAD values:

| Frequency | Name | Valence | Arousal | Dominance | Use Case |
|-----------|------|---------|---------|-----------|----------|
| 2 Hz | Resigned | 2 | 1 | 0 | Acceptance, letting go |
| 10 Hz | Neutral | 4 | 3 | 2 | Baseline state |
| 40 Hz | Excited | 6 | 6 | 2 | Joy, enthusiasm |
| 200 Hz | Overload | 7 | 7 | 3 | Peak intensity |

### Pack/Unpack Operations

```rust
// Packing VAD into Wave byte
fn pack_wave(valence: u8, arousal: u8, dominance: u8) -> u8 {
    (valence & 0x07) | 
    ((arousal & 0x07) << 3) | 
    ((dominance & 0x03) << 6)
}

// Unpacking Wave byte to VAD
fn unpack_wave(wave: u8) -> (u8, u8, u8) {
    let valence = wave & 0x07;
    let arousal = (wave >> 3) & 0x07;
    let dominance = (wave >> 6) & 0x03;
    (valence, arousal, dominance)
}
```

## Temporal States

Eight temporal contexts (3 bits):

| Value | State | Description | Example |
|-------|-------|-------------|---------|
| 0 | Unspecified | No temporal marking | Abstract concepts |
| 1 | Past | Completed action | "I walked" |
| 2 | Present | Current state | "I am walking" |
| 3 | Future | Anticipated action | "I will walk" |
| 4 | Iterative | Repeated action | "I walk daily" |
| 5 | Continuous | Ongoing process | "I keep walking" |
| 6 | Completed | Finished state | "I have walked" |
| 7 | Potential | Possible action | "I might walk" |

## Emotion Modes

Eight expression modifiers (3 bits):

| Value | Mode | Description | Rendering |
|-------|------|-------------|-----------|
| 0 | Raw | Unfiltered emotion | Direct display |
| 1 | Gentle | Softened expression | Muted colors |
| 2 | Excited | Amplified energy | Vibrant, animated |
| 3 | Urgent | Immediate attention | Flashing, bold |
| 4 | Overload | System stress | Warning indicators |
| 5 | Subdued | Dampened expression | Grayed, small |
| 6 | Resonant | Harmonic alignment | Synchronized waves |
| 7 | Dissonant | Conflicting state | Jarring visuals |

## Render Modes

Four display hints (2 bits):

| Value | Mode | Description |
|-------|------|-------------|
| 0 | Plain | Text only |
| 1 | EmojiRich | Full emoji rendering |
| 2 | TtsOn | Text-to-speech enabled |
| 3 | TtsEmoji | Speech with emoji description |

## Token Operations

### Construction
```rust
Token::new(concept, relation, wave, modifier)
```

### Decomposition
```rust
let (concept, relation, wave, modifier) = token.parts();
```

### Modification
```rust
token.with_concept(new_concept)
token.with_wave(new_wave)
token.with_relation(new_relation)
token.with_mod(new_modifier)
```

### Serialization
```rust
let bytes = token.to_be_bytes();
let token = Token::from_be_bytes(bytes);
```

## Integration Points

### MEM|8 Storage
- Tokens stored as wave patterns in memory grid
- Natural decay and reinforcement
- Interference-based associations

### Network Protocol
- 32-bit tokens = minimal bandwidth
- Lossless transmission
- Built-in emotional context

### Human Interface
- Emoji rendering for readability
- Frequency indicators for intensity
- Color coding for emotional state

## Example Token Patterns

### Greeting with Joy
```
Concept: GREETING (0x10)
Relation: INITIATES (0x08)
Wave: Excited/40Hz (0xB2)
Modifier: Present+Gentle+EmojiRich (0x51)
Token: 0x1008B251
Display: "👋✨(40Hz)"
```

### Sad Memory
```
Concept: MEMORY (0x20)
Relation: CONTAINS (0x05)
Wave: Low valence (0x19)
Modifier: Past+Subdued+Plain (0x28)
Token: 0x20051928
Display: "💭🌧️(past)"
```

---

*Ayevn: Where emotion meets encoding*