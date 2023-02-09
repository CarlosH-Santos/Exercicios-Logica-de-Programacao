#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.

valor_imovel = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Digite o tempo[anos] que será financiado: '))

parcela = (valor_imovel/anos)/12
salario_porcent = salario * 0.3


print(f'Para pagar um imóvel no valor R$:{valor_imovel:.2f} reais em {anos} anos a prestação mensal será de R$:{parcela:.2f} reais')

if parcela > salario_porcent:
    print('Empréstimo negado!')

else:
    print('Empréstimo aprovado!')

