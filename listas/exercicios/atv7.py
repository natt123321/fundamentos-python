def mostrarfrutas(frutas):
    for fruta in frutas:
        print(f"A fruta da lista é: {fruta}")


lista_de_frutas = ["Morango", "Amora", "Banana", "Maçã", "Maracujá", "Limão"]

mostrarfrutas(lista_de_frutas)

def quantidadeelementos(frutas):
    quantidade = len(frutas)
    print(f"A quantidade de frutas da lista é {quantidade}")

quantidadeelementos(lista_de_frutas)