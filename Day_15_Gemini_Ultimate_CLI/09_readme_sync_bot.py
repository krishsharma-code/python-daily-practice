import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def update_readme():
    """
    Reads code modules in the Day_15 directory and updates the README.md.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Identify files in the current day's directory
    day_dir = "Day_15_Gemini_Ultimate_CLI"
    if not os.path.exists(day_dir):
        # Fallback if run from inside the dir
        day_dir = "."
    
    files_to_document = [f for f in os.listdir(day_dir) if f.endswith(".py")]
    
    file_summaries = []
    for file in sorted(files_to_document):
        file_path = os.path.join(day_dir, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        print(f"Summarizing {file}...")
        prompt = f"Summarize the purpose and usage of this CLI tool in one bullet point for a README.md file:\n\n```python\n{content}\n```"
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            file_summaries.append(response.text.strip())
        except Exception as e:
            file_summaries.append(f"- **{file}**: Error summarizing ({str(e)})")

    new_readme_content = (
        "# Day 15: Gemini Ultimate CLI\n\n"
        "This directory contains 10 powerful CLI tools leveraging the Gemini AI SDK for repository auditing, "
        "security patching, log analysis, and more.\n\n"
        "## 🛠️ Tools Included\n\n" + "\n".join(file_summaries) +
        "\n\n## 🚀 How to Use\nEach script can be run using Python 3. Ensure your `GEMINI_API_KEY` is set in a `.env` file."
    )

    with open(os.path.join(day_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(new_readme_content)
    
    print(f"README.md updated in {day_dir}")

def main():
    print("Starting README Sync Bot...")
    update_readme()

if __name__ == "__main__":
    main()
