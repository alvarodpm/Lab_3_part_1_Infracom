import os
from threading import Thread

NumClientes = int(input('Seleccione el número de clientes que a los que desea enviar el archivo. Máximo 24: ').rstrip())

def task():
    os.system('python client.py 127.0.0.1')

for i in range(NumClientes): 
	print("new thread")
	new_thread = Thread(target=task)
	new_thread.start()
