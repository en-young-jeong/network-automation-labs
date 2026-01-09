"""
Basic Netmiko script to push configuration commands to Cisco IOS devices.

- Reads device IP addresses from a file
- Reads configuration commands from a file
- Prompts for SSH credentials per device
- Applies configuration to each device
- Logs errors for troubleshooting
"""

from getpass import getpass
from netmiko import ConnectHandler
import traceback

# Open and read IP addresses from file
with open('device') as f:
    devices_list = f.read().splitlines()

with open('config') as f:
    lines = f.read().splitlines()

# Log errors if needed
with open("error_log.txt","w") as log:
    for IP in devices_list:
        try:
            IP=IP.strip()
            print ("Connecting to device " + (IP))
            
# Prompt for credentials to demonstrate per-device connection handling
            username = input("Enter your SSH username: ")
            password = getpass()

            ios_device = {
                'device_type': 'cisco_ios',
                'ip': IP,
                'username': username,
                'password': password
            }

            net_connect = ConnectHandler(**ios_device)
            output = net_connect.send_config_set(lines)
            print (output)
            net_connect.disconnect()

        except Exception as e:
            print(f"Error occurred on {IP}: {e}")
            traceback.print_exc(file=log)
            continue


