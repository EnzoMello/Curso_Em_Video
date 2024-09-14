# Crie um programa que leia dois valores e mostre um menu como ao lado na tela: Seu programa deverá realizar a operação solicitada em cada caso. 
from time import sleep
print("BEM-VINDO AO ENZOAPP")

print("-=" * 20)
n1 = int(input("Coloque o primeiro valor: "))
n2 = int(input("Coloque o segundo valor: "))
opcao = 0
while opcao != 5:
    print('''   [1] Somar os números
    [2] Multiplicar os números
    [3] Definir maior número
    [4] Adicionar novos números
    [5] Sair do programa''')
    print("-=" * 20)
    opcao = int(input("Qual opção você escolhe? "))
    print("=" * 25)
    if opcao == 1:
        print("Somando...")
        sleep(1)
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        print("Multiplicando...")
        sleep(1)
        multiplicacao = n1 * n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, multiplicacao))
    elif opcao == 3:
        print("Definindo maior número...")
        sleep(1)
        if n1 > n2:
            print("O número {} é maior que {}".format(n1, n2))
        else:
            print("O número {} é maior que {}".format(n2, n1))
    elif opcao == 4:
        print("Adicione novos número abaixo:")
        n1 = int(input("Novo número 01: "))
        n2 = int(input("Novo número 02: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(1)        
    else:
        print("Opção inválida.Por favor,tente de novo.")
print("=" * 25)
print("Fim do programa,volte sempre!!")