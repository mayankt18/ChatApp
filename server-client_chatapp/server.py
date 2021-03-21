import socket

print("setting up server...")

s = socket.socket()

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

port = 6969
buff = 1024

s.bind((host_name,port))
print(host_name , ip)

name = input("Enter your name : ")
s.listen(1)
print("Waiting for connections ...")

c , addr = s.accept()

print(f"Received connection form {addr}")
print("connection established")

c_name = c.recv(buff)
c_name = c_name.decode()
print(f"{c_name} has connected")

print("press !bye to leave chat room")
c.send(name.encode())

connected = True
while connected:
    message = input("You > ")
    if message == "!bye":
        message = "See you next time..."
        c.send(message.encode())
        connected = False
    c.send(message.encode())
    
    message = c.recv(buff)
    message = message.decode()
    print(c_name , '> ',message)
s.close()
