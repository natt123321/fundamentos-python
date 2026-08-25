def contar_pares(inicio, fim):
    contador = 0
    for inicio in range(inicio, fim):
        if inicio % 2 == 0:
            contador += 1

    return contador

inicio = int(input("Insira o primeiro numero inteiro: "))
fim = int(input("Insira o segundo numero inteiro: "))
quantidade = contar_pares(inicio, fim)
print(f"Quantidade de numeros pares: {quantidade}")

contar_pares(inicio, fim)