#! /usr/bin/python3
import glob
import os


def main_menu():
	resp = True
	while resp:
		print ("\nO que deseja fazer:\n1. Iniciar\n2. Carregar configuraçao\n3. Configurar\n4. Sair")
		resp = input ("\nInsira a opçao desejada: ")
		if resp == "1":
			resp = False
		elif resp == "2":
			print ('load()')
		elif resp == "3":
			config()
		elif resp == "4":
			print ("\nEncerrando o programa")
			quit()
		else:
			print ("Opçao invalida")



def config ():
	print ("::Configuraçoes::\n\n")
	local_salvamento = input("\nDigite o local em que deseja salvar os arquivos: ")
	local = input("\nDigite o local dos arquivos base desejados: ")
	r = input("\nDeseja utilizar todos os arquivos? Y/N: ")
	r.upper()
	if r == "Y":
		arquivos = glob.glob(local+'*xlsx')
	else:
		contador = 1
		nome_arquivos = []
		n_arquivos = input("\nDigite a quantidade desejada de arquivos: ")
		while contador <= int(n_arquivos):
			print("Arquivo numero", contador)
			nome = input ("Digite o nome do arquivo: ")
			nome_arquivos.append(nome)
			contador+=1
		contador = 0
		arquivos = []
		for itens in nome_arquivos:
			arquivos.append(local+'/'+nome_arquivos[contador]+'.xlsx')
			contador += 1
	r = input("\nDeseja utilizar todas as colunas? Y/N: ")
	r = r.upper()
	if r == "Y":
			colunas = "Y"
	else:
		contador = 0
		colunas = []
		while contador < int(n_arquivos):
			print ("\nArquivo: ", nome_arquivos[contador])
			nome = input("\nInsira a coluna desejada: ")
			colunas.append(nome)
			contador +=1
		print ("\nOs arquivos", nome_arquivos)
		print ("Utilizarao as respectivas colunas")
		print ("             ", colunas)
 	opcao = input("\nQual a operaçao deseja realizar com base nas celulas:\n1. Soma\n2. Subtraçao\n3. Agrupar \nSelecione uma opcao: ")
	if opcao == 1:
		operacao = "sum"
	elif opcao == 2:
		operacao = "diff"
	else:
		operacao = "N"
	modo = input("\nDeseja ativar o inicio rapido?\n(O programa sera iniciado diretamente, sem a apresentaçao do menu\nPara alterar esta opcao sera necessario acessar diretamente o arquivo de configuraçao)\nY/N: ")
	modo = modo.upper()
	if modo == "Y":
		print ("\nModo :Inicio Rapido: <ativado>")
	else:
		print ("\nModo :Inicio Rapido: >desativado<")

main_menu()






print ("Executando...")

