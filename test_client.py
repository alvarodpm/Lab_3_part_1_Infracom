import os
from threading import Thread

def task():
    os.system('python client.py 127.0.0.1')

for i in range(26):
	print("new thread")
	new_thread = Thread(target=task)
	new_thread.start()