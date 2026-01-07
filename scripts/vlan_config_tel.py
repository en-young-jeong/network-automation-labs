"""
This script reads device IP addresses from a file,
connects to multiple network devices via Telnet,
configures Vlans on multiple network devices
(telnetlib is deprecated. Use the third-party library. 'pip3 install telnetlib3')
"""

import getpass
import telnetlib3

user = input("Enter your remote account: ")
password = getpass.getpass()

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
    
#what you want to configure?
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
