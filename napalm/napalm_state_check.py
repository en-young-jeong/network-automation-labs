"""
Basic NAPALM script for collecting operational data from network devices.

- Connects to multiple network devices using NAPALM
- Retrieves common operational state information
- Demonstrates vendor-agnostic, read-only automation
- Stores collected data in structured JSON files
- Handles basic execution errors
"""

from getpass import getpass
from napalm import get_network_driver
import json
import traceback

# NAPALM driver: Cisco IOS -> 'ios', Juniper -> 'junos', Arista -> 'eos'
driver = get_network_driver('ios')

# Prompt for SSH credentials (used for all devices)
username = input('Enter your SSH username: ')
password = getpass()

# Read IP addresses from file
with open('device') as f:
    devices_list = f.read().splitlines()

# Iterate over each device
for IP in devices_list:
    try:
        IP = IP.strip()
        print('Connecting to device ' + IP)
        
        # Open NAPALM connection
        ios = driver(IP, username, password)
        ios.open()
        
        # Collect device information
        output = {}
        output["facts"] = ios.get_facts()
        output["interfaces"] = ios.get_interfaces()
        output["mac_table"] = ios.get_mac_address_table()
        output["arp_table"] = ios.get_arp_table()
        output["bgp_neighbors"] = ios.get_bgp_neighbors()

        # Ping test to 'google.com'
        # From napalm 5.0.0, use an IP address instead of a domain name
        output["ping_test"] = ios.ping('8.8.8.8')

        # Write collected data to a per-device JSON file
        with open(f"{IP}_state.json", "w") as f:
            json.dump(output, f, indent=4)
            
        # Close connection
        ios.close()
        
    # Handle connection or execution errors
    except Exception as e:
         print(f"Error occurred on {IP}: {e}")
         with open("error_log.txt","w") as log:
             traceback.print_exc(file=log)
