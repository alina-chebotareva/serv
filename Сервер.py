#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import time
with socket.socket() as s:
    host = 'localhost'
    port = 8001
    s.bind((host, port))
    print(f'сервер привязан к {port}')
    s.listen()
    print('Начало прослушивания')
    con, addr = s.accept()
    with con:   
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)


# In[ ]:




