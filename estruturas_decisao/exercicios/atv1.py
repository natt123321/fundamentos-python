def numerointeiro():
    numero = int(input("Qual seu numero?"))

    if numero > 0:
        print("Seu numero é positivo")
    elif numero == 0:
        print("Seu numero é igual a zero")
    elif numero < 0:
        print("Seu numero é negativo")

numerointeiro()