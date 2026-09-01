def criar_ranking(pontuacoes):
    notas_ordenadas = sorted(pontuacoes, reverse=True)

    return notas_ordenadas


lista_de_pontuacoes = [100, 150, 200, 750, 500, 300, 450, 600]

print(f"Notas ordenadas = {criar_ranking(lista_de_pontuacoes)}")