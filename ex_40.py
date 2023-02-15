#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
media = (nota_1 + nota_2) / 2
print(f'Sua média é {media:.1f}')

if media >= 7.0:
    print('Você foi aprovado!')

elif media == 5 and media <= 6.9:
    print('Você está de recuperação!')

else:
    print('Você está de recuperação!')
