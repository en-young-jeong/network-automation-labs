"""
This script reads device IP addresses from a file
connects to multiple network devices via Telnet,
retrieves the running configuration,
writes the output to local files
(telnetlib is deprecated. Use the third-party library. 'pip3 install telnetlib3')
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
