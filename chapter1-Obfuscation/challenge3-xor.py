#!/usr/bin/python3

# 
# The correct message encrypted is 'snw{fzs' -> 'EXAMPLE'
#
import sys

#text = sys.argv[1]
#n = len(text)
#
#for k in '0123456789':
#	clean = ''
#	for i in range(n):
#		t = text[i]
#		x = ord(k) ^ ord(t)
#		clean += chr(x)
#
#	print(k, clean)


text = '70155d5c45415d5011585446424c'
n = len(text)

for i in '0123456789':
	for j in '0123456789':
		key = i + j
		clean = ''
		for m in range(n):
			t = text[m]
			k = key[m % len(key)]
			x = ord(k) ^ ord(t)	
#			print(t, k, x)
#			print(type(t), type(k), type(x))
			clean += chr(x)
		print(key, clean.encode('ascii'))

		
		
