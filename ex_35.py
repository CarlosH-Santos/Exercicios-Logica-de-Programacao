#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.

a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor da reta b: '))
c = float(input('Digite o valor da reta c: '))

if a + b > c and a + c > b and c + b > a:
    print('É um triângulo!')
else:
    print('Não pode formar um triângulo!')