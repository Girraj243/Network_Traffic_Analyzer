from logger import log_packet
import scapy.all as scapy # lib for packet sniffing
import csv



# firstly Sniff a packet using scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):   # this ensures that packet has IP layer
        src_ip = packet[scapy.IP].src  # Source IP
        dst_ip = packet[scapy.IP].dst  # Destination IP
        protocol = packet[scapy.IP].proto # protocol TCP or UDP
        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol_name(protocol)}")
        payload = None


        if packet.haslayer(scapy.TCP) or packet.haslayer(scapy.UDP):
            try:
                payload = packet[scapy.Raw].load
                decoded_payload = payload.decode('utf-8')
                print(f"Payload: {decoded_payload}")
            except (IndexError, UnicodeDecodeError):
                print("Payload decoding failed.")

        log_packet(src_ip, dst_ip, protocol,payload)

        logged_data.append({
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Protocol": protocol_name(protocol)
        })
logged_data = []  # empty dict to save data for  csv file
def export_to_csv(filename):
            # Define the CSV file headers
    headers = ["Source IP", "Destination IP", "Protocol", "Payload"]

            # Write the logged data to a CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for data in logged_data:
            writer.writerow(data)

    print(f"Logged data exported to {filename=}")


def protocol_name(number):
    protocol_dict={1:'ICMP', 6:'TCP', 17:'UDP'}
    return protocol_dict.get(number,f"unknown({number})")

def start_sniffing(interface="Realtek RTL8852AE WiFi 6 802.11ax PCIe Adapter"):
    print(f"Sniffing on interface: {interface}")
    scapy.sniff(iface=interface,store=False, prn=packet_callback)

if __name__ == "__main__":
    start_sniffing()


