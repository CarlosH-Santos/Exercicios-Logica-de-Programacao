#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero de 0 a 9999: '))
print(f'Unidade = {numero // 1 % 10}\nDezena = {numero // 10 % 10}\nCentena = {numero // 100 % 10}\n'
      f'Milhar = {numero // 1000 % 10}')




