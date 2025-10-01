# Mem8 API Migration Guide

This guide helps update old examples to work with the current Mem8 API.

## Major API Changes

### 1. Removed Classes/Modules

The following have been removed or refactored:
- `QdrantEmulator` - No longer exposed publicly
- `Memory` struct - Use wave patterns directly
- `Importance` enum - Use u8 values (0-255)
- `SENSE_*` constants moved from `memory` to `core`
- `SimilarityMetric` - No longer needed
- `UploadedFile` - Removed from public API

### 2. Method Name Changes

#### Storage Methods
```rust
// OLD
mem8.store(memory)?;

// NEW - Use specific storage methods:
mem8.store_context(binding_id, wave_pattern, sensory_type)?;
mem8.store_audio(wave_pattern)?;
mem8.store_visual(wave_pattern)?;
mem8.store_language("text", importance)?;
mem8.store_language_with_timestamp("text", importance, timestamp)?;
```

#### Retrieval Methods
```rust
// OLD
mem8.retrieve(memory_id)?;

// NEW
mem8.retrieve_context(memory_id)?;
// Returns Option<(WavePattern, EmotionalContext)>
```

#### Search Methods
```rust
// OLD
mem8.search(query, limit)?;
mem8.search_similar(query, limit)?;

// NEW - Search is done through the internal emulator
// Most examples should use specific retrieve methods instead
```

#### Statistics Methods
```rust
// OLD
mem8.memory_count();
mem8.get_compression_ratio();
mem8.get_emulator_stats();

// NEW
mem8.get_stats(); // Returns MemorySystemStats
// Fields: total_memories, active_patterns, grid_utilization, average_decay
```

#### Decay Methods
```rust
// OLD
mem8.apply_decay()?;
mem8.apply_temporal_decay(duration)?;

// NEW
mem8.apply_memory_decay(memory_id)?; // Apply decay to specific memory
// Returns bool indicating if memory was found
```

### 3. Import Changes

```rust
// OLD
use mem8::{
    memory::{Memory, Importance, SENSE_LANGUAGE, SENSE_VISUAL, SENSE_AUDIO},
    qdrant::{QdrantEmulator, SimilarityMetric},
    // ...
};

// NEW
use mem8::{
    core::{WavePattern, EmotionalContext, SENSE_LANGUAGE, SENSE_VISUAL, SENSE_AUDIO},
    memory::Mem8,
    // ...
};
```

### 4. FileUploader Changes

```rust
// OLD
let uploader = FileUploader::new();

// NEW - FileUploader now requires a Mem8 instance
let mem8 = Mem8::new(256, 256, "storage.db")?;
let mut uploader = FileUploader::new(mem8);

// Upload is now async
let result = uploader.upload_file(&path).await?;
```

### 5. Missing Methods

The following methods no longer exist:
- `mem8.new_with_emulator()` - Use `Mem8::new()` or `Mem8::new_default()`
- `uploader.create_waves_from_upload()` - Waves are created internally during upload

### 6. Async/Await Requirements

File upload operations are now async:

```rust
// Wrap in tokio runtime if in sync context
let rt = tokio::runtime::Runtime::new()?;
rt.block_on(async {
    let result = uploader.upload_file(&path).await?;
    Ok::<_, anyhow::Error>(result)
})?;
```

### 7. Result Type Changes

```rust
// OLD
fn main() -> Result<()>

// NEW - Specify error type
fn main() -> Result<(), Box<dyn std::error::Error>>
// OR
fn main() -> anyhow::Result<()>
```

## Example Migration

### Before:
```rust
use mem8::{
    memory::{Mem8, Memory, Importance, SENSE_LANGUAGE},
    qdrant::QdrantEmulator,
};

let emulator = QdrantEmulator::new("storage.db")?;
let mut mem8 = Mem8::new_with_emulator()?;

let memory = Memory {
    content: "Hello world".to_string(),
    importance: Importance::High,
    // ...
};

let id = mem8.store(memory)?;
let retrieved = mem8.retrieve(id)?;
let count = mem8.memory_count();
```

### After:
```rust
use mem8::{
    core::{WavePattern, SENSE_LANGUAGE},
    memory::Mem8,
};

let mut mem8 = Mem8::new(256, 256, "storage.db")?;

// Store text as language memory
let id = mem8.store_language("Hello world", 200)?; // importance as u8

// Retrieve
if let Some((wave, emotional)) = mem8.retrieve_context(id)? {
    // Use wave and emotional context
}

// Get stats
let stats = mem8.get_stats();
let count = stats.total_memories;
```

## Fixing Common Errors

### Error: "no function or associated item named `from_compressed`"
The `WavePattern::from_compressed()` method doesn't exist. Use the constructor methods:
- `WavePattern::new(amplitude, frequency, phase)`
- `WavePattern::from_data(&[u8])`
- `WavePattern::from_text(&str)`

### Error: "expected `&Path`, found `PathBuf`"
Use a reference: `uploader.upload_file(&path)` instead of `uploader.upload_file(path)`

### Error: "expected future, found `Result<_, _>`"
The method is async. Either:
1. Use `.await` if in async context
2. Wrap in `tokio::runtime::Runtime::new()?.block_on(async { ... })`

### Error: Missing dependencies
Add to Cargo.toml:
- `indicatif` for progress bars
- `axum` for web servers (with appropriate features)

## Recommended Approach

1. **Update imports** to use the new module structure
2. **Replace generic store/retrieve** with specific methods
3. **Handle async operations** properly
4. **Use get_stats()** for statistics instead of individual methods
5. **Remove references** to QdrantEmulator in application code