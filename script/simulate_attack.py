#!/usr/bin/env python3
"""
simulate_attack.py
-----------------
Simulates a DDoS attack for safe testing.
Sends multiple HTTP requests to a target IP (localhost recommended).
"""

import requests
import threading

TARGET = "http://127.0.0.1"
NUM_REQUESTS = 100
THREADS = 10

def send_requests():
    for _ in range(NUM_REQUESTS // THREADS):
        try:
            requests.get(TARGET)
        except:
            pass

if __name__ == "__main__":
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=send_requests)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Simulated DDoS traffic complete.")
