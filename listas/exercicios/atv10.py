def mostrarnumeros(numeros):
    for numero in numeros:
        print(f"O número da lista é: {numero}")


lista_de_numeros = ["1", "5", "9", "4", "2", "7", "8", "6", "3"]

mostrarnumeros(lista_de_numeros)


def inverter_lista(lista):
    lista_invertida = list(reversed(lista))
    return lista_invertida


resultado = inverter_lista(lista_de_numeros)

print(resultado)

