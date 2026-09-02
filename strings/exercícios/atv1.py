def formatar_nome(nome):
    # nome em maiusculo
    nome_maiusculo = nome.upper()

    return (nome_maiusculo)

nome = input("Digite seu nome: ")

nome_maiusculo = formatar_nome(nome)
print(f"Nome maiúsculo: {nome_maiusculo}")