# PDF OCR Converter

A Python tool to automatically convert non-copyable PDF files (containing text as images) into searchable and copyable PDFs using Optical Character Recognition (OCR).

## 📖 Overview

This tool addresses a common problem faced by students: teacher-uploaded PDFs containing text as images that cannot be copied or searched. The script automatically processes all PDF files in the current directory and creates OCR-enhanced versions with searchable text layers while preserving the original layout and images.

## ✨ Features

- **Batch Processing**: Automatically processes all PDF files in the script's directory
- **OCR Enhancement**: Adds searchable text layers to image-based text using Tesseract OCR
- **Layout Preservation**: Maintains original document formatting and images
- **High-Resolution Support**: Handles high-DPI images (up to 1039 DPI)
- **Error Handling**: Continues processing even if individual files fail
- **Organized Output**: Saves all processed files to an `output` folder

## 🔧 Prerequisites

### System Requirements
- Python 3.6 or higher
- Tesseract OCR engine installed system-wide

### Installation

1. **Install Tesseract OCR**:
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt install tesseract-ocr
   ```
   
   **macOS (using Homebrew):**
   ```bash
   brew install tesseract
   ```
   
   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Add Tesseract to your system PATH

2. **Install Python Dependencies**:
   ```bash
   pip install ocrmypdf
   ```

3. **Verify Installation**:
   ```bash
   tesseract --version
   ```

## 📁 File Structure

```
your-project-folder/
├── ocr_pdf.py          # Main script
├── document1.pdf       # Input PDF files
├── document2.pdf
├── lecture_notes.pdf
└── output/             # Created automatically
    ├── document1.pdf   # OCR-enhanced versions
    ├── document2.pdf
    └── lecture_notes.pdf
```

## 🚀 How to Use

1. **Place the Script**: Put `ocr_pdf.py` in the folder containing your PDF files

2. **Run the Script**:
   ```bash
   python ocr_pdf.py
   ```

3. **Wait for Processing**: The script will:
   - Scan for all `.pdf` files in the current directory
   - Create an `output` folder if it doesn't exist
   - Process each PDF with OCR
   - Save enhanced versions to the `output` folder

4. **Access Results**: Find your OCR-enhanced PDFs in the `output` folder

## 📊 Example Output

```
Found 3 PDF file(s) to process.
Processing: /path/to/lecture_notes.pdf
Successfully processed: output/lecture_notes.pdf
Processing: /path/to/assignment.pdf
Successfully processed: output/assignment.pdf
Processing: /path/to/slides.pdf
Successfully processed: output/slides.pdf
```

## ⚙️ Configuration Options

You can modify the script to customize behavior:

- **Language**: Change `language='eng'` to other languages (e.g., `'fra'`, `'deu'`, `'spa'`)
- **DPI Settings**: Adjust `image_dpi=1039` for different image quality needs
- **Optimization**: Change `optimize=0` to `optimize=1` for smaller file sizes

## 🔍 Troubleshooting

### Common Issues

1. **"No PDF files found"**
   - Ensure PDF files are in the same directory as the script
   - Check file extensions (script looks for `.pdf`)

2. **Tesseract not found**
   - Verify Tesseract installation: `tesseract --version`
   - Ensure Tesseract is in your system PATH

3. **High DPI Warnings**
   - These are normal for high-resolution PDFs
   - Output quality should not be affected

4. **Processing Errors**
   - Check if PDF files are corrupted or password-protected
   - Ensure sufficient disk space for output files

### Performance Tips

- **Free up memory** before processing large batches
- **Close other applications** to allocate more resources to OCR
- **Process smaller batches** if you encounter memory issues

## 🎯 Use Cases

- **Student Notes**: Convert lecture slides with image-based text
- **Scanned Documents**: Make old documents searchable
- **Mixed Content PDFs**: Handle documents with both text and images
- **Batch Conversion**: Process multiple files automatically

## ⚠️ Important Notes

- **Processing Time**: OCR is CPU-intensive; large files may take several minutes
- **File Size**: Output files may be larger due to additional text layers
- **Original Files**: Your original PDFs remain unchanged
- **Quality**: OCR accuracy depends on image quality and text clarity

## 📝 License

This project is open source. Feel free to modify and distribute according to your needs.

## 🤝 Contributing

Found a bug or want to add features? Feel free to submit issues or pull requests!

---

**Happy studying!** 📚✨
