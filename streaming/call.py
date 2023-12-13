"""
A module for call in the streaming package.
"""

from socket import socket

with open('request.txt', 'rb') as fp:
    data: bytes = fp.read()

sock: socket = socket()
sock.connect(('httpbin.org', 80))
sock.sendall(data)

chunks: list[bytes] = list(iter(lambda: sock.recv(1024), b''))
reply: bytes = b''.join(chunks)
print(reply.decode())
