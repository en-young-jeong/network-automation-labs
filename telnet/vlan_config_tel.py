"""
Basic Telnet automation script for configuring VLANs
on multiple network devices.

- Reads device IP addresses from a file
- Connects to multiple network devices via Telnet
- Configures VLANs on multiple network devices

Note:
- telnetlib is deprecated
- Consider using a third-party library such as telnetlib3
  (pip install telnetlib3)
"""

from getpass import getpass
import telnetlib3

# Store user-provided username and password in parameters for use across all devices
user = input("Enter your remote account: ")
password = getpass()

f = open ('device')
for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib3.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    
# Send individual commands
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
