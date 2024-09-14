# Faça um programa que leia um número qualquer e mostre seu fatorial
print("BEM-VINDO AO ENZOAPP")

n = int(input("Coloque o número: "))
count = n
f = 1
print("Calculando {}!".format(n))
while count > 0:
    print("{} ".format(count), end = ' ')
    print('X ' if count > 1 else '= ', end = ' ')
    f *= count
    count -= 1
print('{} '.format(f))