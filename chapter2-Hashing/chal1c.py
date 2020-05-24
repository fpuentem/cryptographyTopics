import hashlib

# To find in a easy way the corresponding password, we use a pipe to grep
# of the first four values. In terminal:
# $ python3  chal1c.py | grep '0342db37d0'
# It takes s few seconds, We got the following with time command:
# real	0m22,814s
# user	0m23,776s
# sys	0m0,596s


for c1 in '0123456789':
	for c2 in '0123456789':
		for c3 in '0123456789':
			for c4 in '0123456789':
				for c5 in '0123456789':
					for c6 in '0123456789':
						for c7 in '0123456789': 		
							p = c1 + c2 + c3 + c4 + c5 + c6 + c7
							hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
							print(p, hash)
