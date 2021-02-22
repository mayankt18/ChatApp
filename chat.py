import socket

from tkinter import *

import threading

import sys


class Server:
    window = Tk()

    window.title("chat app")



    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):

        self.sock.bind(('0.0.0.0', 1234))

        self.sock.listen(1)

        



    def handler(self, c, a): # for receiving messages

        while True:

            data = c.recv(20)

            print(str(data, 'utf-8'))


    def send_msg(self, c, a, name):  #for sending messages
        while True:
            msg = input("")
            s_msg = name + ': ' + msg
            c.send(bytes(s_msg, 'utf-8'))

    def run(self):

        name = input("enter your name : ")

        print("Listening for connections...")

        running = True

        while running:

            c, a = self.sock.accept()

            cThread = threading.Thread(target=self.handler, args=(c, a))

            cThread.daemon = True

            cThread.start()

            iThread = threading.Thread(target=self.send_msg, args=(c, a, name))

            iThread.daemon = True

            iThread.start()

            if 

            print(str(a[0]) + ':' + str(a[1]), " connected.")



class Client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self, connected, name):  #for sending messages

        while connected:
            msg = input("")
            s_msg = name + ': ' + msg
            self.sock.send(bytes(s_msg, 'utf-8'))


    def __init__(self, address):

        name = input("Enter your name : ")

        self.sock.connect((address, 1234))

        connected = True

        iThread = threading.Thread(target=self.send_msg, args=[connected, name])

        iThread.daemon = True

        iThread.start()

        

        while connected:

            data = self.sock.recv(20)

            print(str(data, 'utf-8'))


class TServer:

    def __init__(self, port, filename):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.filename = filename

        self.port = port

        self.file = open(filename, 'rb')

        self.filedata = self.file.read(1024)

        self.sock.bind(('0.0.0.0', self.port))

        self.sock.listen(1)

        while True:

            c , a = self.sock.accept()
        
            c.send(self.filedata)

            c.close()

            break

        print("file has been sent sucessfully...")


class TClient:
    
    def __init__(self, address, port, filename):
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.filename = filename

        self.sock.connect((address, 1234))

        while True:

            file = open(filename, 'wb')
            
            file_data = self.sock.recv(1024)

            file.write(file_data)

            file.close()

            break

        print("file has been received sucessfully...")

#for sending = python xyz.py port filename
#for receiving = python xyz.py ip port filename

        
if (len(sys.argv) == 2):

    client = Client(sys.argv[1])

elif (len(sys.argv) == 1):

    server = Server()

    server.run()

elif (len(sys.argv) == 3):
    
    sender = TServer(int(sys.argv[1]), sys.argv[2])

else:
    receiver = TClient(sys.argv[1], int(sys.argv[2]), sys.argv[3])
