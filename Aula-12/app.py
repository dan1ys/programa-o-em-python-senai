# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA.
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO,
# ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES.

import statistics

def media(notas):
    return statistics.mean(notas)

def moda(notas):
    return statistics.mode(notas)

def desvio_padrao(notas):
    return statistics.stdev(notas)

def maior_nota(notas):
    return max(notas)

def menor_nota(notas):
    return min(notas)

notas = []

for i in range(5):
    nota = float(input(F'Digite a nota do aluno {i+1}: '))
    notas.append(nota)

print('\nResultado')
print('Média:', media(notas))
print('Moda:', moda(notas))
print('Desvio padrão:', desvio_padrao(notas))
print('Maior nota:', maior_nota(notas))
print('Menor nota:', menor_nota(notas))