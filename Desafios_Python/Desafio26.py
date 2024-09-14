#Faça um programa que leia uma frase pelo teclado e mostre: 
#Quantas vezes a letra 'A' aparece na frase.
#Qual a posição em que aparece a primeira letra 'A'.
#Qual a posição em que aparece a última letra 'A'.
print('BEM-VINDO AO ENZOAPP')

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} veze(s) na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') + 1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A') + 1))