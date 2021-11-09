#!/usr/bin/env python3
from math import sqrt
import telnetlib

HOST = "0xhorizon.eu"
PORT = 7777

tn = telnetlib.Telnet(HOST, PORT)
data = tn.read_until(b"?>").decode('ascii')

calculus = data.replace("\n\n","\n").split('\n')[1].split()
operator = calculus[1]
result = 0

for i, e in enumerate(calculus):
    if e != operator:
        calculus[i] = int(e)

if operator == "+":
    result = calculus[0] + calculus[2]
elif operator == "/":
    result = calculus[0] / calculus[2]
elif operator == "-":
    result = calculus[0] - calculus[2]
elif operator == "*":
    result = calculus[0] * calculus[2]

tn.write((f'{round(sqrt(result),2)}\n').encode())
print(data,round(sqrt(result),2))
print(tn.read_until(b"}",3).decode())