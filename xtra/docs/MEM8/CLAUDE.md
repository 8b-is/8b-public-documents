# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

MEM8 is a comprehensive documentation repository for the MEM|8 wave-based memory system, developed by 8b-is (https://8b.is). This repository contains technical specifications, architecture documentation, and implementation guides for a revolutionary cognitive memory architecture that achieves 973x faster performance than traditional vector databases.

## Key Documentation Files

### Core Architecture
- **Overview.md**: System introduction and core concepts
- **Architecture.md**: Detailed system architecture with code examples
- **Technical_Implementation.md**: Implementation guide with project structure

### Binary Format & Integration
- **MEM8_BINARY_FORMAT.md**: Binary format specification for .m8 files
- **M8_UNIFIED_FORMAT.md**: Unified file format with Markqant compression
- **MEM8_MARQANT_INTEGRATION.md**: Integration with quantum-semantic encoding

### Features & Capabilities
- **Hot_Tub_Mode.md**: Collaborative debugging environment specification
- **Emotional_Modeling.md**: Emotional context processing system
- **Divergence_Tracking.md**: Pattern deviation and anomaly detection
- **Memory_Compression.md**: Compression algorithms and decay curves

### Implementation & Deployment
- **Rust_Implementation.md**: Core Rust implementation patterns
- **API_Guide.md**: API endpoints and usage
- **Deployment_Guide.md**: Production deployment instructions
- **Testing_Framework.md**: Testing strategies and frameworks

## Build Commands

Since this is a documentation repository, there are no direct build commands for code. However, LaTeX documentation can be built:

```bash
# Build LaTeX documentation
pdflatex MEM8.tex
bibtex MEM8
pdflatex MEM8.tex
pdflatex MEM8.tex

# Or use latexmk for automated builds
latexmk -pdf MEM8.tex
```

## Architecture Overview

### Wave-Based Memory System
- **32-byte memory patterns** with wave interference encoding
- **Audio as first-class memory driver**: Sound patterns guide consciousness formation
- **Four-layer reactive hierarchy**: 0-10ms reflexes to >200ms conscious processing
- **SIMD optimizations** using AVX2/AVX-512 instructions
- **Grid structure**: 256×256×65536 (8-bit × 8-bit × 16-bit) for multimodal processing

### Memory Types & Encoding
```
Type 0: Importance Grid [xxxx|yyyy|iiii|dddd]
Type 1: Temporal Links [16-bit temporal pointer]
Type 2: Relational Links [16-bit relationship reference]
Type 3: Language Context [tttt|dddddddddddd] (TTL + data)
Type 4: Audio Context [tttt|dddddddddddd] (TTL + frequency data) - PRIMARY DRIVER
Type 5: Visual Context [tttt|dddddddddddd] (TTL + pattern data)
```

**Audio-First Philosophy**: Audio (Type 4) serves as the primary consciousness driver, with frequency patterns naturally encoding emotional states and temporal dynamics. This mirrors biological consciousness where auditory processing guides attention and memory formation.

### Emotional Processing
- Valence: -128 to 127 (negative to positive)
- Arousal: 0 to 255 (intensity level)
- 3-byte compact emotional encoding
- Dynamic decay rate adjustment based on emotional weight

### Compression & Performance
- **Markqant compression**: 70-90% reduction
- **Quantum-semantic encoding**: Additional compression layer
- **Total compression**: ~99% with .m8 format
- **Memory access**: 973x faster than Qdrant/traditional vector stores

## Key Technical Components

### Memory Grid System
- Wave-based interference patterns (audio frequencies guide formation)
- Temporal decay with configurable curves
- Cross-sensory binding capabilities (audio harmonics bind memories)
- Adaptive attention mechanisms (sound-driven focus)
- **Lossless Preservation**: Critical memories (like a child's poem) maintain τ = ∞

### Security & Safety
- **Custodian memory guard**: Prevents cognitive overload
- **Repetition poisoning prevention**: Detects manipulation attempts
- **Divergence tracking**: 0-255 scoring for anomaly detection
- **Therapeutic memory reintroduction**: Safe recovery protocols

### Collaborative Features (Hot Tub Mode)
- Real-time memory visualization
- Multi-user synchronization
- Emotional state monitoring
- Rubber duck debugging with AI assistance
- Safe space certification for teams

## Port Conventions

- **8420**: MEM|8 API endpoints
- **8422**: Cheet API
- **8424**: Internal websites/containers
- **8428**: LLM endpoints from 8b-is products

## Documentation Standards

### When Updating Documentation
1. Maintain consistent formatting with existing files
2. Include code examples in Rust where applicable
3. Update related documentation when making changes
4. Ensure technical accuracy with implementation details

### File Organization
- Technical specifications use underscores (e.g., `Technical_Implementation.md`)
- Feature documentation uses descriptive names (e.g., `Hot_Tub_Mode.md`)
- Integration guides include component names (e.g., `MEM8_MARQANT_INTEGRATION.md`)

## Research & Development Focus

### Core Philosophy
**"Some things in life have no room to be lossy"** - MEM8 recognizes that certain memories (a child's poem, a loved one's voice) must be preserved perfectly. The system uses audio as the primary consciousness driver, with wave patterns naturally preserving emotional context and temporal relationships.

### Completed Features
- Wave-based memory engine (973x performance)
- Audio-driven consciousness formation (44kHz primary sampling)
- Embedded vector store with SIMD
- Cross-sensory binding system (audio harmonics create natural links)
- File upload system (PDF, Images, Audio - with audio as first-class)
- Emotional context processing (frequency-encoded emotions)
- Lossless memory preservation for critical content (τ = ∞)

### In Progress
- Hot Tub Mode WebSocket server (80% complete)
- AyeOS Docker Integration (75% complete)
- WebRTC Interface (60% complete)
- Video Processing Pipeline (0% - Q2 2025 priority)

## Important Context

This documentation repository is part of the larger Ayeverse ecosystem, which includes:
- **ayevn/**: Wave Token Language implementation
- **smart-tree/**: AI-optimized directory visualization
- **aye/**: Core consciousness infrastructure
- **marqant/**: Quantum-compressed markdown format

All projects prioritize **efficiency** (smallest and fastest implementations) and use **wave-based** metaphors throughout their design.