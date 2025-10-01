# Mem8 OpenAI-Compatible API

The Mem8 OpenAI-Compatible API allows you to interact with Mem8 personas using standard OpenAI client libraries. This enables seamless integration with existing tools and workflows.

## 🚀 Quick Start

### Starting the Server

```bash
./scripts/manage.sh openai-api
```

The server runs on port **8420** (standard Mem8 API port).

### Python Client Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8420/v1",
    api_key="mem8-dummy-key"  # Not used but required by client
)

response = client.chat.completions.create(
    model="mem8-creative-v1",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## 🤖 Available Models (Personas)

### mem8-creative-v1
**Creative Writer** - High openness and creativity
- Best for: Creative writing, storytelling, imaginative responses
- Traits: Openness (0.9), Conscientiousness (0.7), Extraversion (0.6)
- LLM Backend: llama2:latest (via Ollama)
- Temperature: 0.9

### mem8-technical-v1
**Technical Analyst** - High precision and analytical thinking
- Best for: Technical explanations, code analysis, problem solving
- Traits: Conscientiousness (0.9), Openness (0.7), Extraversion (0.4)
- LLM Backend: codellama:latest (via Ollama)
- Temperature: 0.3

### mem8-counselor-v1
**Empathetic Counselor** - High agreeableness and emotional intelligence
- Best for: Emotional support, advice, understanding perspectives
- Traits: Agreeableness (0.95), Openness (0.8), Conscientiousness (0.8)
- LLM Backend: llama2:latest (via Ollama)
- Temperature: 0.7

## 📚 API Endpoints

### Chat Completions

**Endpoint:** `POST /v1/chat/completions`

Create a chat completion with a Mem8 persona. The persona processes messages through its consciousness system, storing relevant memories in the wave-based memory system.

```json
{
  "model": "mem8-creative-v1",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Write a haiku about memories"}
  ],
  "temperature": 0.7,
  "max_tokens": 150
}
```

**Response:**
```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1700000000,
  "model": "mem8-creative-v1",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Waves upon the shore\nMemories ebb and flow free\nPatterns in the foam"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 14,
    "total_tokens": 29
  }
}
```

### Embeddings

**Endpoint:** `POST /v1/embeddings`

Generate embeddings using Mem8's wave pattern representation. Each text is processed through the memory system and returns a 1536-dimensional vector.

```json
{
  "model": "mem8-technical-v1",
  "input": [
    "Wave-based memory systems",
    "Emotional context persistence"
  ]
}
```

**Response:**
```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [0.0234, -0.0157, 0.0832, ...],
      "index": 0
    },
    {
      "object": "embedding", 
      "embedding": [0.0412, 0.0923, -0.0234, ...],
      "index": 1
    }
  ],
  "model": "mem8-technical-v1",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

### Audio Transcriptions

**Endpoint:** `POST /v1/audio/transcriptions`

Upload audio files for transcription and storage in Mem8's memory system.

```bash
curl -X POST http://localhost:8420/v1/audio/transcriptions \
  -F "file=@audio.wav" \
  -F "model=mem8-technical-v1"
```

**Response:**
```json
{
  "text": "Audio transcription will be processed through Mem8's audio system."
}
```

### File Upload

**Endpoint:** `POST /v1/files`

Upload files (PDF, Word, Excel, JSON, XML, HTML, Images) for processing and memory storage.

```bash
curl -X POST http://localhost:8420/v1/files \
  -F "file=@document.pdf" \
  -F "purpose=assistants"
```

**Response:**
```json
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 12345,
  "created_at": 1700000000,
  "filename": "document.pdf",
  "purpose": "assistants"
}
```

### List Models

**Endpoint:** `GET /v1/models`

List all available Mem8 personas.

**Response:**
```json
{
  "object": "list",
  "data": [
    {"id": "mem8-creative-v1", "object": "model", "owned_by": "mem8"},
    {"id": "mem8-technical-v1", "object": "model", "owned_by": "mem8"},
    {"id": "mem8-counselor-v1", "object": "model", "owned_by": "mem8"}
  ]
}
```

## 🧠 How It Works

### Consciousness Processing

When you send a message to a Mem8 persona:

1. **Stimulus Evaluation**: The text is processed through the consciousness system
2. **Interest Calculation**: Based on persona traits, an interest level is calculated
3. **Memory Storage**: If interest > 70%, consciousness activates and memories are stored
4. **LLM Generation**: The persona's LLM generates a contextual response
5. **Wave Pattern Creation**: The interaction creates wave patterns in the memory grid

### Memory Integration

- All conversations are stored as wave patterns in Mem8's 2D memory grid
- Emotional context (valence, arousal, dominance) is extracted and stored
- Related memories interfere constructively, creating associations
- Memory decay is modulated by emotional significance

### Cross-Modal Support

The API supports multiple modalities:
- **Text**: Chat completions and embeddings
- **Audio**: Transcription and voice processing
- **Files**: Document analysis and extraction
- **Images**: Visual memory storage (via file upload)

## 🔧 Configuration

### Environment Variables

```bash
# Ollama backend URL (default: http://localhost:11434)
export OLLAMA_API_BASE="http://localhost:11434"

# Memory storage location (default: mem8_openai_api.db)
export MEM8_STORAGE="./my_memory.db"

# Grid dimensions (default: 256x256)
export MEM8_GRID_SIZE="512"
```

### Custom Personas

To add custom personas, modify the `create_personas()` function in `openai_api_server.rs`:

```rust
personas.insert(
    "mem8-scientist-v1".to_string(),
    Arc::new(PersonaProfile {
        name: "Research Scientist".to_string(),
        traits: vec![
            PersonaTrait::Openness(0.95),
            PersonaTrait::Conscientiousness(0.85),
            PersonaTrait::Extraversion(0.3),
            PersonaTrait::Agreeableness(0.6),
            PersonaTrait::Neuroticism(0.2),
        ],
    }),
);
```

## 📦 Client Libraries

### Python
```bash
pip install openai
```

### Node.js
```bash
npm install openai
```

### Go
```bash
go get github.com/sashabaranov/go-openai
```

### Rust
```toml
[dependencies]
async-openai = "0.14"
```

## 🌊 Advanced Features

### Streaming Responses
*Note: Currently in development*
```python
stream = client.chat.completions.create(
    model="mem8-creative-v1",
    messages=[{"role": "user", "content": "Tell a story"}],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content, end="")
```

### Memory Context Window
Each persona maintains a rolling context window of recent interactions:
- Window size: 10 messages
- Temporal binding: ±2 seconds
- Cross-sensory associations enabled

### Emotional Modulation
Responses are modulated by detected emotional context:
- High arousal → More energetic responses
- Positive valence → Warmer tone
- High dominance → More assertive style

## 🚨 Error Handling

### Common Errors

**Model Not Found**
```json
{
  "error": {
    "message": "Model 'mem8-unknown' not found",
    "type": "invalid_request_error",
    "code": 404
  }
}
```

**Consciousness Threshold Not Met**
When interest level < 70%, you may receive brief subconscious responses:
```json
{
  "choices": [{
    "message": {
      "content": "I understand. Interest level: 45.2%"
    }
  }]
}
```

## 🔍 Monitoring

### Health Check
```bash
curl http://localhost:8420/health
# Response: OK
```

### Memory Stats
Use the Mem8 CLI to monitor memory usage:
```bash
./scripts/manage.sh cli status
```

## 🎯 Use Cases

1. **Creative Writing Assistant**
   - Use `mem8-creative-v1` for story generation
   - Memories of previous stories influence new creations

2. **Technical Documentation**
   - Use `mem8-technical-v1` for code explanation
   - Builds knowledge graph of technical concepts

3. **Personal AI Companion**
   - Use `mem8-counselor-v1` for conversational AI
   - Remembers personal context and preferences

4. **Multi-Modal Analysis**
   - Upload documents, images, and audio
   - Cross-sensory binding creates rich associations

## 🛠️ Troubleshooting

### Server Won't Start
- Check if port 8420 is available: `lsof -i :8420`
- Ensure Ollama is running: `ollama serve`
- Check Mem8 build: `./scripts/manage.sh build`

### Slow Responses
- First request initializes personas (may take a few seconds)
- Check Ollama model availability: `ollama list`
- Monitor memory usage: `./scripts/manage.sh cli performance`

### Memory Not Persisting
- Check write permissions on memory database
- Verify consciousness activation (interest > 70%)
- Use CLI to inspect memory grid: `./scripts/manage.sh cli memory list`

## 📝 Examples

Full example scripts available in `examples/`:
- `openai_api_client_demo.py` - Python client demonstration
- `openai_api_server.rs` - Server implementation

Run the demo:
```bash
# Terminal 1: Start server
./scripts/manage.sh openai-api

# Terminal 2: Run client demo
python examples/openai_api_client_demo.py
```

---

*"Like waves in the ocean, memories flow through Mem8's consciousness, creating patterns more beautiful than their individual forms."* - Omni