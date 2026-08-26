def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Maria", "Caio", "Laís", "Jonatas", "Gabriel", "Luana"]
mostrar_nomes(lista_de_nomes)

def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

ordenar_nomes(lista_de_nomes)