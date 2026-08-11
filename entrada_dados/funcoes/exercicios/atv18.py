def valorproduto():
    produto = float(input("Qual o valor do produto?"))
    return produto

def qtdeparcelas():
    parcela = int(input("Quantas parcelas?"))
    return parcela

def valorcadaparcela():
    valorparcela = produto / parcela
    return valorparcela

produto = valorproduto()
parcela = qtdeparcelas()
valorparcela = valorcadaparcela()

print(f"O valor de cada parcela ficará de {valorparcela}")