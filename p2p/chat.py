import socket

import threading

import sys

import tqdm

import os

BUFFER = 1024


class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):

        self.sock.bind(('0.0.0.0', 1234))

        self.sock.listen(1)

        



    def handler(self, c, a): # for receiving messages

        while True:

            data = c.recv(BUFFER)

            print(str(data, 'utf-8'))


    def send_msg(self, c, a, name):  #for sending messages
        while True:
            msg = input("")

            if msg == "!send":

                sender = FtClient()

            elif msg == "!accept":

                receiver = FtServer()


            else:

                s_msg = name + ': ' + msg
                
                c.send(bytes(s_msg, 'utf-8'))

    def run(self):

        name = input("enter your name : ")

        print("Listening for connections...")

        print("you can send files by typing !send and accept files by typing !accept")

        running = True

        while running:

            c, a = self.sock.accept()

            cThread = threading.Thread(target=self.handler, args=(c, a))

            cThread.daemon = True

            cThread.start()

            iThread = threading.Thread(target=self.send_msg, args=(c, a, name))

            iThread.daemon = True

            iThread.start()

            print(str(a[0]) + ':' + str(a[1]), " connected.")



class Client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self, connected, name):  #for sending messages

        while connected:
            msg = input("")

            if (msg == "!send"):

                sender = FtClient()

            elif msg == "!accept":

                receiver = FtServer()

            else:
            
                s_msg = name + ': ' + msg
                
                self.sock.send(bytes(s_msg, 'utf-8'))


    def __init__(self, address):

        name = input("Enter your name : ")

        self.sock.connect((address, 1234))

        print(f"connected to {address}")

        print("you can send files by typing !send and accept files by typing !accept")

        connected = True

        iThread = threading.Thread(target=self.send_msg, args=[connected, name])

        iThread.daemon = True

        iThread.start()

        

        while connected:

            data = self.sock.recv(BUFFER)

            print(str(data, 'utf-8'))


class FtServer:
    
    def __init__(self):

        SERVER_HOST = "0.0.0.0"
        SERVER_PORT = 5001
        
        BUFFER_SIZE = 1024
        SEPARATOR = "<SEPARATOR>"
        

        s = socket.socket()

        s.bind((SERVER_HOST, SERVER_PORT))

        s.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

        client_socket, address = s.accept() 

        print(f"[+] {address} is connected.")

        received = client_socket.recv(BUFFER_SIZE).decode()
        
        filename, filesize = received.split(SEPARATOR)

        filename = os.path.basename(filename)

        location = input("Enter complete path to where you want to save the file : ")

        file = location + "\\" + filename

        filesize = int(filesize)

        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(file, "wb") as f:
            while True:
                
                bytes_read = client_socket.recv(BUFFER_SIZE)
                
                if not bytes_read:    
                    
                    break
                
                f.write(bytes_read)
                
                progress.update(len(bytes_read))


        client_socket.close()

        s.close()


class FtClient:

    def __init__(self):

        SEPARATOR = "<SEPARATOR>"
            
        BUFFER_SIZE = 1024
            
        host = input("Enter receiver's ip address: ")
        
        port = 5001
        
        filename = input("Enter file name : ")
        
        filesize = os.path.getsize(filename)
        
        s = socket.socket()
        
        print(f"Connecting to {host}:{port}")
        
        s.connect((host, port))
        
        print("Connected.")
        
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())
        
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(filename, "rb") as f:
            while True:
                
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    
                    break
                
                s.sendall(bytes_read)
                
                progress.update(len(bytes_read))
        
        s.close()




        
if (len(sys.argv) > 1):

    client = Client(sys.argv[1])

else:

    server = Server()

    server.run()
