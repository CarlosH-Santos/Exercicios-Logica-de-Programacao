'''Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

a = input('Nome 01 = ')
b = input('Nome 02 = ')
c = input('Nome 03 = ')
d = input('Nome 04 = ')
lista = [a, b, c, d]
shuffle(lista)

print('A ordem de apresentação é = ')
print(lista)
