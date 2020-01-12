#!/usr/bin/env python

#TODO, this needs to be broken up into separate functions

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

dict_emoji = { 'ok'         : '\U0001F44C',
               'thumbsup'   : '\U0001f44d',
               'thumbsdown' : '\U0001F44E',
               'crossed'    : '\U0001F44D', 
            }

while True:
    message, address = server_socket.recvfrom(1024)
    
    msg = message.decode('unicode-escape')
    msg = msg.split(':')

    #input validation server side, first element of list must be int
    repeat = (msg[0])
    try:
        repeat = int(repeat)
    except ValueError:
        msg = ':'.join(msg)
        print(f"`Unknown command: {msg}` NUM_OF_EMOJIS must be int")
        continue
        

    #input validation server side, emoji must exist in emoji_dict
    emoji = msg[1]
    if emoji not in dict_emoji:
        msg = ':'.join(msg)
        print(f"`Unknown command: {msg}` TYPE_OF_EMOJI does not exist")
        continue

    #handle translate flag, this is messy I should cast this back to a bool from a string
    translate = msg[2]
    if not (translate != "True") or (translate != "False"):
        msg = ':'.join(msg)
        print(f"`Unknown command: {msg}` TRANSLATE_FLAG does not exist, must be True or False")
        continue

    if translate == "True":
        for k, v in dict_emoji.items():
            if k == emoji:
                emoji = k
                emoji=f":{k}:"
    else:
        #translate incomming emoji against dictionary
        for k, v in dict_emoji.items():
            if k == emoji:
                emoji = v
    
    #TODO assumption correct number of arguments, should be validated server and client side
    if len(msg) > 3:
        separator = msg[3]
    else:
        separator = ''
    
    emojiList = []

    for i in range(repeat):
        emojiList.append(emoji)
    
    print(*emojiList, sep=separator)
