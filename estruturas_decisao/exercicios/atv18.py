def calculadorafrete():
    valor: int = int(input("Qual o valor da compra?"))

    if valor <= 100:
        print("O frete será de R$ 20,00")
        frete = valor + 20
        print(f"O valor final ficou de R$ {frete}")
    elif valor >= 101 and valor <= 300:
        print("O frete será de R$ 10,00")
        frete = valor + 10
        print(f"O valor final ficou de R$ {frete}")
    elif valor >= 300:
        print("O frete será grátis :)")

calculadorafrete()