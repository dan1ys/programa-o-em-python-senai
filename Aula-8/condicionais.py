# 2
idade = print(int(input("Digite sua idade: ")))
if idade >= 16:
 print("Pode votar.")
else:
 print("Não pode votar.")

# 3
numero = 8
if numero % 2 == 0:
 print("O número é par.")
else:
 print("O número é ímpar.")

# 4
l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))
if l1 == l2 and l2 == l3:
 print("Triângulo equilátero")
elif l1 == l2 or l1 == l3 or l2 == l3:
 print("Triângulo isósceles")
else:
 print("Triângulo escaleno")

# 5
numero = int(input("Digite um número"))
if numero % 5 == 0 and numero % 7 == 0:
 print("O número é múltiplo de 5 e 7.")
else:
 print("O número não é múltiplo de 5 e 7.")

# 6
numero = print(int(input("Digite um número: ")))
if numero > 10:
 print("Seu número é positivo e maior que 10.")
else:
 print("Seu número não é positivo e maior que 10. ")

# 7
numero = int(input("Digite um número: "))
if numero % 3 == 0 or numero % 5 == 0:
 print("O número é divisível por 3 ou por 5.")
else:
 print("O número não é divisível por 3 nem por 5.")