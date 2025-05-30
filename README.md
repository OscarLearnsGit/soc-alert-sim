# SOC Alert Simulator 

A beginner-friendly cybersecurity project built in Python to simulate basic Security Operations Center (SOC) alerting logic. This script analyzes simulated log entries for suspicious patterns like failed logins, brute-force attacks, and unauthorized access to sensitive endpoints.

## 🚀 Features
- Detects failed login attempts by username and IP
- Identifies suspicious access to `/admin` URLs
- Counts failed login attempts per IP to detect brute-force behavior
- Includes simulated timestamps and sample logs

## 🔐 Real-World Use Cases
- Brute force detection simulation
- Log parsing and security triage scripting
- Foundation for automated SOC tooling or alerting rules

## 🛠 Technologies
- Python 3.12
- Standard libraries only: `datetime`, `collections`

## 📁 File
- `soc_alert_simulator.py`: Main script with all logic

## 📋 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/soc-alert-simulator.git
   cd soc-alert-simulator
   ```
2. Run the Python script:
   ```bash
   python soc_alert_simulator.py
   ```

## 🖥️ Example Output
```
🔴 Failed login attempt by user guest from 10.0.0.3
⚠️ Suspicious /admin access by 192.168.1.101 with status 401
🚨 Brute Force Alert: 10.0.0.3 has 3 failed login attempts!
```

## 🎯 Next Steps
- Add CLI arguments using `argparse`
- Export alerts to `.csv` or `.txt`
- Integrate with a Streamlit dashboard
- Hook into real log files or SIEM exports

## 💼 About the Author
This project was developed as part of a structured 7-week cybersecurity coding program focused on Python + SQL for SOC roles.

> Inspired by real SOC workflows. Built to learn. Ready to grow.
