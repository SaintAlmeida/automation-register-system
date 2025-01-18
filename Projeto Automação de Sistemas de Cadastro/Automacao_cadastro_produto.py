import pyautogui as pa
from time import sleep

#Clicar e inserir o usuário
pa.click(1073,310, duration=2)
pa.write("saint")

#Clicar e inserir a senha
pa.click(1071,334, duration=2)
pa.write('123456')

#clicar em "Entrar" para abrir o sistema
pa.click(972,364)

#Extrair do arquivo Produtos
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
       produto =  linha.split(',')[0]
       quantidade = linha.split(',')[1]
       preco =  linha.split(',')[2]

#Clicar e digitar o produto
pa.click(428,374, duration=1)
pa.write(produto)

#Clicar e digitar Quantidade
pa.click(428,398, duration=1)
pa.write(quantidade)

#Clicar e digitar Preço
pa.click(428,428, duration=1)     
pa.write(preco)

#Clicar em Registrar
pa.click(324,585, duration=1)

sleep(2)