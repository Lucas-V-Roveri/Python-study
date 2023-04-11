#!/usr/bin/python2
import sys
import os
import socket

print (".:BannerGrabbing Criado por:. \n.:<Lucas Vilela Roveri>:. ")
print ("Modo de uso: ./banner.py IP PORTA")

ip = sys.argv[1]
porta = sys.argv[2]
porta = int(porta)
varsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
varsocket.connect_ex((ip,porta))
gbanner = varsocket.recv(1024)
print(gbanner)

varsocket.send("USER AOTN\r\n")
gbanner = varsocket.recv(1024)
print(gbanner)

varsocket.send("PASS AOTN\r\n")
gbanner = varsocket.recv(1024)
print (gbanner)


