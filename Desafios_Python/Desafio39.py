# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou da hora.
# Seu programa também deverá mostrar o tempo que falta ou se já passou do prazo.
from time import sleep
from datetime import date 

print('BEM-VINDO AO ENZOAPP')

atual = date.today().year
ano_nascimento = int(input("Qual seu ano de nascimento? "))
calculo_alistamento = atual - ano_nascimento


print('Verificando...')
sleep(1)

print('=' * 40)

if calculo_alistamento < 18:
    tempo_faltante = 18 - calculo_alistamento
    saldo = atual + tempo_faltante
    print('Você ainda irá se alistar no exército brasileiro.')
    print('Faltam {} anos para você se alistar.'.format(tempo_faltante))
    print('Seu alistamento será em {}'.format(saldo))

elif calculo_alistamento == 18:
    print('Seu alistamento será IMEDIATAMENTE.')

else:
    tempo_faltante = calculo_alistamento - 18
    saldo = atual - tempo_faltante
    print('Se apresse, sua hora de se alistar já passou.')
    print('Você está atrasado {} ano(s).'.format(tempo_faltante))
    print('Seu alistamento foi em {}'.format(saldo))

print('=' * 40)
