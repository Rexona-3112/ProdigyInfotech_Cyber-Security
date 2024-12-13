from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
import os
import csv
from collections import Counter

# Ensure script is run as root/admin
def check_privileges():
    if os.name != 'nt' and os.geteuid() != 0:
        print("[!] Please run this script with root privileges.")
        exit(1)

# Callback function to process each packet
packet_stats = Counter()  # To track packet statistics

def analyze_packet(packet):
    try:
        if IP in packet:
            # Extract basic information
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst
            protocol = "Other"

            # Check protocol type
            if TCP in packet:
                protocol = "TCP"
                packet_stats['TCP'] += 1
            elif UDP in packet:
                protocol = "UDP"
                packet_stats['UDP'] += 1
            elif ICMP in packet:
                protocol = "ICMP"
                packet_stats['ICMP'] += 1
            else:
                packet_stats['Other'] += 1

            # Display extracted information
            print(f"[+] Source: {source_ip}, Destination: {destination_ip}, Protocol: {protocol}")

            # Display payload if available
            if packet.haslayer('Raw'):
                payload = bytes(packet['Raw']).decode('utf-8', errors='ignore')
                print(f"    Payload: {payload[:100]}")  # Limit payload display to 100 characters

            # Log packet details
            log_packet([source_ip, destination_ip, protocol, payload if 'payload' in locals() else "No payload"])
    
    except Exception as e:
        print(f"[!] Error processing packet: {e}")

# Save packets to a log file (CSV)
def log_packet(details):
    with open("packet_log.csv", "a", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(details)

# Main function to capture packets
def start_sniffer(interface=None, count=10, filter_protocol=None):
    print("[*] Starting packet sniffer...")
    print("[*] Press Ctrl+C to stop sniffing.\n")

    # Initialize packet log
    with open("packet_log.csv", "w", newline="") as log_file:
        writer = csv.writer(log_file)
        writer.writerow(["Source IP", "Destination IP", "Protocol", "Payload"])

    # Define filter if specified
    bpf_filter = f"{filter_protocol}" if filter_protocol else "ip"
    
    # Start sniffing
    sniff(iface=interface, filter=bpf_filter, prn=analyze_packet, count=count, store=False)

    # Display summary stats
    print("\n[+] Packet Capture Summary:")
    for protocol, count in packet_stats.items():
        print(f"    {protocol}: {count} packets")

# Run the sniffer
if __name__ == "__main__":
    check_privileges()
    # Customize the interface, packet count, and filter as needed
    start_sniffer(interface=None, count=50, filter_protocol=None)
