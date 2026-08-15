import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# ============================================================
# BANCO DE DADOS
# ============================================================

def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            imc REAL NOT NULL,
            classificacao TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# ============================================================
# FUNÇÃO PARA CALCULAR O IMC
# ============================================================

def calcular_imc(peso, altura):
    return peso / (altura * altura)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"


# ============================================================
# LIMPAR CAMPOS
# ============================================================

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

    tree.selection_remove(tree.selection())

    entry_nome.focus()


# ============================================================
# CREATE - INSERIR PACIENTE
# ============================================================

def inserir_paciente():

    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    peso = entry_peso.get().strip().replace(',', '.')
    altura = entry_altura.get().strip().replace(',', '.')

    # Validação dos campos
    if not nome or not idade or not peso or not altura:
        messagebox.showwarning(
            'Atenção',
            'Preencha todos os campos!'
        )
        return

    try:
        idade = int(idade)
        peso = float(peso)
        altura = float(altura)

        if idade <= 0:
            messagebox.showwarning(
                'Atenção',
                'A idade deve ser maior que zero!'
            )
            return

        if peso <= 0:
            messagebox.showwarning(
                'Atenção',
                'O peso deve ser maior que zero!'
            )
            return

        if altura <= 0:
            messagebox.showwarning(
                'Atenção',
                'A altura deve ser maior que zero!'
            )
            return

    except ValueError:
        messagebox.showerror(
            'Erro',
            'Digite valores válidos para idade, peso e altura!'
        )
        return

    # Calcula o IMC
    imc = calcular_imc(peso, altura)

    # Classifica o IMC
    classificacao = classificar_imc(imc)

    # Insere no banco
    conn = conectar()
    c = conn.cursor()

    c.execute('''
        INSERT INTO pacientes
        (nome, idade, peso, altura, imc, classificacao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        nome,
        idade,
        peso,
        altura,
        imc,
        classificacao
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        'Sucesso',
        f'Paciente cadastrado com sucesso!\n\n'
        f'IMC: {imc:.2f}\n'
        f'Classificação: {classificacao}'
    )

    limpar_campos()
    mostrar_pacientes()


# ============================================================
# READ - MOSTRAR PACIENTES
# ============================================================

def mostrar_pacientes():

    # Limpa a tabela
    for row in tree.get_children():
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()

    c.execute('''
        SELECT id, nome, idade, peso, altura, imc, classificacao
        FROM pacientes
        ORDER BY id
    ''')

    pacientes = c.fetchall()

    for paciente in pacientes:
        tree.insert(
            "",
            "end",
            values=(
                paciente[0],
                paciente[1],
                paciente[2],
                f"{paciente[3]:.2f}",
                f"{paciente[4]:.2f}",
                f"{paciente[5]:.2f}",
                paciente[6]
            )
        )

    conn.close()


# ============================================================
# DELETE - EXCLUIR PACIENTE
# ============================================================

def delete_paciente():

    selecao = tree.selection()

    if not selecao:
        messagebox.showwarning(
            'Atenção',
            'Selecione um paciente para excluir!'
        )
        return

    paciente = tree.item(selecao)
    paciente_id = paciente['values'][0]
    nome = paciente['values'][1]

    resposta = messagebox.askyesno(
        'Confirmar exclusão',
        f'Deseja realmente excluir o paciente:\n\n{nome}?'
    )

    if resposta:

        conn = conectar()
        c = conn.cursor()

        c.execute(
            'DELETE FROM pacientes WHERE id = ?',
            (paciente_id,)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            'Sucesso',
            'Paciente excluído com sucesso!'
        )

        limpar_campos()
        mostrar_pacientes()


# ============================================================
# UPDATE - EDITAR PACIENTE
# ============================================================

def editar():

    selecao = tree.selection()

    if not selecao:
        messagebox.showwarning(
            'Atenção',
            'Selecione um paciente para atualizar!'
        )
        return

    paciente = tree.item(selecao)
    paciente_id = paciente['values'][0]

    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    peso = entry_peso.get().strip().replace(',', '.')
    altura = entry_altura.get().strip().replace(',', '.')

    if not nome or not idade or not peso or not altura:
        messagebox.showwarning(
            'Atenção',
            'Preencha todos os campos!'
        )
        return

    try:
        idade = int(idade)
        peso = float(peso)
        altura = float(altura)

        if idade <= 0 or peso <= 0 or altura <= 0:
            messagebox.showwarning(
                'Atenção',
                'Idade, peso e altura devem ser maiores que zero!'
            )
            return

    except ValueError:
        messagebox.showerror(
            'Erro',
            'Digite valores válidos para idade, peso e altura!'
        )
        return

    # Recalcula o IMC após a alteração
    imc = calcular_imc(peso, altura)

    classificacao = classificar_imc(imc)

    conn = conectar()
    c = conn.cursor()

    c.execute('''
        UPDATE pacientes
        SET nome = ?,
            idade = ?,
            peso = ?,
            altura = ?,
            imc = ?,
            classificacao = ?
        WHERE id = ?
    ''', (
        nome,
        idade,
        peso,
        altura,
        imc,
        classificacao,
        paciente_id
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        'Sucesso',
        f'Dados atualizados com sucesso!\n\n'
        f'Novo IMC: {imc:.2f}\n'
        f'Classificação: {classificacao}'
    )

    limpar_campos()
    mostrar_pacientes()


# ============================================================
# CARREGAR DADOS AO SELECIONAR UM PACIENTE
# ============================================================

def selecionar_paciente(event):

    selecao = tree.selection()

    if not selecao:
        return

    paciente = tree.item(selecao)
    dados = paciente['values']

    limpar_sem_selecao()

    entry_nome.insert(0, dados[1])
    entry_idade.insert(0, dados[2])
    entry_peso.insert(0, dados[3])
    entry_altura.insert(0, dados[4])


def limpar_sem_selecao():

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)


# ============================================================
# INTERFACE GRÁFICA
# ============================================================

janela = tk.Tk()

janela.title('Saúde & Bem-Estar - Cadastro de Pacientes')
janela.geometry('1000x600')
janela.resizable(False, False)


# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    janela,
    text='SAÚDE & BEM-ESTAR',
    font=('Arial', 20, 'bold')
)

titulo.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=(20, 5)
)


subtitulo = tk.Label(
    janela,
    text='Sistema de Cadastro e Cálculo de IMC',
    font=('Arial', 11)
)

subtitulo.grid(
    row=1,
    column=0,
    columnspan=4,
    pady=(0, 20)
)


# ============================================================
# CAMPOS
# ============================================================

label_nome = tk.Label(
    janela,
    text='Nome:',
    font=('Arial', 10, 'bold')
)

label_nome.grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky='e'
)


entry_nome = tk.Entry(
    janela,
    width=35
)

entry_nome.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


label_idade = tk.Label(
    janela,
    text='Idade:',
    font=('Arial', 10, 'bold')
)

label_idade.grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky='e'
)


entry_idade = tk.Entry(
    janela,
    width=35
)

entry_idade.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)


label_peso = tk.Label(
    janela,
    text='Peso (kg):',
    font=('Arial', 10, 'bold')
)

label_peso.grid(
    row=4,
    column=0,
    padx=10,
    pady=8,
    sticky='e'
)


entry_peso = tk.Entry(
    janela,
    width=35
)

entry_peso.grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)


label_altura = tk.Label(
    janela,
    text='Altura (m):',
    font=('Arial', 10, 'bold')
)

label_altura.grid(
    row=5,
    column=0,
    padx=10,
    pady=8,
    sticky='e'
)


entry_altura = tk.Entry(
    janela,
    width=35
)

entry_altura.grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)


# ============================================================
# BOTÕES
# ============================================================

btn_salvar = tk.Button(
    janela,
    text='Cadastrar',
    width=15,
    command=inserir_paciente
)

btn_salvar.grid(
    row=6,
    column=0,
    padx=5,
    pady=15
)


btn_atualizar = tk.Button(
    janela,
    text='Atualizar',
    width=15,
    command=editar
)

btn_atualizar.grid(
    row=6,
    column=1,
    padx=5,
    pady=15
)


btn_deletar = tk.Button(
    janela,
    text='Excluir',
    width=15,
    command=delete_paciente
)

btn_deletar.grid(
    row=6,
    column=2,
    padx=5,
    pady=15
)


btn_limpar = tk.Button(
    janela,
    text='Limpar',
    width=15,
    command=limpar_campos
)

btn_limpar.grid(
    row=6,
    column=3,
    padx=5,
    pady=15
)


# ============================================================
# TABELA
# ============================================================

columns = (
    'ID',
    'NOME',
    'IDADE',
    'PESO',
    'ALTURA',
    'IMC',
    'CLASSIFICAÇÃO'
)

tree = ttk.Treeview(
    janela,
    columns=columns,
    show='headings',
    height=12
)

tree.grid(
    row=7,
    column=0,
    columnspan=4,
    padx=20,
    pady=10
)


# Configuração dos cabeçalhos
for col in columns:
    tree.heading(
        col,
        text=col
    )


# Tamanho das colunas
tree.column('ID', width=50, anchor='center')
tree.column('NOME', width=200)
tree.column('IDADE', width=70, anchor='center')
tree.column('PESO', width=80, anchor='center')
tree.column('ALTURA', width=80, anchor='center')
tree.column('IMC', width=80, anchor='center')
tree.column('CLASSIFICAÇÃO', width=180, anchor='center')


# Evento para selecionar paciente
tree.bind(
    '<ButtonRelease-1>',
    selecionar_paciente
)


# ============================================================
# INICIALIZAÇÃO
# ============================================================

criar_tabela()
mostrar_pacientes()

entry_nome.focus()

janela.mainloop()