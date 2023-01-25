#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep

numero = int(input("Digite um numero de 0 a 5: "))
numero_pc = randint(0, 5)

print('Carregando....')
sleep(1)

print(f'Seu numero: {numero}')
print(f'Numero do computador: {numero_pc}')

if numero == numero_pc:
    print('Parabéns você acertou!')
else:
    print('Tente outra vez!')

