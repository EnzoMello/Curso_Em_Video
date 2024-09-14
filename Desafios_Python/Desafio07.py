#Desenvolva um programa que leia as duas notas de um aluno,calcule e mostre sua média.

print('BEM-VINDO AO ENZOAPP')
nota_1 = float(input('Escreva a primeira nota: '))
nota_2 = float(input('Escreva a segunda nota: '))
media_final = (nota_1 + nota_2) / 2

print('A nota final do aluno é igual a {:.2f}'.format(media_final))