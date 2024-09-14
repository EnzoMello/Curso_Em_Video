#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.O programa vai perguntar o valor da casa,o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal,sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
print('BEM-VINDO AO ENZOAPP')

valor_da_casa = float(input('Insira o valor da casa: '))
salario = float(input('Insira o salário do comprador: '))
anos_pagar = int(input('Insira em quantos anos o comprador vai pagar: '))

prestacao_mensal = valor_da_casa / (anos_pagar * 12)

if prestacao_mensal > salario * 0.3:
    print('O empréstimo foi negado,a parcela é R$ {:.2f} e é superior a 30% do seu salário.'.format(prestacao_mensal))
else:
    print('Meus parabéns,seu empréstimo foi aprovado!! Lembre-se que sua parcela é R$ {:.2f}'.format(prestacao_mensal))