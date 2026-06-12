def calcularDesconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

if __name__ == "__main__":

    valor_final = calcularDesconto(1040, 20)

    print(f"O valor final é de R$ {valor_final:.2f} reais")
