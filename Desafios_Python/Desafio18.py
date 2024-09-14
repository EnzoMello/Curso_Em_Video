#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse ângulo
import math

print('BEM-VINDO AO ENZOAPP')
angulo = float(input("Coloque o valor do ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo {} tem seno igual {:.2f},cosseno igual {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))