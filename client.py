import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    with open("file2", "rb") as f:
        message = f.read()
    
        #message = 'This is the message.  It will be repeated.'.encode()
        #print('sending "%s"' % message)
        print('sending message')

        print("finished sending")
        sock.sendall(message)
    
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            #print('received "%s"' % data)
        print("received everything")
finally:
    sock.close()
