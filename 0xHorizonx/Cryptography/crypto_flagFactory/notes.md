# INFO

We have :

N = 5831008097717569085735427516825344742005710636476016496872172952472223
E = 65537
C = 1684110829310784101135485146139386330031168756507533683193091793159298

Then, instinctively it appears like RSA problem. C as the encrypted message, E as the public key, N the modulus in the RSA formula.

We know that N = p*q where p and q are prime number.

We need to find them.

With online tool we can see that : 

- p=60262187560451968368998416660577
- q=96760644340502867983334366693638726399

Let's check if they're prime numbers. (with dCode site) --> Yes it is, nice.

Next, we need to calculate the natural number D, which is the inverse of E modulo φ(n), (and strictly less than φ(n)), called _the decryption exponent_; D can be calculated efficiently by the extended Euclidean algorithm: 

=> E * D = 1 [φ(n)], where φ(n)=(p-1)*(q-1)
=> D * E + k * φ(n) = 1, where k\in\Z

Let's make euclidean_algo(E, φ(n)) to get the D factor. (with `script.py`)

We get the following result:
D = 558571018470038279448967971537130274907431766563723007412436136409985

Alright, we just have to get C^D % N (RSA decipher formula) and translate it to string. (with `script.py`)

# Gotcha !

horiz0nx{m4th3m4tics_rs4}