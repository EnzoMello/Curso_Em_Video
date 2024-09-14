#Escreva um programa que pergunte a quantidade de km rodados por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,sabendo que o carro custa
# 60 R$ por dia e 0.15 R$ por km rodado.

print('BEM-VINDO AO ENZOAPP')
km_rodado = float(input('Quantos km o carro rodou? '))
dias_alugados = int(input('Quantos dias o carro foi alugado? '))
preço = (km_rodado * 0.15) + (dias_alugados * 60)

print('O preço do aluguel do carro é {:.2f} R$'.format(preço))