# network-automation-labs

## Project Overview
This project demonstrates network automation using Python with Netmiko, NAPALM, and Telnet.
It connects to multiple Cisco routers and switches via Telnet/SSH, applies configurations, retrieves device state, and handles errors automatically.

## Features
- Automates data collection and configuration tasks (VLAN, ACL, OSPF, BGP, ARP/MAC tables)
- Supports Telnet & SSH connections
- Retrieves and stores device states
- Saves and compares running-config files
- Implements logging and error handling using `traceback` and `logging`
- Performs conditional actions using `send_command_timing()` and `compare_config()`
- Loads Configuration and IP addresses from external files

## Tools & Environment
- **Python** (Netmiko, NAPALM)
- **GNS3 / GNS3 VM**
- **Cisco IOS routers & switches (simulated)**
> Note: Telnet scripts are for legacy automation scenarios.
> `telnetlib` is deprecated.
> `telnetlib3` was used for learning purposes only

## How to Run
1. Clone this repository
2. Install dependencies:
   ```bash
   apt-get install python3
   pip3 install netmiko napalm
3. Update `device` and `config` files with your device info
4. Run the script:
   ```bash
   python3 script_name.py

## Example Outputs
- Saved running-config files
- Backup configuration files
- Log files (error logs, debug logs)
- Configuration change reports
- JSON files containing operational state data

## Learning Outcomes 
- Practical experience in network automation
- Understanding of Python libraries for networking
- Hands-on practice with Cisco device management
- Experience handling network automation errors safely

## Future Improvements
- Device configuration into YAML files
- Multithreading
- Using Deepdiff module with JSON backup files
- ...

## Attribution
Some scripts in this repository are based on concepts and examples from David Bombal's Udemy course on Network Automation.
The code has been modified and extended for personal learning and lab practice.

