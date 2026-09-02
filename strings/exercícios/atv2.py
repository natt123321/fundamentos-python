def formatar_nome(nome):
    # nome em minusculo
    nome_minusculo = nome.lower()

    return (nome_minusculo)

nome = input("Digite seu nome: ")

nome_minusculo = formatar_nome(nome)
print(f"Nome minúsculo: {nome_minusculo}")