def distanciapercorrida():
    distancia = float(input("Qual a distancia percorrida? "))
    return distancia

def qtdecombustivel():
    combustivel = float(input("Qual o valor ddo combustivel? "))
    return combustivel

def consumomedio():
    consumo = distancia / combustivel
    return consumo

distancia = distanciapercorrida()
combustivel = qtdecombustivel()
consumo = consumomedio()

print(f"O seu consumo médio é de {consumo} KM/L")