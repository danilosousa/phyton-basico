# idade maior ou igual a 18 é adulto

idade  = int(input("Qual a sua idade? "))
carteira = True

verificador_idade = idade >= 18 and carteira

if verificador_idade:
    print("Você é adulto e pode dirigir")
else:
    print("Você não é adulto e não pode dirigir")


