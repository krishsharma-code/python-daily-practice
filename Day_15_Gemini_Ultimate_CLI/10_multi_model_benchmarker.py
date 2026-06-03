import os
import time
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def benchmark_models(prompt):
    """
    Runs the same prompt across two Gemini models and compares performance.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    models = ["gemini-2.0-flash", "gemini-2.0-pro-experimental"]
    results = []

    print(f"Benchmarking models with prompt: '{prompt[:50]}...'")
    print("-" * 50)

    for model_name in models:
        start_time = time.time()
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            end_time = time.time()
            duration = end_time - start_time
            results.append({
                "model": model_name,
                "time": duration,
                "response": response.text[:200] + "..." if len(response.text) > 200 else response.text
            })
            print(f"Completed {model_name} in {duration:.2f}s")
        except Exception as e:
            print(f"Error with {model_name}: {e}")

    print("\n--- BENCHMARK RESULTS ---\n")
    print(f"{'Model':<30} | {'Time (s)':<10}")
    print("-" * 45)
    for res in results:
        print(f"{res['model']:<30} | {res['time']:<10.2f}")
    
    print("\n--- RESPONSE COMPARISON ---\n")
    for res in results:
        print(f"Model: {res['model']}")
        print(f"Snippet: {res['response']}")
        print("-" * 20)

def main():
    parser = argparse.ArgumentParser(description="Gemini Multi-Model Benchmarker")
    parser.add_argument("prompt", help="The programming prompt to benchmark")
    args = parser.parse_args()

    benchmark_models(args.prompt)

if __name__ == "__main__":
    main()
