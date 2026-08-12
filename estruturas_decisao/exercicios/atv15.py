def classificaçãodevelocidade():
    velocidade: int = int(input("Qual a velocidade do carro?"))

    if velocidade <= 60:
        print("Velocidade permitida")
    elif velocidade >= 60 and velocidade <= 80:
        print("Atenção: velocidade acima do permitido")
    elif velocidade >= 80:
        print("Multa por excesso de velocidade")

classificaçãodevelocidade()