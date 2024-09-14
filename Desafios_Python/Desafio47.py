# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50
print("=" * 20)
print("BEM-VINDO AO ENZO APP")
print("=" * 20)


print("Números pares entre 1 e 50...")

print("=" * 20)
for par in range(1, 51, 2):
    if par % 2 == 0:
        print(par)
print("FIM")
print("=" * 20)