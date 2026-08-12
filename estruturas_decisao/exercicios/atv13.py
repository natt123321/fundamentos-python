def precoingresso():
    idade: int = int(input("Qual sua idade?"))

    if idade <= 5:
        print("O ingresso será gratuito ^_^")
    elif idade >= 6 and idade <= 12:
        print("O ingresso será de R$ 10,00")
    elif idade >= 13 and idade <= 59:
        print("O ingresso será de R$ 20,00")
    elif idade >= 60:
        print("O ingresso será de R$ 10,00")

precoingresso()