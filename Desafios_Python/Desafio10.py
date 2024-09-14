#Leia um programa que leia quanto de dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.1 Dólar = R$ 3,27
print('BEM-VINDO AO ENZOAPP')
dinheiro = float(input('Quanto dinheiro você tem na carteira: '))
dolares = dinheiro / 3.27

print('Você pode comprar {:.2f} dólares.'.format(dolares))