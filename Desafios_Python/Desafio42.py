#Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo. Porém,acrescente o recurso de que tipo de triâng. será formado.
# Equilátero: todos os lados iguais; Isósceles: Dois lados iguais; Escaleno: Todos os lados diferentes.

from time import sleep

print('_' * 20)
print('BEM-VINDO AO ENZOAPP')
print('_' * 20)

reta1 = float(input("Valor da reta 1: "))
reta2 = float(input("Valor da reta 2: "))
reta3 = float(input("Valor da reta 3: "))
print('Verificando...')
sleep(1)


print("=" * 40)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Esses valores podem formar um triângulo.")
    if reta1 == reta2 == reta3:
        print("O triângulo formado será equilátero.")
    elif reta1 != reta2 != reta3 != reta1:
        print("O triângulo formado será escaleno.")
    else:
        print("O triângulo formado será isósceles.")

else: 
    print("Esses valores não podem formar um triângulo.")
print("=" * 40)
