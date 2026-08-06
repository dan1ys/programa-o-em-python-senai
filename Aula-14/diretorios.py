# Exercício 1: Criar e ler um Arquivo

arquivo = open('texto.txt', 'w')
arquivo.write('Olá mundo!')
arquivo.close()

arquivo = open('texto.txt', 'r')
print(arquivo.read())
arquivo.close()



# Exemplo 2: Cria um Diretório

import os

os.mkdir('NovaPasta')
print('Diretório criado.')



# Exercício 3: Renomear um Diretório

import os
os.rename('NovaPasta', 'PastaRenomeada')
print('Diretório renomeado.')



# Exercício 4:  Listar Arquivos em um Diretório

import os
arquivos = os.listdir('.')

for arquivo in arquivos:
    print(arquivo)



# Exercício 5:  Copiar Arquivos em um Diretório

import shutil

shutil.copy('texto.txt', 'copia_texto.txt')
print('Arquivo copiado.')



# Exercício 6:  Remover

import os
os.remove('copia_texto.txt')
print('Arquivo removido.')