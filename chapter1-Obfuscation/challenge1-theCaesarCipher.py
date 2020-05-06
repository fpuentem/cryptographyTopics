#!/usr/bin/python3

import sys

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encryp_txt = sys.argv[1]

n = len(encryp_txt)

for shift in range(26):
	str_out = ""
	
	for i in range(n):
		c = encryp_txt[i]
		loc = alpha.find(c)
		newloc = (loc + shift)%26
		str_out += alpha[newloc]

	print(shift, str_out)
