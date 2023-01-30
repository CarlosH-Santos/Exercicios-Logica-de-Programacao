#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um nao para verificação["0" seleciona o ano atual]: '))
ano_atual = date.today().year

if ano == 0:
    print(f'Ano atual {ano_atual}')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é Bissexto')

else:
    print('O ano não é Bissexto!')



