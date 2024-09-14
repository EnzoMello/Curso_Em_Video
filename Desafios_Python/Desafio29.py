#Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80 km/h,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.
print('BEM-VINDO AO ENZOAPP')
from time import sleep

velocidade = float(input('Insira a velocidade do carro(em km/h): '))
print('Verificando no radar....')
sleep(2)
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite e foi multado.A multa é de R$ {:.2f}'.format(multa))

print('Dirija com segurança sempre e tenha um bom dia!')
