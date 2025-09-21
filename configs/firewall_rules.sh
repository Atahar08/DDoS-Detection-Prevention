#!/bin/bash
# Apply basic firewall rules for DDoS mitigation

# Flush previous rules
sudo iptables -F

# Default policies
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow localhost and established connections
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Rate limiting example
sudo iptables -A INPUT -p tcp --syn -m limit --limit 10/s --limit-burst 20 -j ACCEPT

# Save rules
sudo iptables-save > /etc/iptables/rules.v4

echo "Firewall rules applied successfully."
