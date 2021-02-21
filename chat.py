import socket

import threading

import sys



class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):

        self.sock.bind(('0.0.0.0', 1234))

        self.sock.listen(1)

        



    def handler(self, c, a): # for receiving messages

        while True:

            data = c.recv(1024)

            print(str(data, 'utf-8'))


    def send_msg(self, c, a, name):  #for sending messages
        while True:
            msg = input("")
            s_msg = name + ': ' + msg
            c.send(bytes(s_msg, 'utf-8'))

    def run(self):

        name = input("enter your name : ")

        print("Listening for connections...")

        while True:

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

            data = self.sock.recv(1024)

            print(str(data, 'utf-8'))



if (len(sys.argv) > 1):

    client = Client(sys.argv[1])

else:

    server = Server()

    server.run()