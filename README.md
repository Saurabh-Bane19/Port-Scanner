# Port Scanner  

## Overview  
This project is a **multi-threaded port scanner** designed to efficiently scan for open ports on a target system. It includes multiple scanning techniques, error handling, and stealth features to bypass basic Intrusion Detection Systems (IDS).  

## Features  
✅ **Basic TCP and UDP Scanning**  
✅ **Multi-threading** for Speed  
✅ **Error Handling & Reporting**  
✅ **Banner Grabbing & OS Detection**  
✅ **Stealth Techniques** (Random Delays, IDS Evasion)  
✅ **Export Results** to JSON, CSV, or Text  

## Installation  

### Prerequisites  
- **Python 3.x**  
- Install the required dependencies:  

  ```sh
  pip install -r requirements.txt


## Usage
Run the port scanner with the following command:

python port_scanner.py

Follow the prompts to enter the target IP and port range.

## Scanning Techniques

1. Basic TCP/UDP Scanning
Attempts to establish a connection to check if a port is open.

python port_scanner_basic.py

2. Multi-Threaded Scanning
Uses multiple threads to improve scanning speed.

python port_scanner_threading.py

3. Stealth Scanning (Avoid IDS Detection)
Introduces random delays between scans to reduce detection risk.

python port_scanner_random_delays.py

4. Banner Grabbing
Retrieves service information from open ports.

python grab_banner.py

5. OS Detection
Attempts to determine the operating system of the target.

python os_detection.py

6. Save Scan Results
Exports scan results to a structured format (JSON, CSV, or text).

python save_results.py

Enter target IP: 192.168.1.1
Enter start port: 20
Enter end port: 100
Scanning 192.168.1.1 from port 20 to 100...

[+] Scanning target: 192.168.1.1
[+] Open ports detected:
    - Port 22 (SSH)
    - Port 80 (HTTP)


Roadmap
🚀 Implement more stealth techniques
📜 Enhance logging/reporting features
🔍 Improve OS detection accuracy
🛠️ Add more evasion techniques

## Disclaimer
This tool is for educational and ethical purposes only.
🚨 Unauthorized scanning of networks is illegal. Always ensure you have explicit permission before scanning any system.

