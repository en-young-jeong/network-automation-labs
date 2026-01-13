"""
Advanced Netmiko script to push configuration commands to Cisco IOS devices.

- Reads device IP addresses from a file
- Reads configuration commands from a file
- Prompts for SSH credentials once for all devices
- Sends configuration commands one by one to handle interactive prompts
- Handles confirmation messages (e.g. 'confirm') dynamically
- Implements detailed connection-level and runtime error handling
- Logs detailed execution and error information using the logging module
"""

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException
import logging

# Enable logging
logging.basicConfig(filename='netmiko_config_advanced.log',level=logging.DEBUG, filemode='w')

# Prompt for SSH credentials (used for all devices)
username = input("Enter your SSH username: ")
password = getpass()

# Read IP addresses and commands from files
with open('device') as f:
    devices_list = f.read().splitlines()

with open('config') as f:
    lines = f.read().splitlines()

# Iterate over each device
for IP in devices_list:
    IP = IP.strip()
    print("Connecting to device " + IP)
    
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': username,
        'password': password
   }

    # ---- Connection-level error handling ----
    try:
         net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print (f"Authentication failure {IP} ")
        continue
    except (NetMikoTimeoutException):
        print (f"Timeout {IP}")
        continue
    except (EOFError):
        print (f"End of file while attempting device {IP}")
        continue
    except (SSHException):
        print (f"SSH failure on {IP}")
        continue
    except Exception as e:
        print (f"Unexpected error on {IP}: {e}")
        continue

    # Enter configuration mode explicitly
    net_connect.config_mode()

    # ---- Command execution ----
    try:
        for command in lines:
           print(f"Config {IP} : {command}")
           output = net_connect.send_command_timing(command)
           
           # Handle interactive confirmation prompts if present
           if 'confirm' in output.lower():
               output += net_connect.send_command_timing("\n")
               
           # Print output only if the device returned meaningful text
           if output.strip():
               print(output)

    except Exception as e:
            print(f"Unexpected error on {IP}: {e}")
    # Close the SSH session for this device
    net_connect.disconnect()
