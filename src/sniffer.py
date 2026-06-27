from scapy.all import sniff
from analyzer import analyze_packet


def start_sniffer():

    print("=" * 60)
    print(" NetSentry - Basic Network Sniffer")
    print("=" * 60)
    print("Listening for packets...")
    print("Press CTRL+C to stop.\n")

    sniff(
        prn=analyze_packet,
        store=False
    )
