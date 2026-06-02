import os
import sys
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Loads an image from a path provided via CLI and uses Gemini's vision 
    capabilities to generate a technical description.
    """
    if len(sys.argv) < 2:
        print("Usage: python 09_cli_image_analyzer.py <path_to_image>")
        return

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        return

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)

    try:
        # Load the image using PIL
        img = Image.open(image_path)
        
        # Use gemini-2.5-flash for vision tasks
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        print(f"Analyzing image: {image_path}...")
        
        # Pass both text and image
        response = model.generate_content([
            "Provide a detailed technical description of this image. "
            "Identify objects, colors, and any text present.",
            img
        ])
        
        print("\n--- IMAGE ANALYSIS ---")
        print(response.text)

    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()
