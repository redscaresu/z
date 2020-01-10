#!/usr/bin/env python

#TODO, this needs to be broken up into separate functions

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

while True:
    message, address = server_socket.recvfrom(1024)
    
    msg = message.decode('unicode-escape')
    msg = msg.split(' ')

    #TODO input validation server side, repeat must be int, emoji must conform unicode table   
    repeat = int(msg[0])
    emoji = msg[1]
    
    #TODO assumption is that user has provided the correct number of arguments
    if len(msg) > 2:
        separator = msg[2]
    else:
        separator = ''
    
    emojiList = []

    for i in range(repeat):
        emojiList.append(emoji)
    
    print(*emojiList, sep=separator)
