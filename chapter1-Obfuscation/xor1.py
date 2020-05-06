#!/usr/bin/python3 -O
import sys

text = sys.argv[1]
key = sys.argv[2]

n = len(text)

for i in range(n):
	t = text[i]
	k = key[i%len(key)]
	x = ord(k) ^ ord(t)
	y = chr(x)
	print(t, k, x, y)
