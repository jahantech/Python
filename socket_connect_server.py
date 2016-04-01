#!/usr/bin/python 

import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_addr_port_info = ('localhost',8080)

print "Listening at %s:%s" % server_addr_port_info



