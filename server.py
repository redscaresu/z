#!/usr/bin/env python

import random
import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(1024)
    msg = message.decode()
    msg = msg.split(' ')
    print(msg[1])
    server_socket.sendto(message, address)