def numeroemmetros():
    numerometro = float(input("Qual seu numero em metros? "))
    return numerometro

def numeroemcentimetros():
    numerocentimetro = numerometro * 100
    return numerocentimetro

numerometro = numeroemmetros()
numerocentimetro = numeroemcentimetros()

print(f"O seu numero em centímetros é {numerocentimetro}")
