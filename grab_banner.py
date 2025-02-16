import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, port))

        # Send a simple HTTP request (GET /)
        sock.sendall(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")

        banner = sock.recv(1024).decode().strip()
        if banner:
            print(f"Banner for {ip}:{port}:")
            print(banner)
        else:
            print(f"No banner received from {ip}:{port}")
        
        return banner if banner else None

    except socket.error as e:
        print(f"Error grabbing banner for {ip}:{port} - {e}")
        return None
    finally:
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter port: "))
    print(f"Grabbing banner for {target_ip}:{target_port}...")
    grab_banner(target_ip, target_port)
