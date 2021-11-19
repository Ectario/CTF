#!/usr/bin/env python3

import hashlib

# hashes from https://github.com/spaze/hashes

with open('/home/ectario/Documents/tools/projects/hashes/md5.md', encoding='latin-1') as file:
    file = file.read().split("\n")
    i = 0
    mypwd = file[0].split(":")[0]
    hashed = hashlib.md5(mypwd.encode()).hexdigest()
    while i < len(file)-1:
        if hashed == "0e791913724986920161109490945425" :
            print()
            print(f"WOW : {mypwd}")
            break
        print(f"[+] {mypwd} : {hashed}")
        i+=1
        mypwd = file[i].split(":")[0]
        hashed = hashlib.md5(mypwd.encode()).hexdigest()
