#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:

# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input(str('Digite o seu nome completo: ')).strip()
cont = 0
primeiro_nome = nome.strip().split()

for letra in nome:
    if letra == ' ':
        pass
    else:
        cont += 1

print(f'Com letras maiusculas: {nome.upper()}')
print(f'Com letras minusculas: {nome.lower()}')
print(f'O total de letras foram : {cont} letras')
print(f'O primeiro nome tem: {len(primeiro_nome[0])} letras')

