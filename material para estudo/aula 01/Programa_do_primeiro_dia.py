from tkinter import *


janela = Tk()

def btn_click():
    lb['text'] = """A linguagem foi criada pelo Holandês 
    Guido van Rossum em 1991
    teve a sua inspiração em um programa de televisão britanico 
    Monty Python’s Flying Circus"""
def btn_click1():
    lb['text'] = """Python é uma linguagem de programação de alto nível
interpretada,orientada a objetos e funcional
com principal foco em produtividade e legibilidade"""

def btn_click2():
    lb['text'] = """A syntaxe da linguagem Python é muito simples 
em relação as outras linguagens,alem de ser 
multiplataforma,ou seja,é executavel em diferentes 
tipos de sistemas operacionais"""

def btn_click3():
    lb['text'] = """Python é uma linguagem que vem ganhando muito espaço
nos ambientes corporativos, muito usada em inteligencia artificial, 
um ramo que vem crescendo bastante nos ultimos anos, e pelo simples fato 
de ser MUITOOOOO DIVERTIDO programar em python
    """
def btn_click4():
    lb['text'] = """Por anos Guidor evitou vincular a linguagem 
ao réptil (a cobra píton),porem editora O’Reilly — que possui
a tradição de utilizar animais nas capas 
de seus livros sugeriu colocar uma cobra píton na capa 
do seu primeiro livro "Programming Python" """

def sair():
    janela.destroy()

botao = Button(janela,width=30, height=-40,bg='Red', text='Quem criou a Linguagem Python?', font=('arial', 20, 'bold'), command=btn_click)
botao.place(x=10, y=70)

botao1 = Button(janela, width=30, height= -40,bg='Blue', text='O que é a linguagem Python?', font=('arial',20,'bold'),command= btn_click1)
botao1.place(x=570, y= 70)

botao2 = Button(janela, width=30, height= -40, bg='Green',text='Diferencial da linguagem Python', font=('arial',20,'bold'),command= btn_click2)
botao2.place(x=570, y= 140)

botao3 = Button(janela, width=30, height= -40,bg='Yellow', text='Porque aprender Python? ', font=('arial',20,'bold'),command=btn_click3)
botao3.place(x=10, y= 140)

botao4 = Button(janela, width=50, height= -40, bg='Gray',text='Por que o logo é representado por duas cobras? ', font=('arial',20,'bold'), command=btn_click4)
botao4.place(x=100, y= 230)

botao_sair = Button(janela, width= 30, height=-10, text='Sair', font=('arial', 10 , 'bold'), command=sair)
botao_sair.place(x=400, y =570)

lb = Label(janela, width=50, height=-10, font=('arial',20,'bold'))
lb.place(x=90,y=400)

lb2 = Label(janela, width= 50, height=-30, text='Python The Best Language',font=('arial',20,'bold'))
lb2.place(x=140,y=10)

janela.title('Teste01')
janela.geometry('1100x600+100+80')
janela.mainloop()