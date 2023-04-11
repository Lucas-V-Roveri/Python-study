#!/usr/bin/python3
import socket,sys

print(".:DNS Bruteforce criado por:. \n.:Lucas Vilela Roveri:.\n")


#--Abrindo-Arquivo.txt-no-modo-leitura-&-fazendo-uma-lista-#

brute = open("brutedns.txt", "r")

dados = brute.read()

brute_lista = dados.split("\n")

#----#

ip = sys.argv[1]

contador = 0


for lines in brute_lista:
	try:	
		#-Concatena-host-&-subdominio-#
		subdominio = brute_lista[contador]
	
		contador = contador + 1

		host = subdominio + "." + ip

		#-Tenta-conexão-por-socket-no-host-#

		print (host," <:::Tem como IP:::> ", socket.gethostbyname(host),"\n")
	except:
		pass
