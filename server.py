#!/usr/bin/env python

import random
import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(1024)
    msg = message.decode('unicode-escape')
    msg = msg.split(' ')
    repeat = int(msg[0])
    emoji = msg[1]
    emojiList = []

    for i in range(repeat):
        emojiList.append(emoji)
    
    print(*emojiList, sep="")
