def contagempersonalizada():
    inicio = int(input("Insira o numero inicial: "))
    fim = int(input("Insira o numero final: "))

    for numero in range (inicio, fim + 1): #o +1 no final é pra colocar o numero final
        print(numero)

contagempersonalizada()