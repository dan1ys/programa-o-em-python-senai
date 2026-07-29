# Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nomes = []
contador = 0
while contador < 10:
    nome = ("Digite um nome: ")
    nomes.append(nome)
    contador = contador + 1

print(nomes)