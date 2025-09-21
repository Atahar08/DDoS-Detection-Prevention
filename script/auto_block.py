#!/usr/bin/env python3
"""
auto_block.py
-------------
Automatically blocks suspicious IPs using iptables.
Reads logs from attack_logs.txt.
"""

import os
import re

LOG_FILE = "../logs/attack_logs.txt"
BLOCKED_FILE = "../logs/blocked_ips.txt"

os.makedirs(os.path.dirname(BLOCKED_FILE), exist_ok=True)
if not os.path.exists(BLOCKED_FILE):
    open(BLOCKED_FILE, "w").close()

def block_ip(ip):
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    with open(BLOCKED_FILE, "a") as f:
        f.write(f"{ip}\n")
    print(f"[INFO] Blocked IP {ip}")

def read_new_attacks():
    blocked_ips = set()
    if os.path.exists(BLOCKED_FILE):
        with open(BLOCKED_FILE, "r") as f:
            blocked_ips = set(line.strip() for line in f)

    new_ips = set()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                match = re.search(r"from IP (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    if ip not in blocked_ips:
                        new_ips.add(ip)
    return new_ips

if __name__ == "__main__":
    print("Checking for new suspicious IPs to block...")
    ips_to_block = read_new_attacks()
    for ip in ips_to_block:
        block_ip(ip)
