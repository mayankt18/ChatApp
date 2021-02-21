import socket

import threading

import sys



class Server:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):

        self.sock.bind(('0.0.0.0', 1234))

        self.sock.listen(1)

        print("Listening for connections...")



    def handler(self, c, a): # for receiving messages

        while True:

            data = c.recv(1024)

            print(str(data, 'utf-8'))


    def send_msg(self, c, a):  #for sending messages
        while True:

            c.send(bytes(input(""), 'utf-8'))

    def run(self):

        while True:

            c, a = self.sock.accept()

            cThread = threading.Thread(target=self.handler, args=(c, a))

            cThread.daemon = True

            cThread.start()

            iThread = threading.Thread(target=self.send_msg, args=(c , a))

            iThread.daemon = True

            iThread.start()

            print(str(a[0]) + ':' + str(a[1]), " connected.")



class Client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_msg(self):  #for sending messages

        while True:

            self.sock.send(bytes(input(""), 'utf-8'))

    def handler(self, sock):  # for receiving messages

        while True:

            data = sock.recv(1024)

            print(str(data, 'utf-8'))

    def __init__(self, address):

        self.sock.connect((address, 1234))

        cThread = threading.Thread(target=self.handler, args=[self.sock])

        cThread.daemon = True

        cThread.start()



        iThread = threading.Thread(target=self.send_msg)

        iThread.daemon = True

        iThread.start()

        

        while True:

            data = self.sock.recv(1024)

        
            print(str(data, 'utf-8'))



if (len(sys.argv) > 1):

    client = Client(sys.argv[1])

else:

    server = Server()

    server.run()