#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distância de sua viagem em km: '))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O valor da sua viagem é R$:{valor:.2f} reais')
