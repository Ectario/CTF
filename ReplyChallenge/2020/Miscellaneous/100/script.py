#!usr/bin/env python3
import binascii

with open('doc.txt', 'r') as file:
    doc = file.read().replace("\n",'')
    print(binascii.unhexlify(f'0{doc}').decode('utf8','replace'))