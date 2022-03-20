import os
from threading import Thread

archivo = int(input('Seleccione el tamaño del archivo. 1 para 250Mb, 2 para 100Mb: ').rstrip())
NumClientes = int(input('Seleccione el número de clientes que a los que desea enviar el archivo. Máximo 24: ').rstrip())
def task():
    os.system('python client.py 127.0.0.1 {} {}'.format(archivo, NumClientes))

def task_receive():
	os.system('python client_receive.py 127.0.0.1 {}'.format(archivo))

for i in range(NumClientes):
	print("new client_recieve: " + str(i))
	new_thread = Thread(target=task_receive)
	new_thread.start()	

print("new cliente: " + str(1))
new_thread = Thread(target=task)
new_thread.start()