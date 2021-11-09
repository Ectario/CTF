#!/usr/bin/env python3
import base64
import telnetlib

HOST = "0xhorizon.eu"
PORT = 9999

# Connecting
tn = telnetlib.Telnet(HOST, PORT)
data = tn.read_until(b":").decode('ascii')

# Parsing
blob = data.split("('")[1].split("')")[0]

# Decoding
while not "password" in blob:
    blob = base64.b64decode(blob).decode()

# Sending
password = blob.split(': ')[1]
tn.write((f'{password}\n').encode())


print(blob," => password =", password)
print(tn.read_until(b"}",3).decode())    