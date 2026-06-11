def calcular_desconto(preco: float, taxa: float = 0.1) -> tuple[float, float]:
    desconto = preco * taxa
    preco_final = preco - desconto
    return desconto, preco_final


if __name__ == "__main__":
    preco = int(input("qual o valor do produto? "))

    desconto, preco_final = calcular_desconto(preco)
    print(f"O desconto é de {desconto}")
    print(f"O preço do produto com desconto é de {preco_final:.0f} reais")
