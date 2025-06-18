from scapy.all import sniff, IP, TCP
from collections import deque
import time

# A dictionary to store the timestamps of SYN packets for each source IP
SYN_PACKETS = {}

# A set to keep track of IPs that have been flagged for flooding
FLOODING_IPS = set()

# Configuration settings (could be loaded from a config file)
TIME_WINDOW = 60  # Time window in seconds to monitor for SYN floods
MAX_SYN_PER_IP = 20  # Max number of SYN packets allowed from a single IP within the time window


def packet_callback(packet):
    """
    This function is called for each sniffed packet and checks for potential SYN flood attacks.
    """
    if TCP in packet and packet[TCP].flags == 'S':
        src_ip = packet[IP].src
        current_time = time.time()

        # Check if we have seen this IP before
        if src_ip not in SYN_PACKETS:
            SYN_PACKETS[src_ip] = deque()

        # Append the current timestamp
        SYN_PACKETS[src_ip].append(current_time)

        # Remove timestamps that are outside our time window
        while SYN_PACKETS[src_ip] and current_time - SYN_PACKETS[src_ip][0] > TIME_WINDOW:
            SYN_PACKETS[src_ip].popleft()

        # Check if the number of SYN packets exceeds the threshold
        if len(SYN_PACKETS[src_ip]) > MAX_SYN_PER_IP:
            if src_ip not in FLOODING_IPS:
                dst_port = packet[TCP].dport
                print(f"ALERT: Potential SYN Flood attack detected from IP: {src_ip} targeting port {dst_port}")
                FLOODING_IPS.add(src_ip)

def start_sniffing(interface=None):
    """
    Starts the packet sniffing process on a given network interface.
    """
    print("Starting intrusion detection system...")
    try:
        # The 'prn' argument specifies the callback function to be executed for each packet
        # The 'store' argument is set to 0 to discard sniffed packets and save memory
        if interface:
            sniff(iface=interface, prn=packet_callback, store=0)
        else:
            sniff(prn=packet_callback, store=0)
    except Exception as e:
        print(f"An error occurred during sniffing: {e}")