#pip install pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar
#pyautogui.prees -> pressionar uma tecla
#pyautogui.write -> escrever
#pyautogui.hotkey -> atalho de teclado (ctrl, C)

#passo 1: abrir o sistema da empresa:

#abrir o chrome 
#apertar a tecla win
pyautogui.press("win")

#digitar o texto chrome
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#pedir pro computador esperar 3 segundos
time.sleep(3)

#passo 2: fazer login
pyautogui.click(x=659, y=465)
pyautogui.write("filipe@gmail.com")

pyautogui.press("tab") #passar para o campo senha
pyautogui.write("minhasenha123")

pyautogui.press("tab") #passar para "login"
pyautogui.press("enter")


#passo 3: importar a base de dados dos protutos
#pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("1° produtos.csv")

print(tabela)

time.sleep(2)
#passo 4: cadastrar 1 produto 

for linha in tabela.index:
    pyautogui.click(x=674, y=329) #clica no 1º campo

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc [linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc [linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc [linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    custo = tabela.loc [linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc [linha, "obs"]

    if obs != "nan":
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    pyautogui.press("enter") #apertar o botao de enter

    #numero positivo = scrooll para cima
    #numero negotivo = scroll para baixo
    pyautogui.scroll(10000)

#passo 5: repetir o passo 4 ate acabar todos os produtos

#nan = valor vazio em uma base de dados
#not a number
