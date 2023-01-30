import random
import pyperclip
from tkinter import *


#Gerador de CNPJ
def cnpj(self, pontuacao):
    n = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    v = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
    # calcula dígito 1 e acrescenta ao total
    s = sum(x * y for x, y in zip(reversed(n), v))
    d1 = 11 - s % 11
    if d1 >= 10:
        d1 = 0
    n.append(d1)
    # idem para o dígito 2
    s = sum(x * y for x, y in zip(reversed(n), v))
    d2 = 11 - s % 11
    if d2 >= 10:
        d2 = 0
    n.append(d2)
    if pontuacao == 1:
        cnpj = "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(n)
        return cnpj
    else:
        cnpj = "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)
        return cnpj

#Função de ação de click no botão Gerar Cnpj
def btn3Click():
    entrada = Entry(janela)
    entrada.insert(0, cnpj(self=0, pontuacao=pontuacaoCnpj.get()))
    entrada.place(x=100, y=80)
    texto = str(entrada.get())
    pyperclip.copy(texto)
    lbl_copiado = Label(janela, text="Copiado!")
    lbl_copiado.place(x=220, y=80)
    lbl_copiado.after(400,lbl_copiado.destroy)


#Gerador de CPF
def cpf(self, pontuacao):
    def calcula_digito(digs):
        s = 0
        qtd = len(digs)
        for i in range(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10: return 0
        return res

    n = [random.randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))
    if pontuacao == 1:
        cpf = "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(n)
        return cpf
    else:
        cpf = "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)
        return cpf

#Função de ação de click no botão Gerar CPF
def btn4lick():
    entrada1 = Entry(janela)
    entrada1.insert(0, cpf(self=0, pontuacao=pontuacaoCpf.get()))
    entrada1.place(x=100, y=130)
    texto = str(entrada1.get())
    pyperclip.copy(texto)
    lbl_copiado = Label(janela, text="Copiado!")
    lbl_copiado.place(x=220, y=130)
    lbl_copiado.after(400, lbl_copiado.destroy)

def generate_pis(self, pontuacao):
    # Gerando os 9 primeiros dígitos aleatoriamente
    pis = str(random.randint(1000000000, 9999999999))

    # Calculando o dígito verificador
    total = 0
    weight = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(10):
        total += int(pis[i]) * weight[i]
    rest = 11 - (total % 11)
    if rest == 10 or rest == 11:
        rest = 0
    pis += str(rest)
    #return pis
    if pontuacao == 1:
        p = "%s%s%s.%s%s%s%s%s.%s%s-%s" % tuple(pis)
        return p
    else:
        p = "%s%s%s%s%s%s%s%s%s%s%s" % tuple(pis)
        return p


def btn8Click():
    entrada = Entry(janela)
    entrada.insert(0, generate_pis(self=0, pontuacao=pontuacaoPis.get()))
    entrada.place(x=100, y=180)
    texto = str(entrada.get())
    pyperclip.copy(texto)
    lbl_copiado = Label(janela, text="Copiado!")
    lbl_copiado.place(x=220, y=180)
    lbl_copiado.after(400,lbl_copiado.destroy)




janela = Tk()
janela.title('Automação de Rotina')
janela.geometry('380x250')
texto1 = Label(text='Selecione a opção:', fg='red', font=('bold'))
texto1.place(x=110, y=30)

#Variaveis Globais
pontuacaoCnpj = IntVar()
pontuacaoCpf = IntVar()
pontuacaoPis = IntVar()

#Entradas padrão em branco para layout da janela
entrada = Entry(janela)
entrada.place(x=100, y=80)

entrada1 = Entry(janela)
entrada1.place(x=100, y=130)


entrada2 = Entry(janela)
entrada2.place(x=100, y=180)

#ChecBox para selecionar opção de geração do CNPJ com ou sem pontuação
cb_pontuacaoCnpj = Checkbutton(janela, text = "pontuação", variable=pontuacaoCnpj, onvalue=1, offvalue=0)
cb_pontuacaoCnpj.place(x=100, y=100)

#ChecBox para selecionar opção de geração do CPF com ou sem pontuação
cb_pontuacaoCpf = Checkbutton(janela, text = "pontuação", variable=pontuacaoCpf, onvalue=1, offvalue=0)
cb_pontuacaoCpf.place(x=100, y=150)

#ChecBox para selecionar opção de geração do PIS com ou sem pontuação
cb_pontuacaoCpf = Checkbutton(janela, text = "pontuação", variable=pontuacaoPis, onvalue=1, offvalue=0)
cb_pontuacaoCpf.place(x=100, y=200)

#Botão para chamada da função de ação de click no botão Gerar CPF
botao5 = Button(text=' Gerar CPF ', command=lambda: btn4lick(), bg='gray', fg='black')
botao5.place(x=15, y=130)

#Botão para chamada da função de ação de click no botão Gerar CNPJ
botao6 = Button(text='Gerar CNPJ', command=lambda: btn3Click(), bg='gray', fg='black')
botao6.place(x=15, y=80)

#Botão para chamada da função de ação de click no botão Gerar CNPJ
botao6 = Button(text='Gerar PIS', command=lambda: btn8Click(), bg='gray', fg='black')
botao6.place(x=15, y=175)

janela.mainloop()



