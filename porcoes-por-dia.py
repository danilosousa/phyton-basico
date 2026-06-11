def calcular_porcoes_por_dia(total_porcoes: int, total_dias: int) -> float:
    return total_porcoes / total_dias


if __name__ == "__main__":
    total_porcoes = int(input("Quantas porções do produto você tem? "))
    total_dias = int(input("Quantos dias você vai usar o produto? "))

    porcoes_por_dia = calcular_porcoes_por_dia(total_porcoes, total_dias)

    print(f"Você vai usar por {total_dias} dias")
    print(f"Você precisa de {porcoes_por_dia:.0f} porções")
