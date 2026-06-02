import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Scans the current directory for .py files, extracts their structure/purpose,
    and uses Gemini to generate a professional README.md.
    """
    # Configure Gemini
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)

    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    
    if not py_files:
        print("No Python files found in the current directory.")
        return

    context_data = ""
    for file in py_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                # We'll just take the first 50 lines or so to keep the context lean
                content = f.read(2000) 
                context_data += f"\nFILE: {file}\nCONTENT SNIPPET:\n{content}\n"
        except Exception as e:
            print(f"Skipping {file}: {e}")

    prompt = f"""
    Act as a Technical Documentation Specialist.
    Based on the following Python files in the 'Day 14 Gemini CLI Suite', 
    generate a comprehensive and beautiful README.md file.
    
    Include:
    1. A catchy title and introduction.
    2. A table of contents.
    3. Detailed descriptions for each script.
    4. Setup instructions (Environment variables, etc.).
    5. Usage examples.
    
    File Context:
    {context_data}
    """

    try:
        print("Generating automated README.md...")
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content(prompt)
        
        with open("README_DAY_14.md", "w", encoding='utf-8') as f:
            f.write(response.text)
        
        print("Successfully generated README_DAY_14.md")

    except Exception as e:
        print(f"Error during generation: {e}")

if __name__ == "__main__":
    main()
