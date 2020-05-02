#!/usr/bin/python3 -O
"""
Filename: root13.py
Description: Caesar algorithm with a  hardcode shift equal to 13. When you
encrypt  something once and encrypt it again, you reverse the process.
Instead of making more encrypted , it becomes unencrypted.

$ root13./c.py <string> 
"""
import sys


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = sys.argv[1]
shift = 13

n = len(str_in)
str_out = ""

for i in range(n):
	c = str_in[i]
	loc = alpha.find(c)
	if __debug__:	
		print(i, c, loc)
	
	new_loc = (loc + shift)%26 
	
	str_out += alpha[new_loc]
	if __debug__:	
		print(new_loc, str_out)

print(" Obfuscated version:", str_out) 
