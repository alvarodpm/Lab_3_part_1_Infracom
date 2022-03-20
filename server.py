from datetime import datetime
from email.utils import format_datetime
import socket
import sys
from _thread import *
from sympy import false, true

# Create log file
#formated_datetime = datetime.strftime('%Y-%m-%d-%H-%M-%S')


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

ThreadCount = 0

def threaded_client(connection, client_address):
    global ThreadCount
    connection.send(str.encode('Welcome to the Server'))
    try:
        print('client connected: ', client_address)
        data = connection.recv(16384)
        if data:
            print('FFFFFF')
            connection.sendall(data)
        else:
            while True:
                if 'termino' == connection.recv(16384):
                    print("sent everything to ", client_address)
                    break
    except:
        connection.close()
    finally:
        ThreadCount -= 1
        print('Thread finished. ' + str(ThreadCount) + ' threads restantes')
        connection.close()


while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    
    print('Connected to: ' + client_address[0] + ':' + str(client_address[1]))
    start_new_thread(threaded_client, (connection, client_address))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
sock.close()