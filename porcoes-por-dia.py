total_porcoes = int(input("Quantas porções do produto você tem? "))

total_dias = int(input("Quantos dias você vai usar o produto? "))

dias_de_consumo = total_porcoes / total_dias

print(f"Você vai usar por {total_dias} dias")
print(f"Você precisa de {dias_de_consumo:.0f} porções")