'''Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
#Com cores

from random import choice
cores = {'verde':'\033[1;36;40m','roxo':'\033[1;35;40m','amarelo':'\033[1;33;40m','vermelho':'\033[1;31;40m','verdão':'\033[1;32;40m','limpa':'\033[m'}
a = input('{}Nome numero 1 = {}'.format(cores['verde'],cores['limpa']))
b = input('{}Nome numero 2 = {}'.format(cores['roxo'],cores['limpa']))
c = input('{}Nome numero 3 = {}'.format(cores['amarelo'],cores['limpa']))
d = input('{}Nome numero 4 = {}'.format(cores['vermelho'],cores['limpa']))

lista = [a, b, c, d]
escolhido = choice(lista)
print('{}O aluno escolhido foi {}{}'.format(cores['verdão'],escolhido,cores['limpa']))


