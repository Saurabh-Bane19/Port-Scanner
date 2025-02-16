import os
import platform
import subprocess
import re
from scapy.all import sr1, IP, ICMP

def get_ttl_scapy(target_ip):
    try:
        # Send ICMP Echo Request (Ping)
        packet = IP(dst=target_ip) / ICMP()
        response = sr1(packet, timeout=2, verbose=False)
        
        if response:
            return response.ttl
        else:
            print("No response received.")
            return None
    except Exception as e:
        print(f"Error using scapy: {e}")
        return None

def get_ttl_ping(target_ip):
    try:
        if platform.system().lower() == "windows":
            cmd = f"ping -n 1 {target_ip}"
        else:
            cmd = f"ping -c 1 {target_ip}"

        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        ttl_match = re.search(r"TTL=(\d+)", output)

        if ttl_match:
            return int(ttl_match.group(1))
        else:
            print("TTL not found in ping response.")
            return None
    except Exception as e:
        print(f"Error using ping command: {e}")
        return None

def detect_os(ttl):
    if ttl is None:
        return "Unknown OS"
    
    if ttl <= 64:
        return "Linux / Unix-based"
    elif ttl <= 128:
        return "Windows"
    elif ttl <= 255:
        return "Cisco / Network device"
    else:
        return "Unknown OS"

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    print(f"\nPinging {target_ip} to analyze TTL...")

    ttl_value = get_ttl_scapy(target_ip) or get_ttl_ping(target_ip)

    if ttl_value:
        os_guess = detect_os(ttl_value)
        print(f"\n[+] TTL Value: {ttl_value}")
        print(f"[+] Estimated OS: {os_guess}")
    else:
        print("\n[-] Unable to determine OS.")
