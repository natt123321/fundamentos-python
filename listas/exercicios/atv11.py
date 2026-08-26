def mostrarnumeros(numeros):
    for numero in numeros:
        print(f"O número da lista é: {numero}")


lista_de_numeros = [1, 5, 9, 4, 2, 7, 8, 6, 3]

mostrarnumeros(lista_de_numeros)


def somar_numeros(numeros):
    soma = sum(numeros)
    return soma


resultado = somar_numeros(lista_de_numeros)

print(f"A soma dos números é: {resultado}")