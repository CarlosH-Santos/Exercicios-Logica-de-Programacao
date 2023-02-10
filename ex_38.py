#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

primeiro_valor = int(input('Digite o primeiro valor inteiro: '))
segundo_valor = int(input('Digite o segundo valor inteiro: '))

if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior!')

elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior!')

else:
    print('Os valores são iguais!')


