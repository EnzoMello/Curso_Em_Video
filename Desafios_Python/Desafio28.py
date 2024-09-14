#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
print('BEM-VINDO AO ENZOAPP ')

lista = [0,1,2,3,4,5]
escolhido = random.choice(lista) #Eu poderia usar o método random e randint(0,5) para escolher logo um número entre 0 e 5.
print('PROCESSANDO...')
sleep(3)
numero = int(input('Pronto,o computador escolheu um número.Escolha um número de 0 a 5 que você acha que é o escolhido pelo computador: '))
print('ANALISANDO...')
sleep(2)
if numero == escolhido:
    print('Parabéns,você acertou e venceu!!')
else:
    print('Que pena,você perdeu.')