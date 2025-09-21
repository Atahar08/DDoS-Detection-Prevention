#!/usr/bin/env python3
"""
ddos_detector.py
----------------
Real-time DDoS detection using Scapy.
Detects suspicious traffic per IP and logs alerts.
"""

from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time
import os

LOG_FILE = "../logs/attack_logs.txt"
THRESHOLD = 50  # packets per interval per IP
INTERVAL = 10   # seconds

ip_counts = defaultdict(int)
start_time = time.time()

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_attack(ip, count):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] Potential DDoS detected from IP {ip} - {count} packets\n")
    print(f"[ALERT] Potential DDoS detected from IP {ip}")

def detect_packet(packet):
    global ip_counts, start_time
    if IP in packet:
        src_ip = packet[IP].src
        ip_counts[src_ip] += 1

    if time.time() - start_time >= INTERVAL:
        for ip, count in ip_counts.items():
            if count > THRESHOLD:
                log_attack(ip, count)
        ip_counts.clear()
        start_time = time.time()

if __name__ == "__main__":
    print("Starting DDoS detector...")
    sniff(prn=detect_packet, store=0)
