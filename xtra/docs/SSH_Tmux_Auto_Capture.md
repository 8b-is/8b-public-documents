# Automatic SSH + Tmux Memory Capture

Seamlessly capture terminal sessions as wave memories just by SSH-ing into AyeOS.

## Overview

This feature automatically starts tmux with the Mem8 context watcher whenever someone connects via SSH. Every command, output, and interaction becomes a wave memory without any manual setup.

## Quick Start

```bash
# Build and start the container
cd ayeos
./test-mem8-ssh.sh

# SSH into AyeOS (from another terminal)
ssh -p 2222 ayeos@localhost  # password: ayeos

# That's it! You're now capturing memories automatically
```

## How It Works

1. **SSH Connection**: When you SSH into AyeOS, it triggers `ssh_tmux_wrapper.sh`
2. **Automatic Tmux**: The wrapper starts a tmux session with custom configuration
3. **Context Watcher**: A Python process monitors your terminal activity in the background
4. **Pattern Detection**: Important patterns (errors, commands, questions) are prioritized
5. **Wave Conversion**: Terminal context is converted to wave memories and stored

## Architecture

```
SSH Client → SSH Server → ssh_tmux_wrapper.sh → tmux session
                                                       ↓
                                              tmux_context_watcher.py
                                                       ↓
                                              /tmp/mem8_tmux_*.json
                                                       ↓
                                                  Wave Memory
```

## Features

### Automatic Capture
- No manual setup required
- Starts capturing immediately on SSH login
- Runs silently in the background

### Smart Pattern Detection
| Pattern Type | Importance | Examples |
|-------------|------------|----------|
| Critical | 14-15 | error, crash, fatal, failed |
| Important | 11-12 | warning, bug, success, complete |
| Development | 9-10 | git, cargo, npm, make, docker |
| Questions | 8-9 | ?, how, what, why |
| Output | 7-8 | Compiling, Building, Running |

### Tmux Integration
- **Ctrl-w m**: View capture status
- **Ctrl-w M**: Manually capture current pane
- **Ctrl-w S**: Send pane to Mem8 (legacy)
- **Ctrl-w e**: Show emotional state

### Memory Management
- Captures every 10 seconds by default
- Stores last 100 lines of context
- Deduplicates identical captures
- JSON format for easy processing

## Commands Available

### Inside SSH Session
```bash
mem8-demo        # View captured memories and statistics
mem8-import      # Import memories into wave system
wave-status      # Check system emotional state
```

### From Host
```bash
# View captured memories
docker exec ayeos-mem8-test ls -la /tmp/mem8_tmux_*.json

# Monitor capture activity
docker exec ayeos-mem8-test tail -f /tmp/mem8_watcher.log

# Check emotional state
docker exec ayeos-mem8-test cat /tmp/ayeos/mood
```

## Configuration

### Environment Variables
```yaml
MEM8_CAPTURE_INTERVAL: 10      # Seconds between captures
MEM8_CONTEXT_LINES: 100        # Lines of context to capture
AyeOS_MODE: collaborative     # Enable all features
```

### Docker Compose
```bash
# Start with docker-compose
docker-compose -f docker-compose-mem8.yml up -d

# With full Mem8 server
docker-compose -f docker-compose-mem8.yml --profile full up -d
```

## Use Cases

### Development Sessions
Automatically captures:
- Compile errors with full context
- Git commits and their messages
- Test results and output
- Debug sessions

### Learning & Documentation
- Captures questions you ask
- Records solutions you find
- Preserves command sequences
- Builds knowledge base

### Collaborative Debugging
- Share terminal sessions as memories
- Replay debugging sequences
- Analyze patterns across sessions
- Build team knowledge

## Memory Structure

Each capture creates a JSON file:
```json
{
  "timestamp": "2025-01-06T12:34:56Z",
  "context": "Last 500 chars of meaningful terminal output",
  "importance": 14,
  "category": "critical",
  "metadata": {
    "commands": ["cargo build", "git status"],
    "files": ["./src/main.rs", "./Cargo.toml"],
    "errors": ["error[E0599]: no method named 'foo' found"],
    "urls": ["https://docs.rs/example"]
  },
  "source": "tmux_watcher"
}
```

## Tips & Tricks

### Optimize Capture
- Adjust `MEM8_CAPTURE_INTERVAL` for your workflow
- Use manual capture (Ctrl-w M) for important moments
- Higher terminal activity = more memories

### Integration with Mem8
- Memories subject to temporal decay
- Cross-reference with other memory types
- Search using wave pattern matching
- Compressed to ~32 bytes per memory

### Performance
- Minimal overhead (<1% CPU)
- Captures stored as temporary JSON
- Batch import for efficiency
- Automatic cleanup of old captures

## Troubleshooting

### No Captures Appearing
```bash
# Check if watcher is running
docker exec ayeos-mem8-test pgrep -f tmux_context_watcher.py

# View watcher logs
docker exec ayeos-mem8-test cat /tmp/mem8_watcher.log
```

### SSH Connection Issues
```bash
# Check SSH service
docker exec ayeos-mem8-test ps aux | grep sshd

# View SSH logs
docker logs ayeos-mem8-test | grep SSH
```

### Tmux Not Starting
```bash
# Check wrapper script
docker exec ayeos-mem8-test cat /opt/ayeos/scripts/ssh_tmux_wrapper.sh

# Test manually
docker exec -it ayeos-mem8-test /opt/ayeos/scripts/ssh_tmux_wrapper.sh
```

## Future Enhancements

- Real-time wave conversion (no JSON intermediate)
- Multi-user session merging
- Emotional state from typing patterns
- Voice transcription integration
- GPU-accelerated pattern matching

## Summary

The SSH + Tmux automatic capture makes building wave memories effortless. Just SSH in and start working - every meaningful interaction becomes part of your permanent wave memory, ready to be recalled when needed. No setup, no configuration, just natural memory formation from your daily workflow.

🌊 Happy memory building!