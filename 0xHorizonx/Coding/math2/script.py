#!/usr/bin/env python3
from typing import List
import numpy as np
import telnetlib
import re


HOST = "0xhorizon.eu"
PORT = 6789


def parse(equations : List) -> List:
    factors = []
    results = []
    for eq in equations:
        print(eq)
        if eq[0] != '-':
            eq = '+' + eq
        l = re.findall('([+-][0-9]+)', eq) # Get the numbers list from this equation
        f = [int(x) for x in l] # Cast each one in int
        factors.append(f if len(f)<7 else f[:-1]) # if there is the right member of the equation then we remove it and then append
        results.append(int(eq.split('=')[1])) # Get the right member (ie. the result)
    return factors, results

def doCalculus(numbers : List) -> np.ndarray:
    a = np.array(numbers[0])
    b = np.array(numbers[1])

    r = np.linalg.solve(a, b)
    return r

tn = telnetlib.Telnet(HOST, PORT)
data = tn.read_until(b"solutions:").decode('ascii')
equations = data.split("Example")[0].strip().split("\n")

solutions = doCalculus(parse(equations)) # Make the calculus
solutions = [round(s) for s in solutions] # Round each value

string_solutions = '{'+ f"\"a\":{solutions[3]}, \"b\":{solutions[4]}, \"c\":{solutions[5]}, \
\"x\":{solutions[0]}, \"y\":{solutions[1]}, \"z\":{solutions[2]}" + '}'

print(string_solutions)
tn.write((string_solutions+'\n').encode())
print(tn.read_until(b"}",3).decode())