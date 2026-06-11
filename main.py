def mensagem_futuro(nome: str, idade: int, anos: int = 5) -> str:
    return f"Olá, {nome} daqui {anos} anos você tera {idade + anos} anos de idade"


if __name__ == "__main__":
    nome = input("Seu nome: ")
    idade = int(input("Sua idade: "))

    print(mensagem_futuro(nome, idade))
