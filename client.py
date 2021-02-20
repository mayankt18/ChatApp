import socket

print("Client Server...")

s = socket.socket()

s_host = input("Enter server IP address: ")
name = input("Enter your name: ")

port = 6969
buff = 1024

print("Trying to connect to server...")

s.connect((s_host, port))
print("connected...")

s.send(name.encode())

s_name = s.recv(buff)
s_name = s_name.decode()
print(f"{s_name} has joined...")
print("Enter !bye to exit.")


connected = True
while connected:
    message = s.recv(buff)
    message = message.decode()
    print(s_name, '> ', message)
    
    message = input("You >")
    if message == "!bye":
        message = "See you next time..."
        s.send(message.encode())
        connected = False
    s.send(message.encode())
s.close()
