import json
import csv

def save_to_json(data, filename="scan_results.json"):
    """Save scan results to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Results saved to {filename}")

def save_to_csv(data, filename="scan_results.csv"):
    """Save scan results to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Port", "Status", "Service", "OS"])
        for entry in data:
            writer.writerow(entry)
    print(f"[+] Results saved to {filename}")

def save_to_text(data, filename="scan_results.txt"):
    """Save scan results to a text file."""
    with open(filename, "w") as f:
        for entry in data:
            f.write(f"IP: {entry[0]}, Port: {entry[1]}, Status: {entry[2]}, Service: {entry[3]}, OS: {entry[4]}\n")
    print(f"[+] Results saved to {filename}")

# Example usage
if __name__ == "__main__":
    scan_results = [
        ("127.0.0.1", 80, "Open", "HTTP", "Windows"),
        ("127.0.0.1", 443, "Open", "HTTPS", "Windows"),
        ("127.0.0.1", 22, "Closed", "SSH", "Linux"),
    ]
    
    save_to_json(scan_results)
    save_to_csv(scan_results)
    save_to_text(scan_results)
