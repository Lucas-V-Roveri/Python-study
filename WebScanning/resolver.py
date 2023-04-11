#!/usr/bin/python2

import socket,sys

print(".:DNS Resolver criado por:. \n.:Lucas Vilela Roveri:.\n")


ip = sys.argv[1]

print ip," <:::Tem como IP:::> ", socket.gethostbyname(ip)
