#Crie um programa que leia um nome de uma string e diga se ela tem "SILVA" no nome
print('BEM-VINDO AO ENZOAPP')

nome = str(input('Insira seu nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))