from markitdown import MarkItDown
import os
import json
from datetime import datetime

class DocumentProcessor:
    def __init__(self, enable_plugins=False):
        self.md = MarkItDown(enable_plugins=enable_plugins)
        self.results = []
    
    def process_file(self, file_path):
        """Process a single file and return results"""
        print(f"Processing: {file_path}")
        
        try:
            # Convert the file
            result = self.md.convert(file_path)
            
            # Get file info
            file_size = os.path.getsize(file_path)
            file_ext = os.path.splitext(file_path)[1].lower()
            
            conversion_result = {
                'file_path': file_path,
                'file_size': file_size,
                'file_extension': file_ext,
                'conversion_time': datetime.now().isoformat(),
                'success': True,
                'content_preview': result.text_content[:200] + "..." if len(result.text_content) > 200 else result.text_content,
                'content_length': len(result.text_content),
                'full_content': result.text_content
            }
            
            print(f"✅ Success! Converted {file_size} bytes to {len(result.text_content)} characters")
            
        except Exception as e:
            conversion_result = {
                'file_path': file_path,
                'file_size': 0,
                'file_extension': file_ext if 'file_ext' in locals() else 'unknown',
                'conversion_time': datetime.now().isoformat(),
                'success': False,
                'error': str(e),
                'content_length': 0
            }
            print(f"❌ Failed: {str(e)}")
        
        self.results.append(conversion_result)
        return conversion_result
    
    def process_directory(self, directory_path, output_dir="markdown_output"):
        """Process all supported files in a directory"""
        supported_extensions = {'.pdf', '.docx', '.pptx', '.xlsx', '.html', '.htm', 
                              '.txt', '.csv', '.json', '.xml', '.rtf'}
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        processed_files = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1].lower()
                
                if file_ext in supported_extensions:
                    result = self.process_file(file_path)
                    
                    if result['success']:
                        # Save individual markdown file
                        base_name = os.path.splitext(file)[0]
                        output_path = os.path.join(output_dir, f"{base_name}.md")
                        
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(result['full_content'])
                        
                        print(f"📁 Saved: {output_path}")
                    
                    processed_files.append(result)
        
        return processed_files
    
    def generate_report(self, output_file="conversion_report.json"):
        """Generate a detailed report of all conversions"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_files': len(self.results),
            'successful_conversions': len([r for r in self.results if r['success']]),
            'failed_conversions': len([r for r in self.results if not r['success']]),
            'total_content_length': sum(r.get('content_length', 0) for r in self.results),
            'results': self.results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n📊 Report saved to {output_file}")
        print(f"Summary: {report['successful_conversions']}/{report['total_files']} files converted successfully")
        
        return report

# Example usage
if __name__ == "__main__":
    # Create some test files to demonstrate
    test_files = {
        'test.txt': "This is a simple text file.\n\nIt has multiple paragraphs.\n\n- And some\n- Bullet points",
        'test.csv': "Name,Age,City\nJohn,25,New York\nJane,30,Los Angeles\nBob,35,Chicago",
        'test.json': '{"name": "MarkItDown Demo", "features": ["PDF conversion", "Office docs", "Multi-modal"], "rating": 5}',
        'test.html': '''<!DOCTYPE html>
<html>
<head><title>Demo Page</title></head>
<body>
    <h1>Demo Document</h1>
    <p>This is a <strong>demonstration</strong> of MarkItDown capabilities.</p>
    <ul>
        <li>HTML to Markdown conversion</li>
        <li>Structure preservation</li>
        <li>Easy integration</li>
    </ul>
</body>
</html>'''
    }
    
    # Create test files
    print("Creating test files...")
    for filename, content in test_files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {filename}")
    
    # Process files
    print("\n" + "="*50)
    print("STARTING DOCUMENT PROCESSING")
    print("="*50)
    
    processor = DocumentProcessor()
    
    # Process individual files
    for filename in test_files.keys():
        processor.process_file(filename)
        print("-" * 30)
    
    # Generate report
    report = processor.generate_report()
    
    # Clean up test files
    print(f"\nCleaning up test files...")
    for filename in test_files.keys():
        os.remove(filename)
        print(f"Removed: {filename}")
    
    print(f"\n🎉 Demo complete! Check the 'markdown_output' directory and 'conversion_report.json' for results.")