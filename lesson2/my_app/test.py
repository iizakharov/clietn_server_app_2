import sys
import json
from socket import *
import time
from settings.utils import *
from settings.dict import *

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
server_address = DEFAULT_IP_ADDRESS
server_port = DEFAULT_PORT
s.connect((server_address, server_port))   # Соединиться с сервером
msg = 'Привет, сервер'
s.send(msg.encode('utf-8'))
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
s.close()


print(server_address)
print(server_port)