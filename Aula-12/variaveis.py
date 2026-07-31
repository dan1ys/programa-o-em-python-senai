# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
def comparar (n1, n2):
    if n1 % 2 == 0:
        print(n1, 'é par')
    else:
     print(n2, 'é ímpar')
comparar(10, 7)


# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar(n1, n2, n3):
   resultado = n1 * n2 * n3
   print(resultado)
multiplicar(2, 3, 4)


# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def potencia(numero):
   print(numero ** 2)
potencia(5)


# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.
def verificar_idade(idade):
   if idade == 18:
      print('Bem vindo! Vc já é de maior! :)')
   else:
      print('Idade diferente de 18 anos.')
idade = int(input('Digite sua idade: '))
verificar_idade(idade)


# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def descobrir_idade(ano):
   idade = 2026 - ano
   print('Sua idade é:', idade)
ano = int(input('Digite seu ano de nascimento: '))
descobrir_idade(ano)


# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def copa(ano):
   if ano == 1999:
    print('O Brasil não ganhou a copa do mundo em 1999.')
   else:
      print('Ano diferente.')
ano = int(input('Digite um ano: '))
copa(ano)


# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
def cumprimentar():
   print('Bem vindo ao nosso restaurante!')

def restaurante():
   cardapio = ['Salada', 'Macarronada', 'Sanduíche', 'Sorvete']

   print('Cardápio:')
   for item in cardapio:
      print(item)
   pedido = input('Escolha um prato: ')
   print('Você escolheu', pedido)

cumprimentar()
restaurante()