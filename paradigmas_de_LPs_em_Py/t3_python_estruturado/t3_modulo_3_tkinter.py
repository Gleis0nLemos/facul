from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Zói")
texto.pack()

pic = PhotoImage(file="paradigmas_de_LPs_em_Py/t3_python_estruturado/images/eren.gif")
logo = Label(master=janelaPrincipal, image=pic)
logo.pack()

botao = Button(master=janelaPrincipal, text='Clique', command=funcClicar)
botao.pack()

janelaPrincipal.mainloop()