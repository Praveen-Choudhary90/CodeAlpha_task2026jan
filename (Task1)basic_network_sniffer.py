from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_analyzer(packet):
    
    if IP not in packet:
        return

    print("\n📦 New Packet Captured")
    print(f"Source IP        : {packet[IP].src}")
    print(f"Destination IP   : {packet[IP].dst}")

    if TCP in packet:
        print("Protocol         : TCP")
        print(f"Source Port      : {packet[TCP].sport}")
        print(f"Destination Port : {packet[TCP].dport}")

    elif UDP in packet:
        print("Protocol         : UDP")
        print(f"Source Port      : {packet[UDP].sport}")
        print(f"Destination Port : {packet[UDP].dport}")

    else:
        print("Protocol         : Other")

    if packet.haslayer(Raw):
        raw_payload = packet[Raw].load
        print("Payload (raw)    :", raw_payload[:50])

        try:
            decoded_payload = raw_payload.decode("utf-8", errors="ignore")
            if decoded_payload.strip():
                print("Payload (decoded):")
                print(decoded_payload[:200])
        except:
            print("Payload not readable")

print("🔍 Sniffing started... Press Ctrl+C to stop.\n")
sniff(prn=packet_analyzer, store=False)
