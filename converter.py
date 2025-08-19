import os
import ocrmypdf
from pathlib import Path

# Create output directory if it doesn't exist
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

# Function to process a single PDF
def process_pdf(pdf_path, output_dir, language='eng'):
    output_path = output_dir / pdf_path.name
    print(f"Processing: {pdf_path}")
    try:
        # Perform OCR without skipping any pages, even those with existing text
        ocrmypdf.ocr(
            input_file=pdf_path,
            output_file=output_path,
            language=language,
            skip_text=False,  # Process all pages
            force_ocr=True,   # Force OCR on all pages
            optimize=0,       # Disable optimization to preserve original quality
            jobs=1,           # Single-threaded to avoid resource issues
            image_dpi=1039,   # Match max DPI to handle high-resolution images
            quiet=True        # Suppress non-critical warnings
        )
        print(f"Successfully processed: {output_path}")
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")

# Main function to process all PDFs in the current directory
def main():
    current_dir = Path.cwd()
    pdf_files = [f for f in current_dir.glob("*.pdf") if f.is_file()]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process.")
    for pdf_file in pdf_files:
        process_pdf(pdf_file, output_dir)

if __name__ == "__main__":
    main()
