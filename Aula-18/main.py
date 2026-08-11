import tkinter as tk



def display():
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    soma  =  n1  +  n2
    texto_.config(text = soma)




janela = tk.Tk()
janela.geometry('600x300')


# tk.Label(janela, text  =  'isso é um texto',font=('System', 30), fg= 'blue' ).pack()


sessao_1 =  tk.Frame(janela)
sessao_1.pack()



entrada1  =  tk.Entry(sessao_1, font=('System', 15), fg= 'red')
entrada1.pack(pady= 10)


entrada2  =  tk.Entry(sessao_1, font=('System', 15), fg= 'red')
entrada2.pack(pady= 10)


btn  =  tk.Button(sessao_1, text = '+', command=display, font=('System', 15), fg= 'blue')
btn.pack()


texto_  =  tk.Label(sessao_1, text  =  'Resultado = ',font=('System', 15), fg= 'blue' )
texto_.pack()




janela.mainloop()

