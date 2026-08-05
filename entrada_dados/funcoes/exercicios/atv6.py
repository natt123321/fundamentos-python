def numerointeiro():
    numero = int(input("Qual numero voce quer? "))

    return numero

def vezesdois():
    dobro = numero * 2
    return dobro

def vezestres():
    triplo = numero * 3
    return triplo

numero = numerointeiro()
dobro = vezesdois()
triplo = vezestres()
print(f"O dobro do seu numero é {dobro} e o triplo é {triplo}")