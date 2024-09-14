#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print("BEM-VINDO AO ENZOAPP")


print("10 Primeiros termos da PA")

print("=" * 20)
n1 = int(input("Primeiro termo da PA: "))
razao = int(input('Razão da PA: '))
for c in range(n1, n1 + razao * 10, razao):
    print(c)
print("=" * 20)