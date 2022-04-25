import socket
s = socket.socket()

print("Socket Created")
s = socket.socket()
s.bind(('localhost', 9999))

s.listen(14)
print('Waiting for connection')
while True:
    c, addr = s.accept()

    name = c.recv(1024).decode()

    print("Connected with", addr, name, )
    c.send(bytes('Welcome to Zenith World', 'utf-8'))
    Thanks = c.recv(1024).decode()
    print(addr, Thanks, )
    c.send(bytes('How can we help you?', 'utf-8'))
    Well = c.recv(1024).decode()
    print(addr, Well, )
    c.send(bytes('Wow! That is great, We are glad to know your Interest', 'utf-8'))
    ok = input(" ")
    c.send(bytes(ok, 'utf-8'))
    Reply = c.recv(1024).decode()
    print(addr, Reply, )
    c.send(bytes('We will teach you all you need to know about Networking', 'utf-8'))
    c.close()