from cProfile import label
from tkinter import *
from tkinter import ttk

def center(win):
    win.update_idletasks()  # Update "requested size" from geometry manager
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

janela = Tk()      # cria objeto visual
janela.title("NOTA")
janela.geometry('450x200')
janela.configure(bg='#d3d3d3') # cor da janela
center(janela)

def openNewWindow(): 
      
    contrac = Tk() 
    contrac.title("CONTRA CHEQUE")
    contrac.geometry("1000x650") 
    contrac.configure(bg='#d3d3d3') # cor da janela 
    center(contrac)
    
    frame_topo = Frame(contrac, width=1000,height=70, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_topo.grid(row=0,column=0)

    a = Label(frame_topo,text="0040128 VINICIN NEGOCIOS ", bg='#d3d3d3',) #nome da empresa
    a.place(x=0,y=0) # exibe a frase
    b = Label(frame_topo,text="Rua xxxxxxxxxxxxxxxxxxxx,xxx ", bg='#d3d3d3') #endereco
    b.place(x=0,y=20) # exibe a frase
    c = Label(frame_topo,text="xx/xx/xxxx a xx/xx/xxxx ", bg='#d3d3d3') #data
    c.place(x=0,y=40) # exibe a frase
    d = Label(frame_topo,text="Demonstrativo de Pagamento de Salário ", bg='#d3d3d3') #demonstrativo pagamento etc etc etc
    d.place(x=750,y=0) # exibe a frase
    e = Label(frame_topo,text="102489237682017817517 ", bg='#d3d3d3') #esse numero n faço ideia
    e.place(x=830,y=40) # exibe a frase

    frame_nome = Frame(contrac, width=1000,height=30, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_nome.grid(row=1,column=0)

    numfun = Label(frame_nome,text="102930", bg='#d3d3d3') #num funcionario
    numfun.place(x=0,y=3) # exibe a frase
    nomec = Label(frame_nome,text="------------------------------------------", bg='#d3d3d3') #nome funcionario
    nomec.place(x=60,y=3) # exibe a frase
    
    f = Label(frame_nome,text="MESTRE DO AMOR", bg='#d3d3d3') #ocupação
    f.place(x=830,y=3) # exibe a frase

    vnome = (nome.get())
    nomec['text']=vnome


    frame_titulo = Frame(contrac, width=1000,height=25, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_titulo.grid(row=3,column=0)

    g = Label(frame_titulo,text="Cód.", width=10,height=0, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #codigo
    g.place(x=0,y=-2) # exibe a frase    
    h = Label(frame_titulo,text="Descrição",width=50,height=0, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #descrição
    h.place(x=80,y=-2) # exibe a frase   
    i = Label(frame_titulo,text="Referencia",width=20,height=0, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Referencia
    i.place(x=440,y=-2) # exibe a frase
    j = Label(frame_titulo,text="Vencimentos",width=30,height=0, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Vencimentos
    j.place(x=590,y=-2) # exibe a frase
    k = Label(frame_titulo,text="Descontos",width=25,height=0, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Descontos
    k.place(x=810,y=-2) # exibe a frase  

    frame_meio = Frame(contrac, width=1000,height=295, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_meio.grid(row=4,column=0)

    l = Label(frame_meio,width=10,height=19, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Criando bordas cod.
    l.place(x=0,y=-2) # exibe a frase
    m = Label(frame_meio,width=50,height=19, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Criando bordas descricao
    m.place(x=80,y=-2) # exibe a frase
    n = Label(frame_meio,width=20,height=19, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Criando bordas referencia
    n.place(x=440,y=-2) # exibe a frase 
    o = Label(frame_meio,width=30,height=19, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Criando bordas vencimento
    o.place(x=590,y=-2) # exibe a frase
    p = Label(frame_meio,width=25,height=19, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #Criando bordas descontos
    p.place(x=810,y=-2) # exibe a frase

    frame_mbaixo = Frame(contrac, width=1000,height=84, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_mbaixo.grid(row=5,column=0)

    q = Label(frame_mbaixo, text='Benefício de xx/xx/xxxx até xx/xx/xxxx',width=30,height=0, bg='#d3d3d3') 
    q.place(x=0,y=0) # exibe a frase
    r = Label(frame_mbaixo, width=30,height=2, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #bordas lado direito frame mbaixo
    r.place(x=590,y=0) # exibe a frase
    s = Label(frame_mbaixo, text='Valor Líquido', width=30,height=2, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #bordas lado direito frame mbaixo
    s.place(x=590,y=40) # exibe a frase
    t = Label(frame_mbaixo, width=25,height=2, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #bordas lado direito frame mbaixo
    t.place(x=810,y=0) # exibe a frase
    u = Label(frame_mbaixo, width=25,height=2, bg='#d3d3d3', highlightthickness=2, highlightbackground="black") #bordas lado direito frame mbaixo
    u.place(x=810,y=40) # exibe a frase

    frame_baixo = Frame(contrac, width=1000,height=65, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_baixo.grid(row=6,column=0)

    v = Label(frame_baixo, text='Saldo Base', width=10, bg='#d3d3d3')
    v.place(x=40,y=0) # exibe a frase
    saldobase = Label(frame_baixo, text='', width=10, bg='#d3d3d3')
    saldobase.place(x=40,y=20) # exibe a frase

    w = Label(frame_baixo, text='Sal, Contri. INSS',width=15, bg='#d3d3d3')
    w.place(x=150,y=0) # exibe a frase
    SalContriINSS = Label(frame_baixo, text='', width=15, bg='#d3d3d3')
    SalContriINSS.place(x=150,y=20) # exibe a frase    

    x = Label(frame_baixo, text='Base Cál. FGTS',width=15, bg='#d3d3d3')
    x.place(x=350,y=0) # exibe a frase
    basecalcfgts = Label(frame_baixo, text='', width=15, bg='#d3d3d3')
    basecalcfgts.place(x=350,y=20) # exibe a frase   

    y = Label(frame_baixo, text='F.G.T.S do Mês',width=15, bg='#d3d3d3')
    y.place(x=570,y=0) # exibe a frase
    FGTSMES = Label(frame_baixo, text='', width=15, bg='#d3d3d3')
    FGTSMES.place(x=570,y=20) # exibe a frase  

    z = Label(frame_baixo, text='Base Cálc. IRRF',width=15, bg='#d3d3d3')
    z.place(x=760,y=0) # exibe a frase
    BaseCalcIRRF = Label(frame_baixo, text='', width=15, bg='#d3d3d3')
    BaseCalcIRRF.place(x=760,y=20) # exibe a frase  
    
    aa = Label(frame_baixo, text='Faixa IRRF',width=10, bg='#d3d3d3')
    aa.place(x=920,y=0) # exibe a frase

    frame_ass = Frame(contrac, width=1000,height=81, highlightthickness=2, highlightbackground="black", bg='#d3d3d3')
    frame_ass.grid(row=7,column=0) 
        
# Frame pow
frame_cima = Frame(janela, width=500,height=50, bg='#008080')
frame_cima.grid(row=0,column=0)
#mesma coisa ai de cima oh muda a cor pra ver
frame_baixo = Frame(janela, width=500,height=250, bg='#d3d3d3')
frame_baixo.grid(row=1,column=0)

app_name = Label(frame_cima,text="CONTRA CHEQUE", width=40, height=2, bg='#008080', fg='black', font='times')
app_name.place(x=0,y=0)


f_nome = Label(frame_baixo,text="NOME:", width=15)
f_nome.place(x=0,y=0)
nome = Entry(frame_baixo, width=20) # como se fosse input, recebe o valor da variavel
nome.place(x=100,y=0) # informa local da frase

f_faltas = Label(frame_baixo,text="Salario Bruto: ", width=15) # exibe a frase
f_faltas.place(x=0,y=20) 
faltas = Entry(frame_baixo, width=20)
faltas.place(x=100,y=20)

f_faltas = Label(frame_baixo,text="Horas Extras: ", width=15) # exibe a frase
f_faltas.place(x=0,y=40) 
faltas = Entry(frame_baixo, width=20)
faltas.place(x=100,y=40)

f_faltas = Label(frame_baixo,text="Digite as faltas: ", width=14) # exibe a frase
f_faltas.place(x=0,y=60) 
faltas = Entry(frame_baixo, width=20)
faltas.place(x=100,y=60)

f_faltas = Label(frame_baixo,text="Porcentagem de adiantamento: ") # exibe a frase
f_faltas.place(x=0,y=80) 
faltas = Entry(frame_baixo, width=7)
faltas.place(x=177,y=80)

labelTop = Label(frame_baixo,text = "Paga Pensão?")
labelTop.place(x=0,y=100)

comboExample = ttk.Combobox(frame_baixo,state="readonly", width=5, 
                            values=[
                                    "SIM", 
                                    "NÃO"])
print(dict(comboExample)) 
comboExample.place(x=79,y=100)
comboExample.current(1)

print(comboExample.current(), comboExample.get())
# FAZER COMBO PAGA PENSAO?

#button
bcalcular = Button(frame_baixo, height=5,  text="EXIBIR CONTRA CHEQUE", command=openNewWindow ) # command=calcula)
# posição do button
bcalcular.place(x=250,y=15)

# fixa a janela
janela.mainloop()