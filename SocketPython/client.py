import socket

client = socket.socket()
client.connect( ('localhost',8000))

client.send("Hello, server!!! I am a client.")

msg = client.recv(1024)
print msg

client.close()