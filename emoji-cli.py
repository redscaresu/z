#!/usr/bin/env python

import argparse
import socket

# Create the parser
my_parser = argparse.ArgumentParser(prog='emoji-client',
                                    usage='%(prog)s [options] emoji',
                                    description='send beautiful emojis')

# Add the arguments
my_parser.add_argument('Emoji',
                       metavar='TYPE_OF_EMOJI',
                       type=str,
                       help='the emoji you want')
my_parser.add_argument('-n',
                       metavar='NUMBER_OF_EMOJIS',
                       type=str,
                       help='the number of emojis you need')
my_parser.add_argument('-s',
                       metavar='TYPE_OF_SEPARATOR',
                       type=str,
                       help='the type of separator you want')
my_parser.add_argument('-r',
                       action='store_true',
                       help='if specified do not translate emojis server side')

# Execute the parse_args() method
args = my_parser.parse_args()

emoji = args.Emoji

if args.n is not None:
    numEmojis = args.n
else:
    numEmojis = "1"

if args.s is not None:
    separator = args.s
else:
    separator = ""

translate = args.r

message=f"{numEmojis}:{emoji}:{translate}:{separator}"
# message = b'1:ok:sausage:'
message=message.encode()
# print(translate)
print(message)

#create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)

#create data for client socket
# message = b'3:thumbsup:-'
addr = ("127.0.0.1", 12000)

#send to client socket
client_socket.sendto(message, addr)