#!/usr/bin/env python

#TODO, this needs to be broken up into separate functions

#TO DO implement dictionary that does lookups against emojis

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

# dict_emoji = { 'ok' : b\U0001F44C',
#                'thumbsup'   : b\U0001f44d',
#             }

while True:
    message, address = server_socket.recvfrom(1024)
    
    msg = message.decode('unicode-escape')
    msg = msg.split(' ')

    #TODO input validation server side, repeat must be int, else catch and exit   
    repeat = int(msg[0])

    #TODO input validation server side, emoji must exist in emoji dict else catch and exit
    emoji = msg[1]
    
    #TODO assumption correct number of arguments, should be validated server and client side
    if len(msg) > 2:
        separator = msg[2]
    else:
        separator = ''
    
    emojiList = []

    for i in range(repeat):
        emojiList.append(emoji)
    
    print(*emojiList, sep=separator)
