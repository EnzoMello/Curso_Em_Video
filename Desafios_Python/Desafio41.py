# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade
# Até 9 anos: Mirin
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior 
# Acima: Master

from time import sleep
from datetime import date

ano_atual = date.today().year
ano_de_nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = ano_atual - ano_de_nascimento
print('Verificando...')
sleep(1)

print('=' * 40)

if idade <= 9:
    print('O atleta tem {} anos e está classificado na categoria Mirin.'.format(idade)) 
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos e está classificado na categoria Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e está classificado na categoria Junior.'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e está classificado na categoria Sênior.'.format(idade))
else:
    print('O atleta tem {} anos e está classsificado na categoria Master.'.format(idade))

print('=' * 40)