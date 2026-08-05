def baseretangulo():
    base = float(input("Qual a base do retangulo? "))
    return base

def alturaretangulo():
    altura = float(input("Qual a altura do retangulo? "))
    return altura

def arearetangulo():
    area = base * altura
    return area

base = baseretangulo()
altura = alturaretangulo()
area = arearetangulo()

print(f"A area do seu retangulo é {area}")