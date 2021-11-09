# GIVEN FOR THE CHALL'
import os
from Crypto.Util.strxor import strxor


FLAG = open("flag.txt", "rb").read()

key = os.urandom(8) * 20
c = strxor(FLAG, key[:len(FLAG)])
print(c.hex())
