import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def chunk_text(text, chunk_size=2000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def query_doc(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    chunks = chunk_text(content)
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    print(f"Loaded {file_path} and split into {len(chunks)} chunks.")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nAsk a question about the document: ")
        if query.lower() == 'exit':
            break
        
        # In a real RAG we would use embeddings, but for a simple CLI tool, 
        # we'll provide the most relevant context or just the whole thing if small.
        # Here we'll just send the query with the context of the file.
        
        prompt = f"""
        Use the following document content to answer the user's question.
        
        Document Content:
        {content[:15000]}  # Simple truncation to fit context
        
        Question: {query}
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            print(f"\nAnswer: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="RAG Document Querier CLI")
    parser.add_argument("file", help="Path to the text or markdown file")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    query_doc(args.file)

if __name__ == "__main__":
    main()
