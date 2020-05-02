#!/usr/bin/python3 -O
"""
Filename: caeser.py
Description: Caesar algorithm with a  variable shift.
$ ./ceaser.py <string> <shift>
"""
import sys


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str_in = sys.argv[1]
shift = int(sys.argv[2])

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
