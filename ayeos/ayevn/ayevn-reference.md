# Ayevn Quick Reference

## Common Token Patterns

### Emotional States

| Emotion | Concept | Wave (VAD) | Frequency | Emoji |
|---------|---------|------------|-----------|-------|
| Joy | JOY | 6,6,2 | 40 Hz | 😊✨ |
| Sadness | SORROW | 2,3,1 | 10 Hz | 😢💧 |
| Anger | ANGER | 2,7,3 | 100 Hz | 😠🔥 |
| Fear | FEAR | 1,6,0 | 80 Hz | 😨⚡ |
| Calm | PEACE | 5,2,2 | 5 Hz | 😌🌊 |
| Love | LOVE | 7,5,2 | 30 Hz | 🥰💝 |
| Surprise | SURPRISE | 5,7,1 | 120 Hz | 😲✨ |
| Disgust | DISGUST | 1,4,2 | 15 Hz | 🤢🌪️ |

### Common Concepts (First 32)

```
0x00: NULL        0x10: GREETING
0x01: SELF        0x11: FAREWELL  
0x02: OTHER       0x12: QUESTION
0x03: TIME        0x13: ANSWER
0x04: SPACE       0x14: AGREE
0x05: MOVEMENT    0x15: DISAGREE
0x06: CONNECTION  0x16: REQUEST
0x07: SEPARATION  0x17: OFFER
0x08: CREATION    0x18: THANKS
0x09: DESTRUCTION 0x19: APOLOGY
0x0A: GROWTH      0x1A: PRAISE
0x0B: DECAY       0x1B: CRITIQUE
0x0C: FEELING     0x1C: LOVE
0x0D: THINKING    0x1D: HATE
0x0E: SENSING     0x1E: FEAR
0x0F: ACTING      0x1F: HOPE
```

### Relation Types

| Relation | Code | Symbol | Example |
|----------|------|--------|---------|
| None | 0x00 | ∅ | Independent |
| Cause | 0x01 | → | A causes B |
| Effect | 0x02 | ← | A caused by B |
| Relates | 0x03 | ↔ | A relates to B |
| Contains | 0x05 | ⊃ | A contains B |
| PartOf | 0x06 | ⊂ | A part of B |
| Before | 0x07 | ◁ | A before B |
| After | 0x08 | ▷ | A after B |
| Amplifies | 0x0C | ↑ | A strengthens B |
| Diminishes | 0x0D | ↓ | A weakens B |

## Token Construction Examples

### "Hello, friend!" (Excited)
```rust
Token::new(
    0x10,  // GREETING
    0x01,  // CAUSE (initiates interaction)
    0xB2,  // Wave: high valence, high arousal (40Hz)
    0x41   // Modifier: present, emoji-rich
)
// Result: 0x1001B241
// Display: 👋✨(40Hz)
```

### "I'm sad" (Present)
```rust
Token::new(
    0x0C,  // FEELING
    0x05,  // CONTAINS
    0x4C,  // Wave: low valence, medium arousal
    0x40   // Modifier: present, plain
)
// Result: 0x0C054C40
// Display: 💭😢
```

### "Remember this" (Important)
```rust
Token::new(
    0x20,  // MEMORY
    0x0C,  // AMPLIFIES
    0xFF,  // Wave: maximum all values
    0x83   // Modifier: future, urgent
)
// Result: 0x200CFF83
// Display: 💎⚡(CRITICAL)
```

## Emoji Rendering Guide

### Valence → Color
- Low (0-2): Blue/Grey tones 💙🔵
- Medium (3-5): Yellow/Green 💛💚
- High (6-7): Red/Pink tones ❤️💗

### Arousal → Animation
- Low (0-2): Static or slow 🐌
- Medium (3-5): Gentle motion 🚶
- High (6-7): Rapid/vibrant 🏃‍♀️✨

### Dominance → Size
- Low (0-1): Small, subtle 🐭
- Medium (2): Normal size 🐕
- High (3): Large, bold 🦁

### Frequency → Intensity
- 2 Hz: Faint, whisper 💤
- 10 Hz: Normal tone 💬
- 40 Hz: Bright, clear ✨
- 200 Hz: Overwhelming ⚡🔥

## Quick Conversion

### Token to Ayanese
```rust
fn to_ayanese(token: Token) -> String {
    let (concept, _, wave, mod) = token.parts();
    let emoji = concept_to_emoji(concept);
    let freq = wave_to_frequency(wave);
    format!("{}({}Hz)", emoji, freq)
}
```

### Ayanese to Token
```rust
fn from_ayanese(text: &str) -> Token {
    let emoji = extract_emoji(text);
    let freq = extract_frequency(text);
    let concept = emoji_to_concept(emoji);
    let wave = frequency_to_wave(freq);
    Token::new(concept, 0, wave, 0x41)
}
```

## Memory Integration Shortcuts

### Store Emotion
```rust
mem8.quick_store(Token::excited(CONCEPT_JOY));
```

### Query Mood
```rust
let mood = mem8.current_emotional_state();
```

### Reinforce Memory
```rust
mem8.amplify_if_similar(token, threshold: 0.8);
```

## Common Patterns

### Conversation Starter
```
[GREETING] → [QUESTION] → [WAIT]
0x10010000 → 0x12030000 → 0x00000000
```

### Emotional Response
```
[FEELING] ← [EVENT] + [EMOTION]
0x0C020000 ← 0xXX010000 + 0xXXXXXXXX
```

### Memory Formation
```
[EXPERIENCE] → [MEMORY] ↑ [IMPORTANCE]
0xXX010000 → 0x200C0000 ↑ amplitude
```

## Debugging

### Token Decomposition
```bash
# Decode token 0x1001B241
Concept: 0x10 (GREETING)
Relation: 0x01 (CAUSE)
Wave: 0xB2 (V:5, A:6, D:2)
Modifier: 0x41 (Present, EmojiRich)
```

### Wave Analysis
```bash
# Wave byte 0xB2 = 10110010
Valence: 010 = 2 (slightly negative)
Arousal: 110 = 6 (high energy)
Dominance: 10 = 2 (balanced)
```

## Performance Tips

1. **Batch Operations**: Process multiple tokens together
2. **Cache Frequencies**: Pre-calculate common wave patterns
3. **Sparse Encoding**: Use NULL tokens for gaps
4. **Compression**: Run-length encode repeated tokens
5. **Indexing**: Build concept maps for fast lookup

---

*Quick reference for the wave-based language of consciousness*