from funcoes import verificar_idade, calcularDesconto, calcular_imc

def mensagem_futuro(nome: str, idade: int, anos: int = 5) -> str:
    return f"Olá, {nome} daqui {anos} anos você tera {idade + anos} anos de idade"


if __name__ == "__main__":
    nome = input("Seu nome: ")
    idade = int(input("Sua idade: "))

    print(mensagem_futuro(nome, idade))


    print(verificar_idade(idade))
    print(calcularDesconto(100, 10))
    # print(calcular_imc(63, 1.4))
    print(f"Seu IMC é de {calcular_imc(63, 1.6):.1f}")