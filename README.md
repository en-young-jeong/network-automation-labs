# Network Automation with Python (Netmiko & NAPALM)

## 📌 Project Overview
This project demonstrates network automation using Python with Netmiko and NAPALM.
It connects to multiple Cisco routers and switches via Telnet/SSH, applies configurations,
and retrieves device states automatically.

## ⚙️ Features
- Automates configuration tasks (ACL, OSPF, BGP, ARP/MAC tables)
- Supports Telnet & SSH connections
- Saves and compares running-config files
- Implements logging, error handling, and multithreading
- Uses `expect_string` for conditional actions
- Configuration and IP addresses loaded from external files

## 🛠️ Tools & Environment
- **Python** (Netmiko, NAPALM)
- **GNS3 / GNS3 VM**
- **Cisco IOS routers & switches (simulated)**
- **Wireshark, CLI tools (ping, traceroute)**

## 🚀 How to Run
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install netmiko napalm
