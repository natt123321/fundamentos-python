def mostrar_pares():
    numero = int(input("Insira um numero inteiro: "))

    for numero in range(1, numero + 1):
        if numero % 2 == 0:
            print(f"numeros pares {numero}")

mostrar_pares()