def mostrar_multiplos(numero):
    for i in range (1, 11):
        resultado = numero * i
        print(resultado)

numero = int(input("Digite um número: "))
mostrar_multiplos(numero)