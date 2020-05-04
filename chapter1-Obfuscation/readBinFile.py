import base64

with open('./binarydata', 'rb') as f:
    data = f.read()

# Read data
print(data)

# Data encoded
print(base64.b64encode(data))
