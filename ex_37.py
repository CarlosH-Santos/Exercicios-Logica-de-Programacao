#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um numero inteiro para conversão: '))
print('''Escolha a base de conversão:'
      [1] = Binário
      [2] = Octal
      [3] = Hexadecimal''')

escolha = int(input('Digite a opção desejada: '))

if escolha == 1:
      print(f'{bin(numero)[2:]}')

elif escolha == 2:
      print(f'{oct(numero)[2:]}')

elif escolha == 3:
      print(f'{hex(numero)[2:]}')

else:
      print('Opção inválida!')
