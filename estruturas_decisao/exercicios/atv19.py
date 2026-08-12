def numerointeiro():
    numero = int(input("Qual seu numero?"))

    if numero > 0:
        print("Seu numero é positivo")
        resultadosinal = "positivo"
    elif numero == 0:
        print("Seu numero é igual a zero")
        resultadosinal = "zero"
    elif numero < 0:
        print("Seu numero é negativo")
        resultadosinal = "negativo"

        if numero % 2 == 0:
            print("Seu numero é par")
            resultadoparidade = "par"
        else:
            print("Seu numero é ímpar")
            resultadoparidade = "ímpar"

            print(f"Número: {numero}")
            print(f"Classificação: {resultadoparidade} e {resultadosinal}")

numerointeiro()