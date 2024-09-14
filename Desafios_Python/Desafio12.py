#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.
print('BEM-VINDO AO ENZOAPP')

preco = float(input('Preço do produto: '))
novo_preco = preco - (preco * 0.05)

print('O novo preço do produto,reajustado com o desconto de 5%, é: {:.2f} R$'.format(novo_preco))