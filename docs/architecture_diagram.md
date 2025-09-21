# DDoS Detection & Prevention System Architecture

+------------------+ +--------------------+
| | | |
| Incoming Traffic| -----> | ddos_detector.py |
| | | (Threshold check) |
+------------------+ +---------+----------+
|
v
+--------------+
| attack_logs |
| (logs/) |
+------+------+
|
v
+----------------+
| auto_block.py |
| (iptables) |
+----------------+
|
v
+---------------------+
| Mitigated Traffic |
+---------------------+




- Snort/Suricata IDS monitors packets and triggers alerts.
- Firewall rules provide additional layer of protection.
