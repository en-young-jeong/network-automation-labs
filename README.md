# network-automation-labs

## Project Overview
This project demonstrates network automation using Python with Netmiko and NAPALM.
It connects to multiple Cisco routers and switches via Telnet/SSH, applies configurations,
and retrieves device states automatically.

## Features
- Automates configuration tasks (VLAN, ACL, OSPF, BGP, ARP/MAC tables)
- Supports Telnet & SSH connections
- Saves and compares running-config files
- Implements logging, error handling, and multithreading
- Uses `expect_string` for conditional actions
- Configuration and IP addresses loaded from external files

## Tools & Environment
- **Python** (Netmiko, NAPALM)
- **GNS3 / GNS3 VM**
- **Cisco IOS routers & switches (simulated)**

## How to Run
1. Clone this repository
2. Install dependencies:
   ```bash
   apt-get install python3
   pip3 install netmiko napalm
3. Update `device` and `config` with your device info
4. Run the script:
   ```bash
   python3 script_name.py

## Example Outputs
- Saved running-config files
- Log files
- ...

## Learning Outcomes 
- Practical experience in network automation
- Understanding of Python libraries for networking
- Hands-on practice with Cisco device management

## Future Improvements
- Log files with error handling
- Comparison reports for config changes
- Device configuration into YAML files
- ...

## Attribution
Some scripts in this repository are based on concepts and examples from
David Bombal's Udemy course on Network Automation.
The code has been modified and extended for personal learning and lab practice.

