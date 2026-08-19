def mostrar_impares():
    numero = int(input("Insira um numero inteiro: "))

    for numero in range(1, numero + 1):
        if numero % 2 != 0: #esse exclamação é q o resultado vai ser quebrado e nao vai dar zero
            print(f"numeros impares {numero}")

mostrar_impares()