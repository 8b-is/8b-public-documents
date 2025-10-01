# Tmux Context Watcher for Mem8

Automatically capture terminal context and build memories from your tmux sessions.

## Overview

The Tmux Context Watcher monitors your terminal activity and automatically creates memories in mem8 when it detects important patterns like errors, commands, questions, or significant output.

## Quick Start

```bash
# Start a tmux session
tmux new -s mem8

# Inside tmux, run the watcher
./scripts/start_tmux_watcher.sh

# In another terminal, view captured memories
cargo run --example tmux_memory_importer
```

## Available Watchers

### 1. Python Watcher (Batch Mode)
Captures context and saves to JSON files for later import.

```bash
python3 scripts/tmux_context_watcher.py [interval] [context_lines]
```

Features:
- Captures every 30 seconds by default
- Extracts commands, files, errors, and URLs
- Saves to `/tmp/mem8_tmux_*.json`
- Batch import with `tmux_memory_importer`

### 2. Rust Watcher (Real-time)
Directly creates memories in mem8 as it captures.

```bash
cargo run --example tmux_realtime_watcher -- [interval_seconds]
```

Features:
- Real-time memory creation
- No intermediate files
- Live statistics display
- Automatic deduplication

## Pattern Detection

The watcher detects and prioritizes:

| Pattern | Importance | Examples |
|---------|------------|----------|
| Critical | 14-15 | error, crash, fatal, failed |
| Important | 11-12 | warning, bug, success, complete |
| Development | 9-10 | git, cargo, npm, make, docker |
| Questions | 8-9 | ?, how, what, why |
| Output | 7-8 | Compiling, Building, Running |

## Memory Structure

Each captured memory includes:
- **Context**: Last 20 meaningful lines of terminal output
- **Importance**: 0-15 scale based on detected patterns
- **Category**: Type of activity (critical, development, etc.)
- **Metadata**: Extracted commands, files, errors, URLs
- **Emotional valence**: Derived from content (errors = negative, success = positive)

## Use Cases

1. **Development Sessions**: Automatically capture compile errors, test results, git operations
2. **Debugging**: Track error messages and their context
3. **Learning**: Capture questions and their answers
4. **Command History**: Enhanced history with full context

## Example Session

```bash
$ tmux new -s coding
$ ./scripts/start_tmux_watcher.sh

# In your tmux session, work normally:
$ cargo build
   Compiling mem8 v0.1.0
   error[E0599]: no method named `foo` found
   
$ git commit -m "Fix wave compression"
[master abc123] Fix wave compression

# The watcher captures:
[14:32:15] 📝 Captured critical context (importance: 14)
   Commands: cargo build
   Errors: error[E0599]: no method named `foo` found
   
[14:33:42] 📝 Captured development context (importance: 10)
   Commands: git commit -m "Fix wave compression"
```

## Tips

- Run inside tmux for best results
- Adjust capture interval based on your workflow (5s for debugging, 60s for general work)
- Use `tmux_memory_importer` to bulk import at end of session
- Real-time watcher better for active debugging
- Python watcher better for long sessions

## Integration with Mem8

Captured memories become part of your mem8 wave-based memory system:
- Searchable with wave pattern matching
- Subject to temporal decay
- Can be cross-referenced with other memory types
- Compressed to ~32 bytes per memory

The more you use it, the better mem8 becomes at understanding your development patterns and retrieving relevant context when you need it.