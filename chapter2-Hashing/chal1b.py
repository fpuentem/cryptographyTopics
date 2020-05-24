import hashlib

# To find in a easy way the corresponding password, we use a pipe to grep
# of the first four values. In terminal:
# $ python3 chal1b.py | grep '5875'

for c1 in '0123456789':
	for c2 in '0123456789':
		p = c1 + c2
		hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
		print(p, hash)
