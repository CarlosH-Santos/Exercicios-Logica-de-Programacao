'''Exercício Python 017: Façaum programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo.Calcule e mostre o comprimento da hipotenusa.'''  # Com cores!

from math import hypot
cores = {'azul':'\033[4;34;40m',
         'verde':'\033[4;32;40m',
        'amarelo':'\033[4;33;40m',
         'limpa':'\033[m'}

co = float(input('{}Cateto oposto = {}'.format(cores['azul'], cores['limpa'])))
ca = float(input('{}Cateto adjacente = {}'.format(cores['amarelo'], cores['limpa'])))
hp = hypot(co, ca)
print('{}O comprimento da hipotenusa é = {:.2f} {}'.format(cores['verde'], hp, cores['limpa']))
