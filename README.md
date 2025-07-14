# MarkItDown Demo & Examples

A comprehensive collection of examples and utilities for Microsoft's MarkItDown document conversion tool. This repository provides practical, ready-to-use scripts that demonstrate how to convert various file formats to Markdown for AI/LLM workflows.

## 🚀 What's MarkItDown?

MarkItDown is Microsoft's open-source Python utility that converts documents, images, and audio files into clean, structured Markdown. It's specifically designed for AI workflows and has gained 50,000+ GitHub stars for solving a real problem in document processing.

**Supported formats:** PDF, DOCX, PPTX, XLSX, HTML, images, audio, CSV, JSON, XML, and more.

## 📁 Repository Contents

| Script | Description | Use Case |
|--------|-------------|----------|
| `test_markitdown.py` | Basic functionality test | Quick verification that everything works |
| `document_processor.py` | Advanced document processing with reporting | Process multiple files with detailed analytics |
| `batch_processor.py` | Command-line batch converter | Convert entire directories of documents |
| `multimodal_test.py` | Image and audio processing examples | Demonstrate AI-powered content extraction |

## 🛠️ Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/nirajshiwantha/MarkItDownDemo.git
cd markitdown-demo

# Create virtual environment
python -m venv markitdown-env

# Activate it
source markitdown-env/bin/activate  # Mac/Linux
# markitdown-env\Scripts\activate   # Windows
```

### 2. Install Dependencies

```bash
# Install MarkItDown with all features
pip install markitdown[all]

# Verify installation
python -c "from markitdown import MarkItDown; print('✅ MarkItDown ready!')"
```

### 3. Run Your First Test

```bash
python test_markitdown.py
```

This creates a test HTML file, converts it to Markdown, and shows you the results.

## 📖 Usage Examples

### Basic Document Conversion

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("your_document.pdf")
print(result.text_content)
```

### Batch Processing

```bash
# Convert all documents in a directory
python batch_processor.py ./documents --output ./markdown_output

# Convert specific file types only
python batch_processor.py ./docs --types .pdf .docx --output ./converted
```

### Advanced Processing with Reporting

```python
from document_processor import DocumentProcessor

processor = DocumentProcessor()
results = processor.process_directory("./my_documents")
report = processor.generate_report()
```

### Image Description (Requires OpenAI API)

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI(api_key="your-api-key")
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

result = md.convert("screenshot.png")
print(result.text_content)  # AI-generated description
```

## 🔧 Script Details

### `test_markitdown.py`
- **Purpose**: Verify basic functionality
- **What it does**: Creates test HTML, converts to Markdown, shows before/after
- **Run**: `python test_markitdown.py`

### `document_processor.py`
- **Purpose**: Production-ready document processing
- **Features**: 
  - Batch processing with error handling
  - Detailed conversion reports (JSON)
  - File organization and metadata tracking
  - Progress monitoring
- **Run**: `python document_processor.py`

### `batch_processor.py`
- **Purpose**: Command-line batch conversion tool
- **Features**:
  - Process entire directories
  - Filter by file types
  - Command-line arguments
  - Progress tracking
- **Usage**: `python batch_processor.py <input_dir> [options]`

### `multimodal_test.py`
- **Purpose**: Demonstrate advanced features
- **Features**:
  - OpenAI integration setup
  - Image description examples
  - Audio transcription info
- **Note**: Requires API keys for full functionality

## 🎯 Common Use Cases

### 1. Building RAG Systems
Convert your company docs to feed into AI chatbots:
```bash
python batch_processor.py ./company_docs --output ./rag_content
```

### 2. Document Migration
Move from legacy formats to modern Markdown:
```python
processor = DocumentProcessor()
processor.process_directory("./legacy_docs", "./modernized_docs")
```

### 3. Content Analysis Pipeline
Process mixed file types for AI analysis:
```python
# The document_processor handles mixed formats automatically
results = processor.process_directory("./mixed_content")
```

### 4. Meeting Notes Automation
Convert recorded meetings to searchable text:
```python
result = md.convert("meeting_recording.mp3")
# Gets transcribed, structured text
```

## ⚙️ Configuration Options

### Basic Setup
```python
md = MarkItDown()  # Default settings
```

### With Azure Document Intelligence
```python
md = MarkItDown(docintel_endpoint="your_azure_endpoint")
```

### With OpenAI for Images
```python
from openai import OpenAI
client = OpenAI(api_key="your_key")
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
```

### With Custom Plugins
```python
md = MarkItDown(enable_plugins=True)
```

## 🐛 Troubleshooting

### Common Issues

**"Module not found"**
```bash
# Ensure virtual environment is activated
source markitdown-env/bin/activate
pip install markitdown[all]
```

**PDF conversion fails**
```bash
# Install additional PDF support
pip install pdfplumber pymupdf
```

**File permission errors**
- Close files in other applications
- Check file permissions
- Try copying files to a different location

**Memory issues with large files**
- Process files individually instead of in batches
- Use the command-line tool for large documents

### Getting Help

1. Check the [MarkItDown GitHub Issues](https://github.com/microsoft/markitdown/issues)
2. Review the error messages in the conversion reports
3. Test with smaller files first to isolate issues

## 📊 Output Examples

### Conversion Report Sample
```json
{
  "timestamp": "2025-07-14T10:30:00",
  "total_files": 15,
  "successful_conversions": 13,
  "failed_conversions": 2,
  "total_content_length": 45620,
  "results": [...]
}
```

### Markdown Output Quality
- ✅ Preserves headings, lists, tables
- ✅ Maintains document structure
- ✅ Handles images and links
- ✅ Optimized for LLM consumption

## 🔗 Resources

- **MarkItDown GitHub**: [microsoft/markitdown](https://github.com/microsoft/markitdown)
- **Official Docs**: Check the GitHub README for latest features
- **OpenAI API**: [platform.openai.com](https://platform.openai.com) (for image descriptions)
- **Azure Document Intelligence**: [Azure Form Recognizer](https://azure.microsoft.com/services/form-recognizer/) (for advanced PDF processing)

---

**Built with ❤️ to help developers get the most out of Microsoft MarkItDown**

*Last updated: July 2025*
