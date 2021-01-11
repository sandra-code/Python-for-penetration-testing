#!/usr/bin/python3

import socket

#AF_INET - using IPv4
#SOCK_STREAM - what type of protocol is being used, for example tcp or udp (tcp for this case)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 555

#binding the port and the host tot the socket
serversocket.bind((host, port))

#listen the tcp connection
#parameter 3 - how many requests we allow
serversocket.listen(3)

while True:
    #establish the connection
    clientsocket, address = serversocket.accept()

    print("Received connection from " % str(address))

    #close the socket
    message = "Hi! Thanks for connecting to the server " +  "\r\n"

    clientsocket.send(message)

    clientsocket.close