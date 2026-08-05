def numerointeiro():
    numero = int(input("Qual numero voce quer? "))

    return numero

def ant():
    antecessor = numero - 1
    return antecessor

def suc():
    sucessor = numero + 1
    return sucessor

numero = numerointeiro()
antecessor = ant()
sucessor = suc()
print(f"O antecessor do seu numero é {antecessor} e o sucessor é {sucessor}")
