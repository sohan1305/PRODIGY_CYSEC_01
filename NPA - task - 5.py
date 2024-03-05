pip install scapy

from scapy.all import sniff

# Define the callback function to process captured packets
def packet_callback(packet):
    if packet.haslayer("IP"):  # Filter packets with IP layer
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto

        # Display relevant information
        print(f"Source IP: {src_ip}  Destination IP: {dst_ip}  Protocol: {protocol}")

        # Extract and display payload data if present
        if packet.haslayer("Raw"):
            payload = packet["Raw"].load
            print(f"Payload: {payload.hex()}")  # Display payload data in hexadecimal format

# Start sniffing packets on the network
print("Packet Sniffer started...")
sniff(prn=packet_callback, store=0, count=10)  # Capture 10 packets
