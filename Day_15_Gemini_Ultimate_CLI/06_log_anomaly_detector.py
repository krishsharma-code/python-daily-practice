import os
import sys
import argparse
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def detect_anomalies(log_line):
    """
    Sends a log line to Gemini to detect if it represents an anomaly.
    """
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    
    prompt = (
        "Analyze the following log line and determine if it represents an anomaly, "
        "a security threat, or a critical system error. Respond with 'ANOMALY: [Reason]' "
        "if it is suspicious, otherwise respond with 'NORMAL'.\n\n"
        f"Log: {log_line}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Gemini Log Anomaly Detector")
    parser.add_argument("--file", help="Path to a log file to monitor (simulated streaming)")
    args = parser.parse_args()

    print("=== Gemini Log Anomaly Detector ===")
    print("Monitoring logs... (Press Ctrl+C to stop)")

    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: {args.file} not found.")
            return
        
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    result = detect_anomalies(line.strip())
                    if "ANOMALY" in result:
                        print(f"\033[91m{result}\033[0m")
                    else:
                        print(f"Log: {line.strip()[:50]}... -> OK")
    else:
        # Stream from stdin
        print("Waiting for logs from stdin (type or pipe logs)...")
        for line in sys.stdin:
            if line.strip():
                result = detect_anomalies(line.strip())
                if "ANOMALY" in result:
                    print(f"\033[91m{result}\033[0m")
                else:
                    print(f"Log: {line.strip()[:50]}... -> OK")

if __name__ == "__main__":
    main()
