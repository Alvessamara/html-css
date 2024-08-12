#Passo a passo do projeto
#passo 1:Entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
#passo 2: fazer login
#passo 3 : importar a base de dados
#passo 4: cadastrar 1 produto
#passo 5:repetir o processo do cadastro até acabar a base de dados

import pyautogui 
#pyautogui.click -clicar em algum lugar da tela
#pyautogui.write-escrever um texto
#pyautogui.press- pressionar 1 tecla do teclado

pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")

link= "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
