import socket
import sys
from _thread import *
import os
import threading 

archivo = int(input('Seleccione el tamaño del archivo. 1 para 250Mb, 2 para 100Mb: ').rstrip())
NumClientes = int(input('Seleccione el número de clientes que a los que desea enviar el archivo. Máximo 24: ').rstrip())
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

ThreadCount = 0

def threaded_client(connection):
    global ThreadCount
    connection.send(str.encode('Welcome to the Server'))
    print ("Entraa uwu")
    try:
        with open("file2", "rb") as f:
            message = f.read()
            print('sending message')
            sock.sendall(message)
            print("finished sending")
            #amount_received = 0
            #amount_expected = len(message)
            #while amount_received < amount_expected:
            #data = sock.recv(16384)
            #amount_received += len(data)
            #print('received: ' + str(amount_received) + ' expected: ' + str(amount_expected))
        #print("received everything")
    except:
        connection.close()
    finally:
        ThreadCount -= 1
        connection.close()

list_threads=[]
while ThreadCount<NumClientes:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('Se recibe la solicutud de conexión de: ' + client_address[0] + ':' + str(client_address[1]))
    list_threads.append((client_address,connection))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
for i in list_threads:
    client_address=i[0]
    connection=i[1]
    print("se inicia el thread del puerto ", client_address[1])
    start_new_thread(threaded_client, (connection, client_address ))
sock.close()
