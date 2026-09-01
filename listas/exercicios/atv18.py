def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    temperaturas_ordenadas = sorted(temperaturas)

    return quantidade, soma, media, temperaturas_ordenadas


temperaturas = [25, 30, 22, 28, 26]

print(analisar_temperaturas(temperaturas))