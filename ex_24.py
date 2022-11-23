#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = str(input('Digite o nome da cidade em que você nasceu: ')).upper().strip().split()
if nome[0] == 'SANTO':
    print('True')
else:
    print('False')

