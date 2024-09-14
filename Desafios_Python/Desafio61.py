# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, lendo os 10 primeiros termos da progressão usando a estrutura while.
print("BEM-VINDO AO ENZOAPP")

print("=" * 32)
n1 = int(input("Coloque o primeiro termo da PA: "))
razao = int(input("Coloque a razão da PA: "))
cont = 1
print('=' * 32)

while cont <= 10:
    n1 += razao
    cont += 1
    print("{}".format(n1))