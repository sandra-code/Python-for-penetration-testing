#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 555

clientsocket.connect((host, port))

#maximum amount of data through our port
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
