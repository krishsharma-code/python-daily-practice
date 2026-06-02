import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """
    Reads prompts from 'prompts.txt' and processes them sequentially.
    Saves each response to a dedicated 'reports' directory.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        return
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt_file = "prompts.txt"
    output_dir = "automated_reports"

    # Create dummy prompts if file doesn't exist
    if not os.path.exists(prompt_file):
        with open(prompt_file, "w") as f:
            f.write("Summarize the benefits of Python.\n")
            f.write("Write a 3-line poem about Gemini AI.\n")
            f.write("Explain recursion to a 5-year old.\n")
        print(f"Created sample '{prompt_file}'")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(prompt_file, "r") as f:
        prompts = [line.strip() for line in f if line.strip()]

    print(f"Processing {len(prompts)} prompts...")

    for i, prompt in enumerate(prompts):
        try:
            print(f"Running Prompt {i+1}: {prompt[:30]}...")
            response = model.generate_content(prompt)
            
            filename = f"report_{i+1}.txt"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, "w", encoding='utf-8') as rf:
                rf.write(f"PROMPT: {prompt}\n")
                rf.write("-" * 20 + "\n")
                rf.write(response.text)
            
            print(f"Saved to {filepath}")

        except Exception as e:
            print(f"Error on prompt {i+1}: {e}")

if __name__ == "__main__":
    main()
