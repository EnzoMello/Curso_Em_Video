#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
print('BEM-VINDO AO ENZOAPP')

numero = int(input('Insira o número: '))
par = numero % 2
if par == 0:
    print('Esse número é par.')
else:
    print('Esse número é ímpar.')