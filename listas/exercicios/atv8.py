def mostrarnumeros(numeros):
    for numero in numeros:
        print(f"O número da lista é: {numero}")


lista_de_numeros = ["1", "5", "9", "4", "2", "7", "8", "6", "3"]

mostrarnumeros(lista_de_numeros)

def ordenar_numeros(numeros):
    lista_de_numeros_ordenados = sorted(numeros, reverse=True)
    print(f"A lista ordenada é {lista_de_numeros_ordenados}")

ordenar_numeros(lista_de_numeros)