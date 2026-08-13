import sqlite3


con = sqlite3.connect('cadastro.db')
cursor = con.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,            
        nome TEXT NOT NULL,
        email TEXT NOT NULL 
   )
''')


# crud




def criar_cliente(nome, email):
    cursor.execute('INSERT INTO clientes (nome, email) values(?,?)', (nome, email))
    con.commit()


def listar_clentes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()


def atualizar_mail(id_cliente, novo_email):
    cursor.execute('UPDATE clientes SET email=? WHERE id = ?', (novo_email, id_cliente))
    con.commit()


def deletar_cliente(id_cliente):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
    con.commit()




def sistema():


    while True: 


        op = input('O que deseja fazer 1 - add cliente | 2 -  atualizar | 3 - deletar  : ')


        if  op == '1':



            nome =  input('Nome: ')
            email = input('e - mail: ')
            criar_cliente(nome, email)
            criar_cliente('Lucas', 'Lucas@gmail.com')
            print('Inserindo ... ')
            print(listar_clentes())


        elif op == '2':
            print(listar_clentes()) 
            id  =  int(input('Id: '))
            n_email = input('e - mail: ')
            # atualizar
            print('Atualizando ...')
            atualizar_mail(id, n_email)
            print(listar_clentes())



        elif op == '3':   
        # delete
            
            print(listar_clentes())
            id  =  int(input('Id: '))
            print('deletando ... ')
            deletar_cliente(id)
            print(listar_clentes())


            con.close()


sistema()            