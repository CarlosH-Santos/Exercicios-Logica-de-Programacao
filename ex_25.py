#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo : ')).upper()

if 'SILVA' in nome:
    print('Possui SILVA')
else:
    print('Não possui SILVA')
