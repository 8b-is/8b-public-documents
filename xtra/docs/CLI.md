# Mem8 CLI Documentation

## Overview

The Mem8 CLI (`mem8-cli`) is a comprehensive maintenance tool for advanced system administration. It provides direct access to all core Mem8 subsystems including persona management, memory operations, performance monitoring, and LLM configuration.

**⚠️ WARNING**: This is a maintenance tool for advanced users only. Improper use may affect system performance or data integrity.

## Installation

```bash
# Build the CLI
cargo build --release --bin mem8-cli

# Or use the wrapper script
./scripts/mem8-cli.sh --help
```

## Global Options

- `-s, --storage <PATH>` - Path to Mem8 storage directory (default: `/tmp/mem8_storage`)
- `-v, --verbose` - Enable verbose output
- `-h, --help` - Print help information

## Commands

### System Status

```bash
mem8-cli status [--detailed]
```

Shows overall system health, memory statistics, and performance metrics.

### Persona Management

#### List Personas
```bash
mem8-cli persona list
```

#### Show Persona Status
```bash
mem8-cli persona status <NAME>
```

#### Create New Persona
```bash
mem8-cli persona create <NAME> [OPTIONS]
  --prompt <PROMPT>     Initial personality prompt
  --traits <TRAITS>     Comma-separated traits (e.g., "curious,technical,empathetic")
```

#### Analyze Persona Evolution
```bash
mem8-cli persona evolution <NAME> [--hours <N>]
```

### Memory Operations

#### Memory Statistics
```bash
mem8-cli memory stats [--breakdown]
```

#### Search Memories
```bash
mem8-cli memory search <QUERY> [OPTIONS]
  --limit <N>           Maximum results (default: 10)
  --persona <NAME>      Filter by persona
```

#### Export Memories
```bash
mem8-cli memory export <OUTPUT_FILE> [OPTIONS]
  --format <FORMAT>     Export format: json, csv, wave (default: json)
  --since <DATE>        Filter by date (ISO format)
```

#### Analyze Memory Patterns
```bash
mem8-cli memory patterns [--window <HOURS>]
```

#### Trigger Decay Cycle
```bash
mem8-cli memory decay [--dry-run]
```

### Performance Monitoring

#### Run Benchmarks
```bash
mem8-cli perf bench [OPTIONS]
  --type <TYPE>         Benchmark type: insert, search, decay, all (default: all)
  --iterations <N>      Number of iterations (default: 1000)
```

#### Real-time Monitor
```bash
mem8-cli perf monitor [--interval <SECONDS>]
```

#### Performance History
```bash
mem8-cli perf history [--hours <N>]
```

### LLM Configuration

#### List Models
```bash
mem8-cli llm list
```

#### Add Model
```bash
mem8-cli llm add <PROVIDER> <MODEL> [OPTIONS]
  --endpoint <URL>      Custom API endpoint
  --key <API_KEY>       API key (if required)
```

#### Test Model
```bash
mem8-cli llm test <MODEL>
```

#### Set Default Model
```bash
mem8-cli llm default <MODEL>
```

#### Install Ollama Model
```bash
mem8-cli llm install <MODEL>
```

### API Management

#### List Endpoints
```bash
mem8-cli api list
```

#### Configure Endpoint
```bash
mem8-cli api config <NAME> [OPTIONS]
  --port <PORT>         Port number
  --enable <BOOL>       Enable/disable endpoint
```

#### API Statistics
```bash
mem8-cli api stats [--detailed]
```

### Seed Memory Import

```bash
mem8-cli seed <PATH> [--persona <NAME>]
```

Import foundational memories from files to bootstrap a new persona.

## Common Use Cases

### Creating a New Persona with Seed Memories

```bash
# Create persona
mem8-cli persona create "Alex" \
  --traits "analytical,curious,helpful" \
  --prompt "A technical assistant focused on deep understanding"

# Import seed memories
mem8-cli seed /path/to/knowledge/base --persona Alex

# Check persona status
mem8-cli persona status Alex
```

### Performance Optimization

```bash
# Run comprehensive benchmark
mem8-cli perf bench --type all --iterations 10000

# Monitor in real-time
mem8-cli perf monitor --interval 1

# Check for decay candidates
mem8-cli memory decay --dry-run
```

### Model Management

```bash
# List available models
mem8-cli llm list

# Install new Ollama model
mem8-cli llm install llama2:13b

# Test the model
mem8-cli llm test llama2:13b

# Set as default
mem8-cli llm default llama2:13b
```

## Advanced Features

### Batch Operations

The CLI supports command chaining for batch operations:

```bash
# Create persona and immediately import memories
mem8-cli persona create "Research" --traits "analytical,methodical" && \
mem8-cli seed ~/research/papers --persona Research
```

### Output Formats

Many commands support different output formats:

```bash
# Export as JSON (default)
mem8-cli memory export memories.json

# Export as CSV
mem8-cli memory export memories.csv --format csv

# Export raw wave patterns
mem8-cli memory export waves.dat --format wave
```

### Performance Tuning

The CLI provides detailed performance metrics:

```bash
# Get baseline performance
mem8-cli perf bench --type insert --iterations 10000 > baseline.txt

# Make system changes...

# Compare performance
mem8-cli perf bench --type insert --iterations 10000 > optimized.txt
diff baseline.txt optimized.txt
```

## Security Considerations

1. **Permission Checks**: The CLI warns non-admin users before executing
2. **Dry Run Mode**: Destructive operations support `--dry-run`
3. **Audit Logging**: All CLI operations are logged for security auditing

## Troubleshooting

### Common Issues

1. **"Permission denied"**
   - Run with appropriate user permissions
   - Check storage directory ownership

2. **"Model not found"**
   - Ensure Ollama is running: `ollama serve`
   - Check model is installed: `ollama list`

3. **"Storage not initialized"**
   - Verify storage path exists
   - Check disk space availability

### Debug Mode

Enable verbose output for troubleshooting:

```bash
mem8-cli --verbose status --detailed
```

## Integration with Other Tools

The CLI can be integrated with system monitoring tools:

```bash
# Prometheus metrics export
mem8-cli memory stats --format prometheus > /var/lib/prometheus/mem8.prom

# Cron job for regular maintenance
0 3 * * * /path/to/mem8-cli memory decay >> /var/log/mem8-maintenance.log
```

## Best Practices

1. **Regular Maintenance**: Run decay cycles during low-usage periods
2. **Monitor Performance**: Set up alerts for degraded performance
3. **Backup Before Major Changes**: Export memories before persona modifications
4. **Test Models**: Always test new models before setting as default
5. **Use Dry Run**: Test destructive operations with `--dry-run` first

## Examples Repository

Find more examples in `/scripts/admin/`:
- `persona-create.sh` - Quick persona creation
- `performance-baseline.sh` - Establish performance baselines
- `memory-maintenance.sh` - Automated memory maintenance