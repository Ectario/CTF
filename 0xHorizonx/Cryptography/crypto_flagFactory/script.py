#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes

def pgcd(a,b):
    d,u,v,d1,u1,v1 = a, 1, 0, b, 0, 1
    while d1!=0:
        q = d//d1
        d, u, v, d1 , u1, v1 = d1, u1, v1, d-q*d1 , u-q*u1 ,v-q*v1
    return (u,v)

if __name__ == '__main__':
    p = 60262187560451968368998416660577
    q = 96760644340502867983334366693638726399
    E = 65537
    N = 5831008097717569085735427516825344742005710636476016496872172952472223
    D, _ = pgcd(E,(p-1)*(q-1))
    C = 1684110829310784101135485146139386330031168756507533683193091793159298

    print(long_to_bytes(pow(C,D,N)).decode('ascii'))