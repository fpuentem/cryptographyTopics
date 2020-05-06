#!/usr/bin/python3 -O
import sys

text = sys.argv[1]
key = sys.argv[2]

n = len(text)
cipher = ''

for i in range(n):
	t = text[i]
	k = key[i%len(key)]
	x = ord(k) ^ ord(t)
	cipher = cipher + chr(x)
print(text, key, cipher.encode('utf-8'))
