#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
print('BEM-VINDO AO ENZOAPP')

nome = str(input('Digite o nome da cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')
