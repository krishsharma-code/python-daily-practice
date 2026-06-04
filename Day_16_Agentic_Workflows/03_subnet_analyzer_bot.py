import argparse
import ipaddress
import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()

def analyze_subnet(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
        
        info = {
            "Network Address": str(network.network_address),
            "Netmask": str(network.netmask),
            "Broadcast Address": str(network.broadcast_address),
            "Total Hosts": network.num_addresses,
            "Usable Host Range": f"{list(network.hosts())[0]} - {list(network.hosts())[-1]}" if network.num_addresses > 2 else "N/A"
        }
        
        print("=== Subnet Analysis ===")
        for key, value in info.items():
            print(f"{key}: {value}")
        
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        prompt = f"""
        Given the following network details:
        Network: {info['Network Address']}
        Mask: {info['Netmask']}
        Total Hosts: {info['Total Hosts']}
        
        Suggest network segmentation best practices and security considerations for this subnet.
        """
        
        print("\n=== Gemini Security Suggestions ===")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        print(response.text)

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Subnet Analyzer Bot CLI")
    parser.add_argument("cidr", help="IP address with CIDR (e.g., 192.168.1.0/24)")
    args = parser.parse_args()

    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY not found.")
        sys.exit(1)

    analyze_subnet(args.cidr)

if __name__ == "__main__":
    main()
