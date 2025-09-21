# 🛡️ DDoS Detection & Prevention System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OS](https://img.shields.io/badge/Linux-Ubuntu-orange)
![Status](https://img.shields.io/badge/Status-Ready-green)

---

## **Overview**

This project is a **real-time DDoS Detection & Prevention System** built with **Python, Scapy, Snort, and iptables**.  
It captures network traffic, detects suspicious activity, logs alerts, and automatically blocks malicious IPs.

Perfect for **learning, testing, and showcasing** cybersecurity skills on your GitHub portfolio.

---

## **Features**

- 🟢 Real-time network traffic monitoring (`ddos_detector.py`)
- 🛑 Automatic IP blocking via iptables (`auto_block.py`)
- 🚨 Safe DDoS simulation for testing (`simulate_attack.py`)
- 🔐 Snort & Suricata IDS integration
- ⚡ Firewall mitigation and rate-limiting rules
- 📄 Logging for attack analysis and monitoring

---

## **Folder Structure**

DDoS-Detection-Prevention/
│
├── scripts/ # Python scripts
│ ├── ddos_detector.py
│ ├── auto_block.py
│ └── simulate_attack.py
│
├── configs/ # IDS & firewall configs
│ ├── snort_rules.rules
│ ├── suricata_rules.yaml
│ └── firewall_rules.sh
│
├── logs/ # Logs for attacks and blocked IPs
│ ├── attack_logs.txt
│ └── blocked_ips.txt
│
├── docs/ # Documentation & diagrams
│ └── architecture_diagram.md
│
└── README.md



---

## **Prerequisites**

Ensure your system is running **Ubuntu/Linux** and has Python installed.


# Update system
`sudo apt update`

# Install dependencies
`sudo apt install python3-pip python3-dev iptables snort -y`

# Python packages
`pip install scapy requests`

## 🚀 Setup & Running Instructions

### 1. Install Dependencies

**System Packages**

`sudo apt update`  
`sudo apt install python3-pip python3-dev iptables snort -y`

**Python Packages**

`pip install scapy requests`

---

### 2. Set Script Permissions

`chmod +x scripts/*.py`  
`chmod +x configs/firewall_rules.sh`

---

### 3. Apply Firewall Rules

`sudo bash configs/firewall_rules.sh`  
✅ This sets up basic iptables rules for traffic filtering and rate limiting.

---

### 4. Run the System

**a) Start DDoS Detection**

`python3 scripts/ddos_detector.py`  
🟢 Monitors network traffic in real-time and logs suspicious IPs.

**b) Run Automatic IP Blocking**

`python3 scripts/auto_block.py`  
🛑 Reads the detection logs and blocks malicious IPs using iptables.

**c) Optional: Simulate DDoS Traffic (Safe Test)**

`python3 scripts/simulate_attack.py`  
🚨 Sends controlled traffic to test detection and auto-blocking.

---

### 5. Verify Logs

**Detected Attacks:** `/logs/attack_logs.txt`  
**Blocked IPs:** `/logs/blocked_ips.txt`  

Check these files to confirm detection and mitigation.
