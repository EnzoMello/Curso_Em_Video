#Escreva um programa que leia dois números inteiros e compare-os,mostrando na tela uma mensagem:
#"O primeiro valor é maior","O segundo valor é maior" e "Não existe valor maior,os dois são iguais".
from time import sleep
print('BEM-VINDO AO ENZOAPP')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
print('Verificando...')
sleep(1)


print('=' * 40)

if n1 > n2:
    print('RESULTADO:O primeiro número é o maior.')
elif n2 > n1:
    print('RESULTADO:O segundo número é o maior.')
else:
    print('RESULTADO:Não existe valor maior,os dois são iguais.')

print('=' * 40)