#!/usr/bin/env python3
from AESAlg import *
import sys
import hashlib

class SuperSafeCrypto(object):
    def __init__(self, keys):

        assert len(keys) == 4
        self.keys = keys
        self.ciphers = []
        for x in range(4):
            a = AESAlg(keys[x])
            self.ciphers.append(a)

    def multiCipher(self, pt):
        base = self.ciphers
        x        = base[0].enc(pt)
        y        = base[1].enc(x)
        z        = base[2].enc(y)
        ct = base[3].enc(z)
        return ct

    def multiDecipher(self, ct):
        base = self.ciphers
        z      = AESAlg.depadding(base[3].dec(ct))
        y        = AESAlg.depadding(base[2].dec(z))
        x        = AESAlg.depadding(base[1].dec(y))
        pt  = AESAlg.depadding(base[0].dec(x))
        return pt

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./hansome.py [FILENAME] [PASSWORD]")
        exit()

    fName = sys.argv[1]
    pt = open(fName, "rb").read()

    password = sys.argv[2].encode('utf-8')
    assert len(password) == 8

    l = len(password) // 4
    keys = [ 
        hashlib.sha256(password[0:l]).digest(),
        hashlib.sha256(password[l:2*l]).digest(),
        hashlib.sha256(password[2*l:3*l]).digest(),
        hashlib.sha256(password[3*l:4*l]).digest(),
    ]
    c = SuperSafeCrypto(keys)

    ct = c.multiCipher(pt)
    pt2 = c.multiDecipher(ct)
    assert pt == pt2

    open(fName+".enc", "wb").write(ct)
