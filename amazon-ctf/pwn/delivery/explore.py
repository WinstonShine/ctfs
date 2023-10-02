#!/usr/bin/python3

payload = 'a' * 32
i = 0
while i < 26:
    payload += chr(i + 65) * 4
    i+=1

print(payload)
