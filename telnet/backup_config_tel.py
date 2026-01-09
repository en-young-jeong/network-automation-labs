"""
Basic Telnet automation script for retrieving running configurations
from multiple network devices.

- Reads device IP addresses from a file
- Connects to multiple network devices via Telnet
- Retrieves the running configuration
- Writes the output to local files

Note:
- telnetlib is deprecated
- Consider using a third-party library such as telnetlib3
  (pip install telnetlib3)
"""

import getpass
import telnetlib3

user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ('device')

for IP in f:
    IP=IP.strip()
    print ("Get running config from Switch " + (IP))
    HOST = IP
    tn = telnetlib3.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
