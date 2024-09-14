#Desenvolva um programa que pergunte a distância de uma viagem em km.Calcule o preço da passagem,cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
from time import sleep
print('BEM-VINDO AO ENZOAPP')

distancia = float(input('Distância da viagem em km: '))
print('Analisando valor...')
sleep(1)
if distancia <= 200:
    preco_passagem = distancia * 0.50
    print('O preço da passagem é R$ {:.2f}'.format(preco_passagem))
else:
    preco_passagem = distancia * 0.45
    print('O preço da passagem é R${:.2f}'.format(preco_passagem))