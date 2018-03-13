import socket

server = socket.socket()
server.bind( ('localhost',8000))
server.listen(5)

while True:
    conn, addr = server.accept()
    print "Connection established"
    print addr

    msg = conn.recv(1024)
    print msg

    conn.send("Connection established")
    conn.close()