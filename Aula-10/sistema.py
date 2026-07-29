# Crie um sistema de notas de alunos

print('Sistema de notas de alunos. ')
chances = 3
while chances > 0 :
    acesso =  12345
    senha =  int(input('Digite a senha: '))
    chances -= 1
    if senha == acesso:
        print('Insira as notas: ')
        n1 = float(input('Digite a primeira nota: '))
        n2 = float(input('Digite a segunda nota: '))
        n3 = float(input('Digite a terceira nota: '))
        print('Notas cadastradas com sucesso! ')
        break
    else:
        print('Senha incorreta, digite novamente. ')
        print('Quantidade de chances', chances)
    if chances == 0: print('Senha incorreta: conta bloqueada. ')
input('Digite enter para sair')