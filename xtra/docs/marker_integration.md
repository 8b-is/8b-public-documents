# 📄 Marker-PDF Integration for Mem8

## Overview

Mem8 now supports high-quality document import through integration with [marker-pdf](https://github.com/VikParuchuri/marker), enabling conversion of PDFs, DOCX, PPTX, EPUB, HTML, and images into wave-based memories with temporal processing.

## Supported Formats

### Input Formats
- **PDF** - Digital and scanned documents
- **DOCX/DOC** - Microsoft Word documents  
- **PPTX/PPT** - PowerPoint presentations
- **XLSX/XLS** - Excel spreadsheets
- **EPUB** - E-books
- **HTML** - Web pages
- **Images** - PNG, JPEG, TIFF (with OCR)

### Output Processing
- **Markdown** - Formatted text with equations, tables, and code
- **JSON** - Structured document tree with layout information
- **Temporal Waves** - Natural reading-speed memory formation

## Key Features

### 1. **High-Quality Conversion**
- Preserves document structure (headings, lists, tables)
- Maintains equations in LaTeX format
- Extracts and references images
- Handles multi-column layouts
- OCR for scanned documents

### 2. **Temporal Processing**
Documents unfold into memories at natural reading speeds:
- **Headers**: 2-3 words/second (high importance)
- **Body text**: 4-5 words/second
- **Code/Tables**: 1-2 elements/second
- **Footnotes**: 6-7 words/second (lower importance)

### 3. **Wave Encoding by Content Type**
Different document elements create distinct wave patterns:

| Content Type | Amplitude | Frequency | Purpose |
|--------------|-----------|-----------|---------|
| Section Headers | 0.9 | 500Hz | Navigation anchors |
| Tables | 0.85 | 450Hz | Structured data |
| Equations | 0.85 | 480Hz | Mathematical concepts |
| Code Blocks | 0.75 | 400Hz | Technical content |
| Body Text | 0.6 | 350Hz | Main content |
| Footnotes | 0.5 | 300Hz | Supporting details |

### 4. **LLM Enhancement** (Optional)
- Table structure improvement
- Cross-page table merging
- Inline math formatting
- Form value extraction
- Image descriptions

## Installation

```bash
# Install marker-pdf with full support
pip install marker-pdf[full]

# For GPU acceleration (recommended)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

## Usage

### Command Line

#### Single Document Import
```bash
# Import a PDF
python scripts/import/import_document_marker.py document.pdf --db memories.db

# Import with LLM enhancement
python scripts/import/import_document_marker.py document.pdf --use-llm

# Import specific pages
python scripts/import/import_document_marker.py document.pdf --page-range "0,5-10,20"

# Force OCR on all pages
python scripts/import/import_document_marker.py document.pdf --force-ocr
```

#### Batch Import
```bash
# Import all PDFs in a folder
python scripts/import/import_document_marker.py /path/to/docs --batch

# Import specific file types
python scripts/import/import_document_marker.py /path/to/docs --batch --types pdf,docx,epub
```

### Python API

```python
from mem8.upload.converters.marker_integration import MarkerConverter
from mem8.memory import Mem8
import std::sync::{Arc, RwLock}

# Initialize Mem8
mem8 = Mem8::new(32, 32, "memories.db")
mem8_arc = Arc::new(RwLock::new(mem8))

# Create converter
converter = MarkerConverter::new(mem8_arc)
    .with_llm()  # Optional: use LLM
    .with_json_output()  # Optional: JSON format

# Import document
memory_ids = converter.import_to_mem8(Path::new("document.pdf"))
```

### Rust API

```rust
use mem8::upload::converters::marker_integration::MarkerConverter;
use std::path::Path;

let converter = MarkerConverter::new(mem8_arc);
let memory_ids = converter.import_to_mem8(Path::new("document.pdf"))?;
```

## Processing Pipeline

### 1. Document Analysis
```
PDF/DOCX/etc → Marker → Layout Detection → Block Extraction
```

### 2. Temporal Segmentation
```
Blocks → Semantic Segments → Reading Speed Assignment → Temporal Spacing
```

### 3. Wave Generation
```
Text Segment → Importance Analysis → Wave Parameters → Memory Storage
```

### 4. Cross-References
```
TOC Entries → Page Links → Section Hierarchy → Navigation Waves
```

## Memory Organization

### Table of Contents
- Stored as high-amplitude navigation waves
- Phase encodes page position
- Frequency indicates heading level

### Page Structure
- Each page has unique phase offset
- Vertical position encoded in wave phase
- Reading order preserved

### Content Relationships
- Tables maintain cell relationships
- Equations link to surrounding text
- Images reference their captions

## Advanced Features

### Structured Extraction
Extract specific data using JSON schemas:

```python
from pydantic import BaseModel

class ResearchPaper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    conclusions: List[str]

schema = ResearchPaper.model_json_schema()
data = extractor.extract_with_schema(file_path, schema)
```

### Custom Processing
Override default wave generation:

```rust
impl MarkerConverter {
    fn custom_block_wave(&self, block: &MarkerBlock) -> WavePattern {
        match block.block_type.as_str() {
            "CustomType" => WavePattern::new(0.95, 600.0, 0.0),
            _ => self.create_block_wave(block, 0),
        }
    }
}
```

## Performance

### Speed
- **Single document**: 2-15 seconds (depending on size)
- **Batch processing**: ~120 pages/second on GPU
- **Memory overhead**: ~5GB VRAM per worker

### Accuracy
- **Text extraction**: 95.7% (heuristic score)
- **Table recognition**: 81.6% (90.7% with LLM)
- **Equation formatting**: 85%+ accuracy

## Troubleshooting

### Common Issues

1. **Out of Memory**
   - Reduce worker count for batch processing
   - Split large PDFs into chunks
   - Use CPU mode: `TORCH_DEVICE=cpu`

2. **Poor OCR Quality**
   - Use `--force-ocr` flag
   - Enable `--format-lines` for better formatting
   - Try `--use-llm` for complex documents

3. **Missing Dependencies**
   ```bash
   # Install system dependencies
   sudo apt-get install tesseract-ocr poppler-utils
   ```

4. **Slow Performance**
   - Enable GPU: check `torch.cuda.is_available()`
   - Reduce image extraction: `--disable-image-extraction`
   - Use JSON output for faster processing

## Examples

### Research Paper Import
```bash
# Import with enhanced math and table handling
python scripts/import/import_document_marker.py \
    research_paper.pdf \
    --use-llm \
    --format json \
    --db research.db
```

### Book Chapter Import
```bash
# Import specific chapters with pagination
python scripts/import/import_document_marker.py \
    book.pdf \
    --page-range "50-150" \
    --format markdown \
    --db books.db
```

### Presentation Import
```bash
# Import slides as visual memories
python scripts/import/import_document_marker.py \
    presentation.pptx \
    --db presentations.db
```

## Best Practices

1. **Use LLM for Complex Documents**
   - Financial reports with tables
   - Scientific papers with equations
   - Forms and structured documents

2. **Optimize for Memory Type**
   - Technical docs: Emphasize code blocks
   - Literature: Focus on narrative flow
   - Reference: Prioritize TOC and indices

3. **Temporal Spacing**
   - Allow natural pauses between sections
   - Group related content temporally
   - Preserve document rhythm

4. **Memory Management**
   - Monitor total memory count
   - Use decay for temporary imports
   - Tag memories by source document

## Future Enhancements

- [ ] Real-time document watching
- [ ] Incremental page updates  
- [ ] Custom OCR models
- [ ] Multi-language optimization
- [ ] Collaborative annotation import
- [ ] Version tracking for documents

## Related Documentation

- [Temporal Processing](temporal_processing.md)
- [Wave Patterns](../README.md#wave-patterns)
- [Upload System](upload_system.md)
- [Memory Management](memory_management.md)