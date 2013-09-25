#!/usr/bin/python2

import socket
import select
import sys

def echoserver(port, size, connections):
    host = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, int(port)))
    s.listen(5)
    input = [s,sys.stdin]
    running = 1
    while running:
        inputready,outputready,exceptready = select.select(input,[],[])

        for i in inputready:

            if i == s:
                # handle server socket
                client, address = s.accept()
                input.append(client)

            elif i == sys.stdin:
                # handle standard input
                junk = sys.stdin.readline()
                running = 0

            else:
                # handle other sockets
                data = i.recv(int(size))
                if data:
                    i.send(data)
                    print "Received message: %s" % data
                else:
                    i.close()
                    input.remove(i)

if len(sys.argv) != 4:
    print "Usage: %s <port> <packet size> <max connections>" % sys.argv[0]
    quit()

echoserver(sys.argv[1], sys.argv[2], sys.argv[3])