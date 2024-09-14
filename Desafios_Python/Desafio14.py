#Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit.
print('BEM-VINDO AO ENZOAPP') 
temperatura_celsius = float(input('Insira a temperatura em Celsius: '))
temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32

print('A temperatura {} graus Celsius é igual a {:.2f} graus Fahrenheit'.format(temperatura_celsius, temperatura_fahrenheit))