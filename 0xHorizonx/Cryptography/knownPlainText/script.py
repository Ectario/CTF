#!/usr/bin/env python3
import os
from Crypto.Util.strxor import strxor


FLAG = bytes.fromhex(open("flag.txt", "r").read()) # Reading the file and Reverse the c.hex() in the encrypt.py
print('8 first char =',FLAG[:8])

key = strxor(FLAG[:8], b'horiz0nx')
print('key =',key)

result = ''


for i in range(len(FLAG)):
    result += chr(FLAG[i] ^ key[i % 8])

print('flag =',result)
