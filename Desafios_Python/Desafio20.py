#O mesmo professor do desafio anterior quer sortear a ordem de apresentação do trabalho dos quatro alunos.Faça um programa que leia o nome dos quatro alunos e diga a ordem de apresentação.
import random
print('BEM-VINDO AO ENZOAPP')

n1 = str(input("Nome do primeiro aluno: "))
n2 = str(input("Nome do segundo aluno: "))
n3 = str(input("Nome do terceiro aluno: "))
n4 = str(input("Nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)

print("A ordem de apresentação é: ")
print(lista)