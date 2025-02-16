import socket
import threading

# Define a function to scan a specific port
def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Increased timeout
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)  # Add open ports to the list
        sock.close()
    except socket.error:
        pass

# Function to initiate the scanning process using multiple threads
def scan_ports(ip, start_port, end_port):
    open_ports = []  # List to hold open ports
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    print(f"Scanning {target_ip} from port {start_port} to {end_port}")
    
    open_ports = scan_ports(target_ip, start_port, end_port)
    
    if open_ports:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")
