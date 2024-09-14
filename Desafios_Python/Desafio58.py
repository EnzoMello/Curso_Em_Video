# Melhore o jogo do desafio 28, onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
import random
from time import sleep
print("BEM-VINDO AO ENZOAPP")

lista = [1,2,3,4,5,6,7,8,9]
escolhido = random.choice(lista)

print('=' * 67)
n = int(input("O computador escolheu um número entre 0 e 10.Tente acertar: "))
print('=' * 67)

while n != escolhido:
    n = int(input("Tente novamente: "))
    if n == escolhido:
        print('=' * 65)
        print("Meus parabéns, você acertou!! O número escolhido pelo computador foi {}.".format(escolhido))
        print('=' * 65)
