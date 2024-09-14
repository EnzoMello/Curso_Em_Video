#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
print("BEM-VINDO AO ENZOAPP")


print("=" * 15)
sexo = str(input("Insira o sexo da pessoa [M/F]: ")).upper()
print("=" * 15)

if sexo == "M":
    print("O sexo escolhido é Masculino.")
elif sexo == "F":
    print("O sexo escolhido é Feminino.")

while sexo not in "MmFf":
    sexo = str(input("Sexo inválido.Por favor,confirme seu sexo.")).upper()
    if sexo == "M":
        print("O sexo escolhido é Masculino.")
    elif sexo == "F":
        print("O sexo escolhido é Feminino.")