def baseretangulo():
    base = float(input("Qual a base do retangulo? "))
    return base

def alturaretangulo():
    altura = float(input("Qual a altura do retangulo? "))
    return altura

def perimetroretangulo():
    perimetro = 2 * (base + altura)
    return perimetro

base = baseretangulo()
altura = alturaretangulo()
perimetro = perimetroretangulo()

print(f"A area do seu retangulo é {perimetro}")