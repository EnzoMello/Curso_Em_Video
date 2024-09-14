#Refaça o desafio 49, mostrando a tabuada de um número que o usuário escolher. Porém, agora faça usando laço for.
print("=" * 20)
print("BEM-VINDO AO ENZOAPP")
print("=" * 20)

print("Tabuada usando for...")
n = int(input("Insira um número: "))

print('-' * 20)
for c in range(0, 11):
    print("{} X {} = {}".format(n, c, n * c))
print("FIM")
print('-' * 20)
