#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,calcule e mostre o comprimento da sua hipotenusa
import math

cateto_oposto = float(input("Insira o valor do cateto oposto: "))
cateto_adjacente = float(input("Insira o valor do cateto adjacente: "))
somatorio = cateto_oposto**2 + cateto_adjacente**2
hipotenusa = math.sqrt(somatorio) #Poderia usar math.hypot(cateto_oposto, cateto_adjacente)

print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

#O math.hypot é um math que calcula diretamente a hipotenusa utilizando dois parâmetros