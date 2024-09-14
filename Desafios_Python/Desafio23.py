#Faça um programa que leia um número de 0 a 9999 e mostre cada um dos dígitos separados na forma de unidade,dezena,centena e milhar.

print('BEM-VINDO AO ENZOAPP')

numero = int(input('Insira o número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))