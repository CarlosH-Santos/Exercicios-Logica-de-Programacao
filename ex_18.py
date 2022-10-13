'''Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo qualquer: '))
angulo_rad = radians(angulo)
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f'O angulo {angulo:.0f}º possui: \n* Seno = {seno:.2f} \n* Cosseno = {cosseno:.2f} \n* Tangente = {tangente:.2f}')
