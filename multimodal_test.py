from markitdown import MarkItDown
import os
from openai import OpenAI

def test_with_openai_images():
    """Test image description with OpenAI"""
    
    # You'll need an OpenAI API key for this
    # Get one from: https://platform.openai.com/api-keys
    api_key = input("Enter your OpenAI API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("Skipping OpenAI image test (no API key provided)")
        return
    
    try:
        client = OpenAI(api_key=api_key)
        md = MarkItDown(llm_client=client, llm_model="gpt-4o")
        
        print("MarkItDown with OpenAI configured successfully!")
        print("You can now convert images with: md.convert('your_image.jpg')")
        
        # Create a simple test (you'd need an actual image file)
        # result = md.convert("test_image.jpg")
        # print(result.text_content)
        
    except Exception as e:
        print(f"Error setting up OpenAI: {e}")

def test_audio_transcription():
    """Test audio transcription (requires audio files)"""
    md = MarkItDown()
    
    print("Audio transcription is available for:")
    print("- .wav files")
    print("- .mp3 files") 
    print("- .m4a files")
    print("\nPlace an audio file in this directory and uncomment the code below to test")
    
    # Uncomment and modify for your audio file:
    # result = md.convert("your_audio_file.wav")
    # print("Transcription:", result.text_content)

if __name__ == "__main__":
    print("=== Multimodal Features Test ===\n")
    
    print("1. Testing OpenAI Integration for Images:")
    test_with_openai_images()
    
    print("\n" + "-"*40)
    print("2. Audio Transcription Info:")
    test_audio_transcription()