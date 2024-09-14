#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários superiores a R$1250,00,calcule um aumento de 10%
#Para os inferiores ou iguais,o aumento é de 15%.
print('BEM-VINDO AO ENZOAPP')

salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    aumento = salario * 0.10
    salario_novo = salario * 1.15
else:
    aumento = salario * 0.15
    salario_novo = salario * 1.15
print('O aumento será de R$ {:.2f} e o novo salário passará a ser R$ {:.2f}'.format(aumento,salario_novo))
