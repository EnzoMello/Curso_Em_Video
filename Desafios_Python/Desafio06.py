#Crie um algoritmo que leia um número e mostre o seu dobro,o triplo e a raíz quadrada

print('BEM-VINDO AO ENZOAPP')

n1=int(input('Insira o número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)


print('O dobro do número lido é {}. \n O triplo do número lido é {}. \n A raíz quadrada de {} é {:.2f}'.format(dobro, triplo, n1, raiz))