#!/usr/bin/python2

import socket
import sys

def echoclient(port):
    host = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    running = 1
    while running:
        text = raw_input("Enter message: ")
        s.send(text)
        data = s.recv(1024)
        if data:
            print '[Server echo] %s' % data
        else:
            print "Connection closed"
            quit()

if len(sys.argv) != 2:
    print "Usage: %s <port>" % sys.argv[0]
    quit()

echoclient(sys.argv[1])