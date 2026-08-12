def definirtriangulo():
    valor1 = float(input("Qual o primeiro valor?"))
    valor2 = float(input("Qual o segundo valor?"))
    valor3 = float(input("Qual o terceiro valor?"))

    if valor1 == valor2 == valor3:
        print("O seu triângulo é equilátero")
    elif valor1 == valor2 or valor2 == valor3 or valor3 == valor1:
        print("O seu triângulo é isósceles")
    else:
        print("O seu triângulo é escaleno")

definirtriangulo()