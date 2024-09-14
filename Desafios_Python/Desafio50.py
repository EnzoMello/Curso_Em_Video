# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.Se o número for ímpar desconsidere-o
print("BEM-VINDO AO ENZOAPP")

soma = 0
cont = 0

print("Soma de números pares...")
print("=" * 20)
for c in range(0,6):
    n = int(input("Insira um número: "))
    if n % 2 == 0:
        soma += n
        cont += 1
        print('Você informou {} números e a soma foi {}'.format(cont, soma))
print("FIM")
print("=" * 20)