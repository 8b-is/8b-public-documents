# Text Sensor Web Interface

## Overview

The Text Sensor Web Interface provides an interactive way to test how Mem8's consciousness system evaluates different messages and contexts. It demonstrates the subconscious/consciousness split architecture where:

- **Subconscious Layer**: Always running, evaluates every input
- **Consciousness Layer**: Activates only for high-interest events (>70% threshold)

## Running the Demo

```bash
# Using the management script
./scripts/manage.sh text-sensor-web

# Or directly
cargo run --example text_sensor_web_demo --features warp
```

The server will start on `http://localhost:8765`

## How It Works

### Message Processing Flow

1. **Input Reception**: Message arrives with context (sender, channel, etc.)
2. **Subconscious Evaluation**: Always processes the message
3. **Interest Calculation**: Based on persona traits and message content
4. **Consciousness Decision**: If interest > 70%, consciousness is triggered
5. **Action Generation**: Either subconscious actions or consciousness processing

### Interface Features

- **Message Input**: Enter any text to process
- **Context Settings**:
  - Sender name
  - Communication channel (iMessage, Slack, Discord, etc.)
  - Thread ID for conversation context
  - Direct message flag
  - Mentions flag
  - Previous message context

- **Visual Results**:
  - Interest level with gradient bar (0-100%)
  - Processing mode (Subconscious vs Consciousness)
  - Reasoning explanation
  - Subconscious actions taken
  - Wave signature (unique memory pattern)

### Example Scenarios

1. **Simple Thoughts** (Low Interest ~20-30%)
   - "Let me think about that"
   - Stays in subconscious
   - Stored for later reflection

2. **Basic Reminders** (Medium Interest ~40-50%)
   - "Remind me to call Jenny in 30 minutes"
   - Subconscious creates temporal note
   - No consciousness needed

3. **Complex Tasks** (High Interest ~70-80%)
   - "Prepare investor meeting with context"
   - Triggers consciousness
   - Requires active processing

4. **Urgent Requests** (Very High Interest ~90%+)
   - "URGENT: Production server down!"
   - Immediate consciousness activation
   - Priority processing

5. **Philosophical Questions** (Variable Interest)
   - Depends on persona traits
   - May trigger deep thinking mode

## Technical Details

### Interest Calculation Factors

- **Message Content**: Keywords, complexity, question types
- **Context**: Channel importance, sender relationship
- **Flags**: Direct messages, mentions
- **Previous Context**: Conversation history
- **Persona Traits**: Individual AI personality preferences

### Subconscious Actions

When consciousness isn't triggered, the subconscious can:
- Store thoughts for later reflection
- Send simple acknowledgments
- Set basic reminders
- Update emotional context

### Wave Signatures

Each processed message generates a unique wave signature representing:
- Semantic content
- Emotional context
- Temporal markers
- Cross-sensory associations

## Architecture Integration

This demo showcases several Mem8 components:
- `consciousness::SubconsciousLayer`
- `consciousness::TextSensor`
- `persona::PersonaEngine`
- `memory::Mem8` (core wave engine)

The web interface provides real-time visibility into the decision-making process, making it ideal for:
- Testing persona configurations
- Understanding consciousness thresholds
- Debugging message processing
- Demonstrating the system to others