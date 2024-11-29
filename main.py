import scapy.all as scapy
scapy.show_interfaces()
import csv
import time
from packet_sniffer import start_sniffing,export_to_csv
from logger import init_db,log_packet
from analyzer import analyzer_traffic
from traffic_visualization import visualize_protocol






if __name__ == '__main__':
    connect= init_db()
    print("Database establised")
    start_sniffing()

    analyzer_traffic()

    visualize_protocol()

    export_to_csv(f"logged_packets {time.strftime('%Y-%m-%d')}.csv")