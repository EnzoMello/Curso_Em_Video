#Crie um programa que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem no final,de acordo com a média atingida: 
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
from time import sleep

print('BEM-VINDO AO ENZOAPP')

print('=' * 32)
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
print('=' * 32)

print('VERIFICANDO...')
sleep(1)
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.2f}.')

print("..." * 12)
if media < 5.0:
    print('Resultado = REPROVADO')
elif media >= 5.0 and media < 7.0:
    print('Resultado = RECUPERAÇÃO')
else:
    print('Resultado = APROVADO')
print("..." * 12)