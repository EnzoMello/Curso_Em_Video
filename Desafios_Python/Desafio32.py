#Faça um programa que leia um número qualquer e diga se ele é ou não bissexto.
from datetime import date
print('BEM-VINDO AO ENZOAPP')

ano = int(input('Digite o ano que você quer analisar(Digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO.'.format(ano))