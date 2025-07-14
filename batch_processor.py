import os
import sys
from markitdown import MarkItDown
from pathlib import Path
import argparse

def batch_convert(input_dir, output_dir="converted_markdown", file_types=None):
    """Convert all supported files in a directory to Markdown"""
    
    if file_types is None:
        file_types = ['.pdf', '.docx', '.pptx', '.xlsx', '.html', '.htm', '.txt', '.csv']
    
    md = MarkItDown()
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Find all files
    input_path = Path(input_dir)
    files_to_process = []
    
    for file_type in file_types:
        files_to_process.extend(input_path.glob(f"**/*{file_type}"))
    
    print(f"Found {len(files_to_process)} files to process")
    
    successful = 0
    failed = 0
    
    for file_path in files_to_process:
        try:
            print(f"Processing: {file_path.name}")
            
            # Convert file
            result = md.convert(str(file_path))
            
            # Create output filename
            output_filename = file_path.stem + '.md'
            output_path = Path(output_dir) / output_filename
            
            # Save result
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result.text_content)
            
            print(f"  ✅ Saved to: {output_path}")
            successful += 1
            
        except Exception as e:
            print(f"  ❌ Failed: {e}")
            failed += 1
    
    print(f"\n📊 Batch processing complete!")
    print(f"   Successful: {successful}")
    print(f"   Failed: {failed}")
    print(f"   Output directory: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Batch convert documents to Markdown')
    parser.add_argument('input_dir', help='Directory containing files to convert')
    parser.add_argument('--output', '-o', default='converted_markdown', 
                       help='Output directory (default: converted_markdown)')
    parser.add_argument('--types', '-t', nargs='+', 
                       default=['.pdf', '.docx', '.pptx', '.xlsx', '.html', '.txt'],
                       help='File types to process (default: common document types)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_dir):
        print(f"Error: Directory '{args.input_dir}' does not exist")
        sys.exit(1)
    
    batch_convert(args.input_dir, args.output, args.types)