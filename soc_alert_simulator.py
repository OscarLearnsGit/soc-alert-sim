"""
SOC Alert Simulator
-------------------
This Python script simulates basic SOC (Security Operations Center) logic
by parsing and analyzing mock log data. It detects:
- Failed logins
- Suspicious /admin access
- Brute-force login attempts
"""

from collections import defaultdict
from datetime import datetime

# Sample log data (normally parsed from log files)
log_data = [
    {"timestamp": "2025-05-30T10:00:00", "user": "admin", "ip": "192.168.1.101", "path": "/admin", "status": "401"},
    {"timestamp": "2025-05-30T10:01:00", "user": "guest", "ip": "10.0.0.23", "path": "/home", "status": "200"},
    {"timestamp": "2025-05-30T10:02:00", "user": "admin", "ip": "192.168.1.101", "path": "/admin", "status": "403"},
    {"timestamp": "2025-05-30T10:03:00", "user": "guest", "ip": "10.0.0.3", "status": "failed"},
    {"timestamp": "2025-05-30T10:04:00", "user": "guest", "ip": "10.0.0.3", "status": "failed"},
    {"timestamp": "2025-05-30T10:05:00", "user": "guest", "ip": "10.0.0.3", "status": "failed"},
]

def check_failed_login(entry):
    if entry.get("status") == "failed":
        print(f"🔴 Failed login attempt by user {entry['user']} from {entry['ip']}")

def detect_admin_access(entry):
    if "/admin" in entry.get("path", "") and "200" not in entry.get("status", ""):
        print(f"⚠️ Suspicious /admin access by {entry['ip']} with status {entry['status']}")

def analyze_ip_threshold(entries, threshold=3):
    from collections import defaultdict
    fail_counts = defaultdict(int)
    for entry in entries:
        if entry.get("status") == "failed":
            fail_counts[entry["ip"]] += 1

    for ip, count in fail_counts.items():
        if count >= threshold:
            print(f"🚨 Brute Force Alert: {ip} has {count} failed login attempts!")

# Process log data
for entry in log_data:
    check_failed_login(entry)
    detect_admin_access(entry)

analyze_ip_threshold(log_data)
