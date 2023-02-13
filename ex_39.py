#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year

ano_nasc = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - ano_nasc
falta = 18 - idade
passou = idade - 18


if idade < 18:
    alista = falta + ano_atual
    print(f'Você tem {idade} anos!\nFalta {falta} anos para se alistar\nSeu alistamento será em {alista}')

elif idade > 18:
    alist = ano_atual - passou
    print(f'Você tem {idade} anos!\nPassou {passou} anos do período de alistamento!\nSeu alistamento foi em {alist}')

else:
    print(f'Você tem {idade} anos!\nEste é o ano do seu alistamento!')

