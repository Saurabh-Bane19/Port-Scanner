import socket

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

# Test with a known closed port
scan_port("127.0.0.1", 9999)  # Should trigger a connection error

# Test with an invalid IP address
scan_port("999.999.999.999", 80)  # Should trigger a timeout error
