# 1- peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
     numero =  int(input('Insira um número: '))
except TypeError:
     print('Você inseriu um tipo de dado incorreto')
except ValueError:
     print('Você inseriu um tipo de dado incorreto')
else:
   print(numero)



# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

import random
chances = 3
while  chances > 0:
 chances = chances - 1
n  =   int(input('Digite um numero> '))
r = random.randint(1,2)
if n  == r : 
 print(f'Vc ganhou o jogo, o número é: {r}')
 break
else: 
 print(f'Vc perdeu o jogo, o número é {r}')     

try: