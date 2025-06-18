import socket
import time

# An external target that is known to be online
TARGET_IP = "8.8.8.8" # Google's DNS Server
PORTS_TO_TEST = range(1, 100) # Test the first 99 ports

print(f"Starting test: sending SYN packets to {TARGET_IP}...")

for port in PORTS_TO_TEST:
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a very short timeout so it doesn't hang
        sock.settimeout(0.1)
        # This sends a SYN packet but doesn't wait for a full connection
        sock.connect_ex((TARGET_IP, port))
        sock.close()
        print(f"Sent SYN to port {port}")
    except Exception as e:
        print(f"Error on port {port}: {e}")
    time.sleep(0.1) # Wait a little between packets

print("Test finished.")