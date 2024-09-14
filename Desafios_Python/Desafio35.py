#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.
print('BEM-VINDO AO ENZOAPP')

reta1 = float(input('Comprimento da reta 1: '))
reta2 = float(input('Comprimento da reta 2: '))
reta3 = float(input('Comprimento da reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')