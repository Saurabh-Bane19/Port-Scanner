import socket
import threading
import random
import time

# Function to scan individual port with error handling
def scan_port(ip, port):
    """Try connecting to a port and handle errors gracefully."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set timeout for responsiveness
        result = s.connect_ex((ip, port))  # Returns 0 if open, else error code
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except socket.timeout:
        print(f"[-] Timeout on port {port}")
    except socket.error as err:
        print(f"[-] Error scanning port {port}: {err}")

# Function to scan multiple ports using threads with stealth features
def scan_ports(ip, start_port, end_port):
    """Scan a range of ports with stealth scanning features."""
    print(f"Scanning {ip} from port {start_port} to {end_port}")
    threads = []
    for port in range(start_port, end_port + 1):
        # Start scanning using multiple threads
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
        
        # Adding randomized delay for stealth
        delay = random.uniform(0.1, 2)  # Random delay between 0.1 and 2 seconds
        time.sleep(delay)  # Add a random delay to avoid detection

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

# Example usage:
if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target_ip, start_port, end_port)
