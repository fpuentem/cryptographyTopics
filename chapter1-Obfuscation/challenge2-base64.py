#!/usr/bin/python3

import base64

# Encode and decode 'ABC' message
msg_encode = base64.b64encode("ABC".encode(encoding = 'UTF-8',errors = 'strict'))
msg_decode = base64.b64decode(msg_encode)

print("encode message: {}".format(msg_encode))
print("decode message: {}".format(msg_decode))

# Decode message 'U2FtcGxliHRlenHQ'
msg_encode = 'U2FtcGxliHRleHQ='
msg_decode = base64.b64decode(msg_encode)
print("encode message: {}".format(msg_encode))
print("decode message: {}".format(msg_decode))

# Decode message 'VGhpcyBpcyB0b28gZWFzeQ=='
msg_encode = 'VGhpcyBpcyB0b28gZWFzeQ=='
msg_decode = base64.b64decode(msg_encode)
print("encode message: {}".format(msg_encode))
print("decode message: {}".format(msg_decode))

# Decode message, encoded several times 'VWtkc2EwbEliSFprVTJeFl6SlZaMWxUUW50aU1qbDNVSGM5UFFvPQo='
n = 10
msg_encode = 'UVVKRFJBPT0=' #'VWtkc2EwbEliSFprVTJeFl6SlZaMWxUUW5OaU1qbDNVSGM5UFFvP'
print(type(msg_encode))

for i in range(n):
    print('Deep of decode: {}'.format(i))
    msg_decode = base64.b64decode(msg_encode)
    print(msg_decode)
    msg_encode = msg_decode
