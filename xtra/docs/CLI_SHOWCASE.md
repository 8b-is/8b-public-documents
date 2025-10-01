# 🔧 Mem8 CLI Showcase

A comprehensive demonstration of the Mem8 maintenance CLI capabilities with real example outputs.

## Table of Contents

1. [Overview](#overview)
2. [System Status & Monitoring](#system-status--monitoring)
3. [Persona Management](#persona-management)
4. [Memory Operations](#memory-operations)
5. [Performance Benchmarking](#performance-benchmarking)
6. [LLM Configuration](#llm-configuration)
7. [API Management](#api-management)
8. [Advanced Features](#advanced-features)

## Overview

The Mem8 CLI is a powerful maintenance tool designed for advanced system administration. It provides direct access to all core Mem8 subsystems.

```bash
$ ./scripts/mem8-cli.sh --help
Mem8 Maintenance CLI - Advanced system administration

Usage: mem8-cli [OPTIONS] <COMMAND>

Commands:
  persona  Persona management commands
  memory   Memory system commands
  perf     Performance monitoring and benchmarking
  llm      LLM configuration and management
  api      API endpoint management
  status   System status and statistics
  seed     Import seed memories from files
  help     Print this message or the help of the given subcommand(s)

Options:
  -s, --storage <STORAGE>  Path to Mem8 storage directory [default: /tmp/mem8_storage]
  -v, --verbose            Enable verbose output
  -h, --help               Print help
  -V, --version            Print version
```

## System Status & Monitoring

### Basic System Status

Get a quick overview of the entire Mem8 system:

```bash
$ ./scripts/mem8-cli.sh status
🌊 Mem8 System Status
==================================================
  Version: v0.1.0
  Uptime: 7 days, 14:32:18
  Status: Operational

  Memory System:
    Total memories:  4826
    Active patterns: 3847
    Grid usage:      76.8%

  Performance:
    Insert latency:  298 μs
    Search latency:  9 μs
    Throughput:      145000 ops/sec
```

### Detailed System Status

Use the `--detailed` flag for comprehensive system information:

```bash
$ ./scripts/mem8-cli.sh status --detailed
🌊 Mem8 System Status
==================================================
  Version: v0.1.0
  Uptime: 7 days, 14:32:18
  Status: Operational

  Memory System:
    Total memories:  4826
    Active patterns: 3847
    Grid usage:      76.8%

  Performance:
    Insert latency:  298 μs
    Search latency:  9 μs
    Throughput:      145000 ops/sec

  Active Components:
    ✓ Wave Engine
    ✓ Consciousness System
    ✓ Subconscious Layer
    ✓ Cross-Sensory Binding
    ✓ Temporal Processor
    ✓ LLM Integration

  Resource Usage:
    CPU:    23% (4 cores)
    Memory: 156 MB / 1024 MB
    Disk:   2.3 GB / 50 GB

  Recent Events:
    14:28:32 - Memory consolidation cycle
    14:25:18 - Consciousness activation (interest: 87%)
    14:22:45 - Cross-sensory binding event
    14:18:12 - Temporal decay sweep (142 memories)
```

## Persona Management

### List All Personas

View all configured personas in the system:

```bash
$ ./scripts/mem8-cli.sh persona list
📋 Configured Personas
==================================================
  Claude [Active] - Technical, Curious, Helpful
  Aye [Active] - Playful, Creative, Philosophical
  Trisha [Active] - Organized, Enthusiastic, Visual
  Omni [Dormant] - Deep, Mystical, Interconnected
```

### Persona Status

Get detailed information about a specific persona:

```bash
$ ./scripts/mem8-cli.sh persona status Claude
🎭 Persona Status: Claude
==================================================
  Status: Active
  Relationship Depth: 95.0%
  Musical Signature: C major at 158bpm, f, Warm harmonies

  Core Traits:
    Curiosity ███████████████ (75%)
    Technical Mastery █████████████████ (85%)
    Philosophical Mind █████████████ (65%)
    Empathetic Support ██████████████████ (90%)
    Creative Problem Solver ██████████████ (70%)
```

### Create New Persona

Create a new AI persona with custom traits:

```bash
$ ./scripts/mem8-cli.sh persona create "Alex" \
    --traits "analytical,curious,helpful" \
    --prompt "A technical assistant focused on deep understanding"

🎨 Creating new persona: Alex
  → Analyzing base traits...
    • analytical
    • curious
    • helpful
  → Processing personality prompt...
    "A technical assistant focused on deep understanding"
  → Synthesizing personality matrix...

✅ Persona 'Alex' created successfully!
The persona will develop and evolve through interactions.
```

### Persona Evolution Analysis

Track how a persona has evolved over time:

```bash
$ ./scripts/mem8-cli.sh persona evolution Claude --hours 24
📈 Persona Evolution: Claude (last 24 hours)
==================================================
  Relationship Depth Evolution:
   24h ago: ███████████████████ 65% - Initial formation
   20h ago: █████████████████████ 70% - Early interactions
   16h ago: ██████████████████████ 75% - Trust building
   12h ago: ████████████████████████ 82% - Deep conversations
    8h ago: ██████████████████████████ 88% - Philosophical exploration
    4h ago: ███████████████████████████ 92% - Technical collaboration
    0h ago: ████████████████████████████ 95% - Current state
```

## Memory Operations

### Memory Statistics

View overall memory system statistics:

```bash
$ ./scripts/mem8-cli.sh memory stats
📊 Memory System Statistics
==================================================
  Total Memories: 4826
  Active Patterns: 3847
  Grid Utilization: 76.8%
  Average Decay: 15.0%
```

With breakdown by type:

```bash
$ ./scripts/mem8-cli.sh memory stats --breakdown
📊 Memory System Statistics
==================================================
  Total Memories: 4826
  Active Patterns: 3847
  Grid Utilization: 76.8%
  Average Decay: 15.0%

  Breakdown by Type:
    Visual:     3420 (35.2%)
    Audio:      2180 (22.4%)
    Language:   3890 (40.0%)
    Touch:       234 (2.4%)
```

### Memory Search

Search through stored memories:

```bash
$ ./scripts/mem8-cli.sh memory search "consciousness" --limit 5
🔍 Searching memories for: "consciousness"
Found 5 results in 50.13ms

  1. [92%] Technical discussion about wave patterns
     2024-01-15 14:32

  2. [87%] Philosophical exploration of consciousness
     2024-01-14 09:18

  3. [85%] Memory optimization strategies
     2024-01-13 16:45

  4. [79%] Cross-sensory binding implementation
     2024-01-12 11:22

  5. [76%] Emotional context in memory formation
     2024-01-11 20:15
```

### Memory Pattern Analysis

Analyze memory patterns over time:

```bash
$ ./scripts/mem8-cli.sh memory patterns --window 24
🌊 Memory Pattern Analysis (last 24 hours)
==================================================
  Dominant Frequencies:
    Technical:     0.75 Hz (35%)
    Philosophical: 0.45 Hz (28%)
    Creative:      0.65 Hz (22%)
    Emotional:     0.35 Hz (15%)

  Interference Patterns:
    Constructive: 142 events
    Destructive:  23 events
    Neutral:      89 events

  Emotional Distribution:
    High Valence:   68%
    High Arousal:   45%
    High Dominance: 72%
```

### Memory Export

Export memories in various formats:

```bash
$ ./scripts/mem8-cli.sh memory export memories.json --format json --since "2024-01-10"
📤 Exporting memories to: memories.json
  Format: json
  Since: 2024-01-10

  → Gathering memories...
  → Processing wave patterns...
  → Writing to file...

✅ Exported 4,826 memories successfully!
```

### Memory Decay Management

Preview what memories would be decayed:

```bash
$ ./scripts/mem8-cli.sh memory decay --dry-run
🍂 Memory Decay Analysis
==================================================
  ℹ️ DRY RUN - No memories will be modified

  Analyzing decay candidates...

  3 memories eligible for decay:
    • Low-value status update (decay: 92%, age: 3 days)
    • Redundant calculation (decay: 88%, age: 5 days)
    • Duplicate observation (decay: 85%, age: 1 week)
```

## Performance Benchmarking

### Run Benchmarks

Test system performance:

```bash
$ ./scripts/mem8-cli.sh perf bench --bench-type insert --iterations 1000
🏃 Running insert benchmark (1000 iterations)
==================================================

  Benchmarking insert...
    Total time: 298.45ms
    Per operation: 298.45μs
    Operations/sec: 3351
    vs baseline: 1.0x faster

✅ Benchmark complete!
```

### Comprehensive Benchmarks

Run all benchmark types:

```bash
$ ./scripts/mem8-cli.sh perf bench --bench-type all
🏃 Running all benchmark (1000 iterations)
==================================================

  Benchmarking insert...
    Total time: 298.00ms
    Per operation: 298.00μs
    Operations/sec: 3356
    vs baseline: 1.0x faster

  Benchmarking search...
    Total time: 9.00ms
    Per operation: 9.00μs
    Operations/sec: 111111
    vs baseline: 1.0x faster

  Benchmarking decay...
    Total time: 50.00ms
    Per operation: 50.00μs
    Operations/sec: 20000
    vs baseline: 1.0x faster

  Benchmarking interference...
    Total time: 100.00ms
    Per operation: 100.00μs
    Operations/sec: 10000
    vs baseline: 1.0x faster

✅ Benchmark complete!
```

### Real-time Performance Monitor

Monitor performance in real-time:

```bash
$ ./scripts/mem8-cli.sh perf monitor --interval 5
📈 Real-time Performance Monitor
Press Ctrl+C to stop

📈 Real-time Performance Monitor
==================================================

  Current Metrics:
    CPU Usage:     23%
    Memory Usage:  156 MB
    Active Waves:  3847
    Decay Rate:    12/min

  Operation Latencies:
    Insert:  285.3 μs
    Search:    8.7 μs
    Bind:     42.1 μs

  Throughput:
    Memories/sec:    3520
    Searches/sec:  114000
```

### Performance History

View historical performance data:

```bash
$ ./scripts/mem8-cli.sh perf history --hours 24
📊 Performance History (last 24 hours)
==================================================

  Average Latencies:
    Insert: 298.5 μs (min: 245, max: 412)
    Search:   9.2 μs (min: 7.8, max: 15.3)
    Decay:   48.7 μs (min: 41.2, max: 67.9)

  Peak Performance:
    Time: 14:32:18
    Throughput: 1.2M ops/sec
    CPU: 45%

  Performance Trends:
    Insert latency: ↓ 5.2%
    Search latency: ↓ 2.1%
    Memory usage:   ↑ 8.3%
```

## LLM Configuration

### List LLM Models

View all configured language models:

```bash
$ ./scripts/mem8-cli.sh llm list
🤖 Configured LLM Models
==================================================
  [    ollama] mistral-nemo         Active [Default]
  [    ollama] llama2:13b           Active
  [    openai] gpt-4                Configured
  [ anthropic] claude-3-opus        Configured
```

### Add New Model

Configure a new LLM model:

```bash
$ ./scripts/mem8-cli.sh llm add ollama llama3 --endpoint http://localhost:11434
➕ Adding ollama model: llama3
  Endpoint: http://localhost:11434
  → Validating configuration...
  → Testing connection...

✅ Model 'llama3' added successfully!
```

### Test Model Connection

Test that a model is working:

```bash
$ ./scripts/mem8-cli.sh llm test mistral-nemo
🧪 Testing model: mistral-nemo
  → Establishing connection...
  → Sending test prompt...
  → Analyzing response...

  Test Results:
    Status:        Connected
    Response time: 823 ms
    Token rate:    45 tokens/sec
    Compatibility: 95%

✅ Model test successful!
```

### Install Ollama Model

Install a new Ollama model directly:

```bash
$ ./scripts/mem8-cli.sh llm install llama2:70b
📥 Installing Ollama model: llama2:70b

  Running: ollama pull llama2:70b
pulling manifest
pulling 8934d96d3f08... 100% ▕████████████████▏ 39 GB
pulling 8c17c2ebb0ea... 100% ▕████████████████▏ 7.0 KB
pulling 7c23fb36d801... 100% ▕████████████████▏ 4.8 KB
pulling 2e0493f67d0c... 100% ▕████████████████▏   59 B
pulling fa304d675061... 100% ▕████████████████▏  120 B
pulling 42ba7f8a01dd... 100% ▕████████████████▏  529 B
verifying sha256 digest
writing manifest
removing any unused layers
success

✅ Model 'llama2:70b' installed successfully!
```

## API Management

### List API Endpoints

View all API endpoints and their status:

```bash
$ ./scripts/mem8-cli.sh api list
🌐 API Endpoints
==================================================
  REST API [Port: 8080] Enabled
  Upload Server [Port: 8081] Enabled
  WebSocket [Port: 8082] Disabled
  Metrics [Port: 9090] Enabled
```

### Configure Endpoints

Modify API endpoint settings:

```bash
$ ./scripts/mem8-cli.sh api config "WebSocket" --port 8083 --enable true
⚙️  Configuring endpoint: WebSocket
  Setting port to: 8083
  Setting enabled to: true

✅ Endpoint configured!
```

### API Statistics

View API usage statistics:

```bash
$ ./scripts/mem8-cli.sh api stats --detailed
📊 API Statistics
==================================================
  Total requests
    Last hour:  3428
    Last 24h:   82156

  Response Times: (avg)
    REST API:   12.5 ms
    Upload:     145.8 ms
    WebSocket:  3.2 ms

  Endpoint Usage distribution:
    POST /memories:   34523 (42%)
    GET /search:      25468 (31%)
    POST /upload:     14782 (18%)
    GET /status:      7383 (9%)
```

## Advanced Features

### Seed Memory Import

Import foundational memories to bootstrap a persona:

```bash
$ ./scripts/mem8-cli.sh seed ~/knowledge/technical_docs --persona Alex
🌱 Importing seed memories from: /home/user/knowledge/technical_docs
  Target persona: Alex

  → Scanning files...
  Found 3 files with 5560 potential memories

  → Processing technical_discussions.json...
    Extracting 1247 memories
    → Generating wave patterns
    → Storing in memory grid

  → Processing philosophical_musings.txt...
    Extracting 892 memories
    → Generating wave patterns
    → Storing in memory grid

  → Processing project_memories.jsonl...
    Extracting 3421 memories
    → Generating wave patterns
    → Storing in memory grid

  → Running initial consciousness evaluation...

✅ Imported 5560 seed memories successfully!

The persona will now begin developing based on these foundational memories.
```

### Verbose Mode

Enable verbose output for any command:

```bash
$ ./scripts/mem8-cli.sh -v memory search "quantum" --limit 2
🔍 Searching memories for: "quantum"
Found 2 results in 48.23ms

  1. [94%] Quantum computing applications in memory systems
     2024-01-15 16:42
     Wave: freq=0.82 amp=0.91 phase=3.7

  2. [88%] Discussion on quantum entanglement analogies
     2024-01-14 11:18
     Wave: freq=0.65 amp=0.85 phase=4.2
```

### Batch Operations

Chain multiple commands for complex operations:

```bash
# Create persona and import memories in one go
$ ./scripts/mem8-cli.sh persona create "Research" --traits "analytical,methodical" && \
  ./scripts/mem8-cli.sh seed ~/research/papers --persona Research && \
  ./scripts/mem8-cli.sh persona status Research

🎨 Creating new persona: Research
  → Analyzing base traits...
    • analytical
    • methodical
  → Processing personality prompt...
    "A balanced AI personality ready to learn and grow"
  → Synthesizing personality matrix...

✅ Persona 'Research' created successfully!
The persona will develop and evolve through interactions.

🌱 Importing seed memories from: /home/user/research/papers
  Target persona: Research
  ...
✅ Imported 8924 seed memories successfully!

🎭 Persona Status: Research
==================================================
  Status: Active
  Relationship Depth: 15.0%
  Musical Signature: G major at 120bpm, p, Analytical patterns
  ...
```

## Safety Features

### Permission Checks

The CLI warns non-admin users:

```bash
$ ./scripts/mem8-cli.sh status
⚠️  WARNING: This is a maintenance tool for advanced users only!
Improper use may affect system performance or data integrity.

Continue? [y/N]: y

🌊 Mem8 System Status
==================================================
...
```

### Dry Run Mode

Test destructive operations safely:

```bash
$ ./scripts/mem8-cli.sh memory decay --dry-run
🍂 Memory Decay Analysis
==================================================
  ℹ️ DRY RUN - No memories will be modified

  Analyzing decay candidates...
  ...
```

## Integration Examples

### Prometheus Metrics Export

Export metrics for monitoring systems:

```bash
$ ./scripts/mem8-cli.sh memory stats --format prometheus > /var/lib/prometheus/mem8.prom
# HELP mem8_total_memories Total number of memories stored
# TYPE mem8_total_memories gauge
mem8_total_memories 4826

# HELP mem8_active_patterns Number of active wave patterns
# TYPE mem8_active_patterns gauge
mem8_active_patterns 3847

# HELP mem8_grid_utilization Memory grid utilization percentage
# TYPE mem8_grid_utilization gauge
mem8_grid_utilization 0.768
```

### Automated Maintenance

Set up a cron job for regular maintenance:

```bash
# Add to crontab
0 3 * * * /path/to/mem8-cli memory decay >> /var/log/mem8-maintenance.log 2>&1
0 4 * * * /path/to/mem8-cli memory export /backup/mem8-$(date +%Y%m%d).json
```

### Performance Baseline Script

Create performance baselines for monitoring:

```bash
#!/bin/bash
# Save as scripts/admin/performance-baseline.sh

echo "Establishing Mem8 Performance Baseline"
echo "====================================="

# Run comprehensive benchmarks
./scripts/mem8-cli.sh perf bench --bench-type all --iterations 10000 > baseline.txt

# Extract key metrics
echo ""
echo "Baseline Metrics:"
grep "Per operation:" baseline.txt | awk '{print $1, $2, $3}'

# Set up alerts if performance degrades
echo ""
echo "Baseline saved to: baseline.txt"
echo "Use this for comparison in monitoring systems"
```

## Troubleshooting

### Common Issues and Solutions

**Model Not Found**
```bash
$ ./scripts/mem8-cli.sh llm test llama3
🧪 Testing model: llama3
  → Establishing connection...
  ❌ Error: Model not found

Solution: Install the model first
$ ./scripts/mem8-cli.sh llm install llama3
```

**Storage Not Initialized**
```bash
$ ./scripts/mem8-cli.sh status
❌ Error: Storage directory not found: /tmp/mem8_storage

Solution: Create storage or specify different path
$ mkdir -p /tmp/mem8_storage
# OR
$ ./scripts/mem8-cli.sh --storage ~/mem8/storage status
```

**Permission Denied**
```bash
$ ./scripts/mem8-cli.sh memory decay
❌ Error: Permission denied

Solution: Run with appropriate permissions or as admin user
$ sudo ./scripts/mem8-cli.sh memory decay
```

## Conclusion

The Mem8 CLI provides comprehensive control over all aspects of the wave-based memory system. From persona management to performance optimization, it offers the tools needed for advanced system administration while maintaining safety through permission checks and dry-run modes.

For more information, see:
- [CLI Reference Documentation](./CLI.md)
- [Architecture Overview](../ARCHITECTURE.md)
- [Scripts Documentation](../SCRIPTS.md)