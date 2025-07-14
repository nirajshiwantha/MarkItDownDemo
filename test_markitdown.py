from markitdown import MarkItDown
import os

def test_basic_conversion():
    """Test basic MarkItDown functionality"""
    md = MarkItDown()
    
    # Create a simple test file
    test_content = """
    <!DOCTYPE html>
    <html>
    <head><title>Test Document</title></head>
    <body>
        <h1>Welcome to MarkItDown</h1>
        <h2>Features</h2>
        <ul>
            <li>Converts multiple file formats</li>
            <li>Preserves document structure</li>
            <li>Works with AI/LLMs</li>
        </ul>
        <p>This is a <strong>test</strong> paragraph with <em>formatting</em>.</p>
        <table>
            <tr><th>Format</th><th>Supported</th></tr>
            <tr><td>PDF</td><td>Yes</td></tr>
            <tr><td>DOCX</td><td>Yes</td></tr>
            <tr><td>HTML</td><td>Yes</td></tr>
        </table>
    </body>
    </html>
    """
    
    # Save test HTML file
    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    # Convert to markdown
    result = md.convert('test.html')
    
    print("=== Original HTML ===")
    print(test_content[:200] + "...")
    print("\n=== Converted Markdown ===")
    print(result.text_content)
    
    # Save the result
    with open('test_output.md', 'w', encoding='utf-8') as f:
        f.write(result.text_content)
    
    print(f"\n✅ Conversion successful! Output saved to test_output.md")
    
    # Clean up
    os.remove('test.html')

if __name__ == "__main__":
    test_basic_conversion()