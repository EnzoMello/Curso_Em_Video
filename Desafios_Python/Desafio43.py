# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25: Peso Ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade Mórbida

from time import sleep

print('-' * 20)
print("BEM-VINDO AO ENZOAPP")
print('-' * 20)

peso = float(input("Coloque o peso da pessoa: "))
altura = float(input("Coloque a altura da pessoa: "))
imc = peso / (altura**2)
print('Verificando...')
sleep(1)

if imc < 18.5:
    print('CONDIÇÃO: Abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('CONDIÇÃO: Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('CONDIÇÃO: Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('CONDIÇÃO: Obesidade.')
else:
    print('CONDIÇAÕ: Obesidade Mórbida.')