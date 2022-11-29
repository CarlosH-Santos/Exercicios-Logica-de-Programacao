#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input('Digite uma frase : ')).upper()
nome1 = nome.replace(' ', '')
n1 = nome1.count('A')
n2 = nome1.count('Á')
print('O numero de letras ''A'' na frase é = {} '.format(n1+n2))
print('A primeira vez que aparece é na posição {} '.format(nome1.find('A')+1))
print('A ultima vez em que aparece é na posição {} '.format(nome1.rfind('A')+1))

