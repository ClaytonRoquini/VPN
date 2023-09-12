import random
import pyautogui
import pyperclip
import time
from tkinter import *
import subprocess




def conectarVpn1():
    subprocess.Popen('C:\Program Files\Fortinet\FortiClient\FortiClient.exe')
    pyautogui.PAUSE = 1
    time.sleep(5)
    pyautogui.click(x=1103,y=627)
    pyautogui.click(x=938,y=673)
    pyautogui.click(x=898,y=693)
    texto = '''Meleloah88'''
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey('alt', 'F4')

def conectarVpn2():
    subprocess.Popen('C:\Program Files\Fortinet\FortiClient\FortiClient.exe')
    pyautogui.PAUSE = 1
    time.sleep(5)
    pyautogui.click(x=1103, y=627)
    pyautogui.click(x=918,y=692)
    pyautogui.click(x=898, y=693)
    texto = '''Meleloah88'''
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey('alt', 'F4')

def abrirChrome():
    #subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
    #pyautogui.PAUSE = 1
    #time.sleep(3)
    # Maximiza chrome
    #pyautogui.click(x=125, y=1063)
    # Abrir Chrome
    pyautogui.click(x=125, y=1063)
    time.sleep(1)
    # Jira
    pyautogui.click(x=72, y=80)

    # Nova aba 2
    pyautogui.click(x=267, y=15)
    # Planer
    pyautogui.click(x=1510, y=79)
    # Nova aba 3
    pyautogui.click(x=511, y=14)
    # Bimmer
    pyautogui.click(x=1599, y=82)
    time.sleep(4)
    # Clica Senha
    pyautogui.click(x=863, y=467)
    time.sleep(1)
    # Selecionar senha salva
    pyautogui.click(x=1016, y=522)
    time.sleep(1)
    # Avançar
    pyautogui.hotkey('enter')
    time.sleep(8)
    # Geral
    pyautogui.click(x=812, y=125)
    # Agenda
    pyautogui.click(x=820, y=167)
    # Nova aba 4
    pyautogui.click(x=748, y=15)
    # EmailGoogle
    pyautogui.click(x=1715, y=81)
    #Chat Google
    pyautogui.click(x=365, y=1062)
    # Gerenciador de VM
    pyautogui.click(x=269, y=1066)

def all():
    subprocess.Popen('C:\Program Files\Fortinet\FortiClient\FortiClient.exe')
    pyautogui.PAUSE = 1
    time.sleep(5)
    pyautogui.click(x=1103, y=627)
    pyautogui.click(x=938, y=673)
    pyautogui.click(x=898, y=693)
    texto = '''Meleloah88'''
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')
    time.sleep(11)
    pyautogui.hotkey('alt', 'F4')
    #subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
    #pyautogui.PAUSE = 1
    #time.sleep(3)
    # Abrir Chrome
    pyautogui.click(x=125, y=1063)
    time.sleep(1)
    # Jira
    pyautogui.click(x=72, y=80)
    # Nova aba 2
    pyautogui.click(x=267, y=15)
    # Planer
    pyautogui.click(x=1510, y=79)
    # Nova aba 3
    pyautogui.click(x=511, y=14)
    # Bimmer
    pyautogui.click(x=1599, y=82)
    time.sleep(4)
    # Clica Senha
    pyautogui.click(x=863, y=467)
    time.sleep(1)
    # Selecionar senha salva
    pyautogui.click(x=1016, y=522)
    time.sleep(1)
    # Avançar
    pyautogui.hotkey('enter')
    time.sleep(8)
    # Geral
    pyautogui.click(x=812, y=125)
    # Agenda
    pyautogui.click(x=820, y=167)
    # Nova aba 4
    pyautogui.click(x=748, y=15)
    # EmailGoogle
    pyautogui.click(x=1715, y=81)
    # Chat Google
    pyautogui.click(x=319, y=1061)
    # Gerenciador de VM
    pyautogui.click(x=269, y=1066)




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
texto1.place(x=130, y=10)

#Variaveis Globais
pontuacaoCnpj = IntVar()
pontuacaoCpf = IntVar()
pontuacaoPis = IntVar()

botao1 = Button(text='VPN PRO1', command=lambda: conectarVpn1(), bg='gray', fg='black')
botao1.place(x=15, y=40)

botao2 = Button(text='VPN PRO2', command=lambda: conectarVpn2(), bg='gray', fg='black')
botao2.place(x=100, y=40)

botao3 = Button(text='CHROME', command=lambda: abrirChrome(), bg='gray', fg='black')
botao3.place(x=185, y=40)

botao4 = Button(text='TODOS', command=lambda: all(), bg='gray', fg='black')
botao4.place(x=260, y=40)

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



