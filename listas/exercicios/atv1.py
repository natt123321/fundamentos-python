def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Maria", "Caio", "Laís", "Jonatas", "Gabriel", "Luana"]
mostrar_nomes(lista_de_nomes)

def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nomes(lista_de_nomes, nome = "Yasmin")