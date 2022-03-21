from datetime import datetime
from email import message
import logging
import socket
import sys
from _thread import *
import os
import logging
import time

archivo = int(input('Seleccione el tamaño del archivo. 1 para 250Mb, 2 para 100Mb: ').rstrip())
peso = ''
if(archivo == 1):
    peso = '250MB'
elif(archivo == 2):
    peso = '100MB'

formated_date_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
logging.basicConfig(filename='Logs/'+formated_date_time+'-log.txt', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger('Logs/'+str(formated_date_time)+'-log')
log.setLevel(logging.DEBUG)
log.debug('Archivo: file' + str(archivo))
log.debug('Peso del archivo: ' + peso)


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
    tiempoInicio = time.time()
    connection.send(str.encode('Welcome to the Server'))
    try:
        print('client connected:', client_address)
        with open("file2" , "rb") as f:
            data = f.read()
        while True:
            if data:
                connection.sendall(data)
            else:
                print('Entra al break')
                break
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