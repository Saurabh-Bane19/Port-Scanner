import socket

def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempt
        
        # Attempt to connect to the target port
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        exit()
    except socket.error:
        print("[!] Unable to connect to target")
        exit()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    print(f"\nScanning {target} from port {start_port} to {end_port}\n")
    for port in range(start_port, end_port + 1):
        scan_port(target, port)