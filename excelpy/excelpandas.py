#! /usr/bin/python3
import pandas as pd
import glob
import os

print ("::::::::::::::::::BEM-VINDO:::::::::::::::::\n::::::::::::::::::::::::::::::::::::::::::::\n.:::::Iniciando Concatenador de Dados::::::.\n::::::::::::::::::::::::::::::::::::::::::::")

#Define os locais e coleta os arquivos desejados#

local = input ("\nDigite o local dos arquivos desejados: ")
if os.path.isdir(local) == False:
		print ("\nLocal do arquivos base nao foi encontrado\nPor favor, confira os inputs e tente novamente")
		input("\n\n.:Pressione ENTER para encerrar:.")
		quit()

local_salvamento = input ("\nDigite o local em que deseja salvar os arquivos:")

arquivos = glob.glob(local+'*xlsx')

print(arquivos)


#Cria Uma nova planilha vazia#

df1 = pd.DataFrame()

#Le todos os arquivos dentro da pasta e junta-os na planilha anterior#


column = ['Coluna 2', "COLUMN2", "Soma"]

contador = 0

for arquivos in arquivos:

	df2 = pd.read_excel(arquivos)[column[contador]]
	df1 = pd.concat([df1,df2],axis= 1,ignore_index=True)
	contador +=1

#Cria uma coluna com a operaçao por linha e concatena-a com as outras,#
#Retira colunas vazias caso existam"

df3 = pd.DataFrame(df1.sum(axis = 1))

df1 = pd.concat(([df1,df3]),axis=1,ignore_index = True)

df1 = df1.dropna(axis=1, how='all')

df1.columns = column



#Salva o novo arquivo na pasta designada#

try: 
	df1.to_excel(local_salvamento+"/resultado.xlsx", index = False)
	print ("\n.::Processo Concluido com Sucesso::.\n")
except:
	print ("\nUm erro foi encontrado no processo para salvar o arquivo\nPor favor, verifique os inputs e tente novamente\n")


