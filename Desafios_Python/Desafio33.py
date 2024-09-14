#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('BEM-VINDO AO ENZOAPP')

n1 = float(input("Coloque o número 1: "))
n2 = float(input("Coloque o número 2: "))
n3 = float(input("Coloque o número 3: "))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))