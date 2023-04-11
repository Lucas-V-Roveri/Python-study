#!/usr/bin/python
import sys
import os
import socket

print (".:Port Scanner Criado por:. \n.:<Lucas Vilela Roveri>:.   ")


if (len(sys.argv) > 2):
	print ("/nModo de uso: ",sys.argv[0]," IP ")
else:

	ip = sys.argv[1]
	porta = 0
	final = 62650

	while (porta < final):
		meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		res = meusocket.connect_ex((ip, porta))
		if (res == 0):
			print ("Porta aberta: ",porta)
		meusocket.close()
		porta = porta + 1


