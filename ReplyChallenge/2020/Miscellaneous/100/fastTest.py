#!usr/bin/env python3

test = int(input("[+] 4 digit (between 0-9) : "))

with open('2attempt.txt') as file:
    file = [int(i) for i in file.read().split('\n')]
    if test in file:
        print("[+] Already tested.")
    else:
        print("[+] NOT Tested. Added in toTest.txt")
        content = ''
        with open('toTest.txt', 'r') as f:
            content = f.read()
        with open('toTest.txt', 'w') as f:
            content += f'\n{test}'
            f.write(content)
