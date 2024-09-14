#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
import math

print('BEM-VINDO AO ENZOAPP')
num = float(input("Digite um número: "))
num_final = math.trunc(num)

print('A porção inteira do número {} é {}'.format(num, num_final)) #Poderia ser math.trunc(num) logo direto no lugar de num_final.