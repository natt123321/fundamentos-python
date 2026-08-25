def somar_pares(inicio, fim):
    soma = 0

    for numero in range(inicio, fim):
        if numero % 2 == 0:
            soma += numero

    return soma


inicio = int(input("Insira o primeiro número inteiro: "))
fim = int(input("Insira o segundo número inteiro: "))

resultado = somar_pares(inicio, fim)
print(f"A soma dos números pares é: {resultado}")

somar_pares(inicio, fim)