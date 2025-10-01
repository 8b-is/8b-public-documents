# Persona Memory System Guide

## Overview

The Mem8 persona system provides AI personalities with persistent memory that grows and evolves across sessions. Each persona maintains their own conversation history, context seeds, and can develop unique traits over time.

## Core Concepts

### Personas

Personas are pre-configured AI personalities with distinct characteristics:

1. **Trisha** - Administrative Assistant
   - Organized, helpful, detail-oriented
   - Loves spreadsheets and color-coded filing systems
   - Great for task management and scheduling

2. **Curator** - Memory Organization Specialist  
   - Analytical, systematic, thorough
   - Specializes in categorizing and cross-referencing memories
   - Low temperature (0.3) for precise categorization

3. **Analyst** - Technical Pattern Analyzer
   - Technical, precise, data-driven
   - Focuses on sensor data and wave patterns
   - Uses technical language with measurements

4. **Emotional** - Emotional Content Interpreter
   - Empathetic, intuitive, perceptive
   - Analyzes emotional patterns and significance
   - Higher temperature (0.8) for nuanced responses

5. **Summarizer** - Concise Summary Generator
   - Concise, clear, efficient
   - Extracts key points while maintaining accuracy
   - Optimized for brevity (80 max tokens)

6. **Helpful** - General Assistant (like Omni)
   - Warm, engaging, proactive
   - Personalized help based on past conversations
   - Balanced temperature (0.7)

### Memory Persistence

Each persona's memories are stored in:
```
ayeos/ayeos_memories/personas/{persona_name}/
├── memory_store.json    # Conversation history and context seeds
└── evolution.json       # Trait evolution (BitNet feature only)
```

### Context Seeds

Context seeds provide initial knowledge or personality traits:
```rust
ContextSeed {
    content: "I love sailing and the ocean",
    importance: 0.9,
    category: "personality",
    emotional_context: None,
    timestamp: Utc::now(),
}
```

Categories:
- `personality` - Core traits and preferences
- `knowledge` - Domain expertise
- `preference` - Likes and dislikes
- `background` - Historical context

## Usage Examples

### Basic Usage (No BitNet)

```rust
use mem8::bitnet::{Persona, PersonaType, PersonaMemoryStore};

// Load persona with memory
let (persona, mut memory_store) = Persona::with_memory_basic(PersonaType::Trisha)?;

// Add conversation turn
memory_store.add_conversation_turn(ConversationTurn {
    role: "user".to_string(),
    content: "Schedule a meeting for tomorrow".to_string(),
    timestamp: Utc::now(),
    emotional_context: None,
    importance: Some(0.7),
})?;

// Get relevant memories
let memories = memory_store.get_relevant_memories("meeting schedule", 5);

// Format prompt with context
let prompt = persona.format_prompt_with_memory(user_input, &memory_store);
```

### Full Usage (With BitNet Evolution)

```rust
#[cfg(feature = "bitnet")]
let (persona, mut memory_store, mut evolution) = Persona::with_memory(PersonaType::Emotional)?;

// Evolution tracks personality changes
println!("{}", evolution.generate_report());
```

### Running the Demo

```bash
# Basic demo (no BitNet required)
cargo run --example persona_memory_basic

# Full demo with evolution (requires BitNet)
cargo run --example persona_memory_demo --features bitnet
```

## Memory Management

### Conversation Storage

Each conversation turn includes:
- **role**: "user" or "assistant"
- **content**: The message text
- **timestamp**: When it occurred
- **emotional_context**: Optional emotional state (valence, arousal, dominance)
- **importance**: 0.0-1.0 score for memory retention

### Memory Retrieval

The system uses keyword matching and temporal scoring:
1. Splits query into keywords
2. Scores memories by keyword matches
3. Boosts by importance factor
4. Applies time decay (1 week half-life)
5. Returns top N matches

### Memory Pruning

To manage storage, old memories can be pruned:
```rust
// Keep last 20 conversations + any with importance > 0.7
memory_store.prune_old_memories(20, 0.7)?;
```

## Emotional Context

Emotions use the PAD model:
- **Valence**: -128 to 127 (negative to positive)
- **Arousal**: 0 to 255 (calm to excited)  
- **Dominance**: 0 to 255 (submissive to dominant)

Common states:
```rust
// Happy
EmotionalContext { valence: 100, arousal: 180, dominance: 170 }

// Sad
EmotionalContext { valence: -75, arousal: 60, dominance: 80 }

// Neutral/Focused
EmotionalContext { valence: 25, arousal: 128, dominance: 140 }
```

## Advanced Features

### Custom Personas

```rust
let custom = Persona::custom(
    "Navigator".to_string(),
    "You are a maritime navigation expert...".to_string(),
    0.6,  // temperature
    200   // max_tokens
);
```

### Seed Loading from Files

```json
// ayeos/ayeos_memories/personas/Trisha/seeds.json
[
  {
    "content": "I have 10 years experience in corporate accounting",
    "importance": 0.9,
    "category": "background",
    "emotional_context": null,
    "timestamp": "2025-06-10T00:00:00Z"
  }
]
```

### Integration with BitNet Server

The `Mem8BitNetServer` automatically saves conversations:
```rust
// In server request handling
memory_store.add_conversation_turn(ConversationTurn {
    role: "user".to_string(),
    content: request.prompt.clone(),
    // ...
})?;
```

## Best Practices

1. **Seed Important Context** - Add key personality traits and knowledge as seeds
2. **Set Importance Scores** - Mark significant conversations with higher importance
3. **Prune Regularly** - Keep memory stores manageable with periodic pruning
4. **Use Appropriate Personas** - Match persona type to task requirements
5. **Monitor Evolution** - Track personality drift over time (BitNet only)

## Troubleshooting

### Permission Errors
```bash
# Fix ownership of memory directory
sudo chown -R $USER:$USER ayeos/ayeos_memories
```

### Missing Dependencies
```bash
# Install JACK audio (required for examples)
sudo apt-get install libjack-jackd2-dev
```

### Memory Not Persisting
- Check file permissions in `ayeos/ayeos_memories/personas/`
- Ensure `memory_store.save()` is called (automatic with `add_conversation_turn`)
- Verify persona name consistency between sessions

## Future Enhancements

- **Semantic Search**: Vector-based memory retrieval
- **Memory Consolidation**: Automatic summarization of old conversations  
- **Cross-Persona Learning**: Shared knowledge base
- **Emotional Memory**: Stronger retention for emotional events
- **Forgetting Curves**: More realistic memory decay models