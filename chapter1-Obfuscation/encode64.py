#!/usr/bin/python3

import base64
'''
   A		  B			 C	   		 D
01000001 | 01000010 | 01000011 | 01000100

010000-010100-001001-000011-010001-00 
010000-010100-001001-000011-010001-000000
16	  -20    -9     -3     -17    -	0==
QUJDRA==\n
'''

# string len 3, 3*8 = 24 -> 24%6 = 0
print(base64.b64encode("ABC".encode(encoding = 'UTF-8',errors = 'strict')))

# string len 4,  4*8 = 32 -> 32%6 = 2
print(base64.b64encode("ABCD".encode(encoding = 'UTF-8',errors = 'strict')))

# string len 4 + 2(zeros),  6*8 = 48 -> 48%6 = 0
# We have no padding here - there's a filling of binary zeros.
print(base64.b64encode("ABCD".encode(encoding='UTF-8', errors='strict') + bytes([0]) + bytes([0])))
