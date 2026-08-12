def numeros():
    numero1 = int(input("Qual o primeiro numero?"))
    numero2 = int(input("Qual o segundo numero?"))

    if numero1 > numero2:
        print("O primeiro número é maior")
    elif numero1 < numero2:
        print("O segundo número é maior")
    else:
        print("Os dois números são iguais")

numeros()