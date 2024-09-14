#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

print('BEM-VINDO AO ENZOAPP')
valor = float(input('Insira o valor(em metros): '))
centimetros = valor * 100
milimetros = valor * 1000

print(' O valor em centímetros é {:.0f} cm. \n O valor em milímetros é {:.0f} mm.'.format(centimetros, milimetros))