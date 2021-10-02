#!/usr/bin/env python3
import sys

def decrypt(message, key):
    with open(message, 'rb') as content_file:
        content = content_file.read()
    unciphertext = list(' ' * 256)
    for i in range(0,256):
        new_pos = (3**(key+i)) % 257
        unciphertext[i] = ((content[new_pos-1])^i)^(new_pos-1)
    return bytes(unciphertext)

def main():
    for i in range(1,257):
        unciphertext = decrypt(sys.argv[1], i)
        if unciphertext.decode('utf8','replace').find('FLG') > 0:
            print(unciphertext.decode('utf8','replace'))

if __name__ == '__main__':
    main()

