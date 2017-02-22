import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8073))
#data = sk.recv(1024)
#print(data)
while True:
    inp = input(">>>")
    sk.sendall(bytes(inp))
    #print(sk.recv(1024))
sk.close()
