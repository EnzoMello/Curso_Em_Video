# Faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta necessária para pintá-la,sabendo que cada litro de tinta,pinta uma área de 2m2
print('BEM-VINDO AO ENZOAPP')

largura = float(input('Largura da parede é: '))
altura = float(input('Altura da parede é: '))
area = largura * altura
quantidade_de_tinta = area / 2

print('A área da sua parede é {:.2f} metros quadrados. \n A quantidade de tinta necessária para pintar a parede é equivalente a {:.2f} litros.'.format(area, quantidade_de_tinta))