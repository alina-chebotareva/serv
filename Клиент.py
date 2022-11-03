#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
HOST = 'localhost'
PORT = 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Клиент подключен')
while True:
    user_input = str(input()) 
    if not user_input:
        break
    s.sendall(user_input.encode())
    data = s.recv(1024)
    if not data:
        break
    print("Данные полученные с сервера", data.decode('utf-8'))


# In[ ]:




