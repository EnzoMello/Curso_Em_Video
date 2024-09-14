#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas
#Quantas letras ao todo,sem considerar espaços
#Quantas letras tem o primeiro nome

print('BEM-VINDO AO ENZOAPP')

nome = str(input("Insira seu nome completo: "))

print('Nome em maiúsculo é: {}'.format(nome.upper()))
print('Nome em minúsculo é: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))