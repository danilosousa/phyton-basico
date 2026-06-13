def calcularDesconto(preco, porcentagem):
    return preco - (preco * porcentagem / 100)

if __name__ == "__main__":

    valor_final = calcularDesconto(1040, 20)

    print(f"O valor final é de R$ {valor_final:.2f} reais")


def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

if __name__ == "__main__":
    idade = int(input("Digite a sua idade: "))
    print(verificar_idade(idade))


def calcular_imc(peso, altura):
    return peso / (altura ** 2)

if __name__ == "__main__":
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))
    print(calcular_imc(peso, altura))
    print(f"Seu IMC é de {calcular_imc(peso, altura):.1f}")
