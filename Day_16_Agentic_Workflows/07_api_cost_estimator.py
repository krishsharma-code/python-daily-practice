import argparse
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def estimate_cost(prompt):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    model_id = "gemini-2.0-flash"
    
    try:
        # Get token count for input
        input_tokens = client.models.count_tokens(
            model=model_id,
            contents=prompt
        ).total_tokens
        
        # Simulate a typical response size (or actually call it)
        # For an estimator, we might just use the input tokens to predict
        # but let's do a real call to get actual output tokens for a sample interaction
        response = client.models.generate_content(
            model=model_id,
            contents=prompt
        )
        
        output_tokens = client.models.count_tokens(
            model=model_id,
            contents=response.text
        ).total_tokens

        # Pricing for Gemini 2.0 Flash (as of early 2025/2026 estimates)
        # Input: $0.10 / 1M tokens
        # Output: $0.40 / 1M tokens
        input_cost = (input_tokens / 1_000_000) * 0.10
        output_cost = (output_tokens / 1_000_000) * 0.40
        total_cost = input_cost + output_cost

        print(f"=== Cost Estimate ({model_id}) ===")
        print(f"Input Tokens:  {input_tokens}")
        print(f"Output Tokens: {output_tokens}")
        print(f"Input Cost:    ${input_cost:.6f}")
        print(f"Output Cost:   ${output_cost:.6f}")
        print(f"Total Cost:    ${total_cost:.6f}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="API Cost Estimator CLI")
    parser.add_argument("prompt", help="The prompt to analyze for cost")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    estimate_cost(args.prompt)

if __name__ == "__main__":
    main()
