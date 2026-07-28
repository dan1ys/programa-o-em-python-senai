# Verificando se uma string é vazia ou não

nome = input("Digite seu nome: ")
match nome:
    case "":
     print("Voce não digitou nada. ")

    case _:
     print("Nome cadastrado!")

#  Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)  


idade =  int(input('Idade: '))


match idade:


    case idade if idade <= 12:
        print('Criança')
    case idade if idade >= 13 and idade <=17:
        print('Adolescente')
    case idade if idade >= 18  and idade <= 35:
        print('Jovem')
    case idade if idade > 35 and idade <= 65:
        print('Adulto')
    case _:
        print('Idoso')       