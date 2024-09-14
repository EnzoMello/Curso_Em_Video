#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ainda não atingiram.
from datetime import date
print('=' * 20)
print('BEM-VINDO AO ENZOAPP')
print('=' * 20)

maior = 0
menor = 0
ano_atual = date.today().year

for c in range(1,8):
    ano = int(input("Qual o número que você nasceu? "))

    if ano + 18 >= ano_atual:
        maior += 1
    else:
        menor += 1
print('=' * 20)
print('A quantidade de pessoas que atingiram a maioridade é {}. \nA quantidade de pessoas menores de idade é {}.'.format(maior, menor))
print('=' * 20)