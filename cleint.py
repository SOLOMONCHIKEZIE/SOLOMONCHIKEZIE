import socket
c = socket.socket()
c.connect(('localhost', 9999))
name = input("What is your name")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024). decode())
Thanks = input(" ")
c.send(bytes(Thanks, 'utf-8'))

print(c.recv(1024). decode())
Well = input(" ")
c.send(bytes(Well, 'utf-8'))
print(c.recv(1024). decode())
print(c.recv(1024). decode())
print(c.recv(1024). decode())
Reply = input(" ")
c.send(bytes(Reply, 'utf-8'))
print(c.recv(1024). decode())
print(c.recv(1024). decode())
