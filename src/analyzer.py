from scapy.layers.inet import IP


def analyze_packet(packet):
    """
    Analyze captured packet and display basic information.
    """

    if packet.haslayer(IP):
        ip = packet[IP]

        print("-" * 60)
        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")
        print(f"Protocol       : {ip.proto}")
