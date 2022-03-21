from email import message
import socket
import sys
from _thread import *
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

ThreadCount = 0

archivo = int(input('Seleccione el tamaño del archivo. 1 para 250Mb, 2 para 100Mb: ').rstrip())


def threaded_client(connection):
    global ThreadCount
    connection.send(str.encode('Welcome to the Server'))
    try:
        print('client connected:', client_address)
        with open("file" + str(archivo), "rb") as f:
            data = f.read()
        while True:
            #data = connection.recv(16384)
            #print('received "%s"' % data)
            if data:
                connection.sendall(data)
            else:
                break
        print("sent everything to", client_address)
    except:
        connection.close()
    finally:
        ThreadCount -= 1
        print('Threads faltantes: ' + str(ThreadCount))
        connection.close()

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    
    print('Connected to: ' + client_address[0] + ':' + str(client_address[1]))
    start_new_thread(threaded_client, (connection, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
sock.close()
