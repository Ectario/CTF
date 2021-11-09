# INFO 

We have 2 files. encrypt.py and flag.txt. It appears like a xoring with random number and the flag.txt (which seems to be hexadecimal string).

The title tells us 'KnownPlainText', so we probably have to use a text that we know and which is unencrypted. By thinking about it we know that the flag starts with 'horiz0nx'.

Moreover, by observing the encrypt.py script, we notice that this one uses an encryption key of 8 bytes. Since the encryption is an XOR (symmetric encryption). We can deduce the 8 byte key in XORing 'horiz0nx' and the first 8 char of the flag.txt.

Explanation :

+ <=> XOR operator

plaintext + key = encrypted text

_and xor being symmetrical:_

plaintext + encrypted text = key


So we got the idea.

Let's code! 

# Script 

- get flag.txt without the hexa format
- xoring what we know to get the key
- xoring the entire flag with the key which is now recovered

# Gotcha !

flag = horiz0nx{plZ_us3_0n3_t1me_p4d:)}


