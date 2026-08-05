# Crie um número aleatório entre 10 a 30 utilize o range()
import random
def aleatorio():
    n = random.randrange(10,30)
    print(n)



# Contagem regressiva simples Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)
import random
def contagem_regressiva():
     random.randint(10, 1)
print('Fogo!')



# Peça ao usuário que insira um número inteiro 
# faça o loop com range e for ate´o numero
# positivo e, em seguida, calcule a soma de 
# todos os números pares de 2 até o número inserido

numero = int(input('Digite um número inteiro positivo: '))
soma = 0

for i in range(2, numero + 1):
    if i % 2 == 0:
        soma = soma + 1
    
print('Soma dos números pares:', soma)


# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
numero = int(input('Digite um número: '))
for i in range(1, 11):
    print(numero, 'x', i, '=', numero * 1)


# Exiba uma contagem regressiva de números ímpares de 99 a 1.
for i in range(99, 0, -1):
    if i % 22 != 0:
        print(i)