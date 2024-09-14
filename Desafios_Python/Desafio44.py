# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal; 3x ou mais no cartão: 20% de juros
from time import sleep

print("BEM-VINDO AO ENZOAPP")
print('1 = À vista dinheiro/cheque \n 2 = À vista no cartão \n 3 = 2X no cartão \n 4 = 3X ou mais no cartão')

print("=" * 20)
preço = float(input("Coloque o preço do produto: "))
opção = int(input("Qual opção de pagamento? "))
print("=" * 20)

if opção == 1:
    valor = preço * 0.9
    print(" O preço a pagar, com 10% de desconto, é: {:.2f}".format(valor))
elif opção == 2:
    valor = preço * 0.95
    print(" O preço a pagar, com 5% de desconto, é: {:.2f}".format(valor))
elif opção == 3:
    valor = preço / 2
    print("Sua compra será dividida em 2X de {:.2f} R$".format(valor))
    print(" O preço a pagar não tem desconto e por isso o valor final será: {:.2f}".format(preço))
elif opção == 4:
    valor = preço * 1.20
    parcela = int(input("Quantas parcelas? "))
    parcela2 = valor / parcela
    print("Sua compra será dividida em {}X de {:.2f} R$ COM JUROS".format(parcela, parcela2))
    print(" O preço a pagar de {:.2f} tem 20% de juros e por isso seu valor final é: {:.2f}".format(preço, valor))
else:
    print("Opção inválida de pagamento, tente novamente.")
