def compra():
    valor = float(input("Qual o valor da compra?"))

    if valor <= 100:
        print("Não terá desconto, poxa :(")

    elif valor >= 101 and valor <= 500:
        print("O desconto é de 10% :)")
        desconto = valor * 0.1
        print(f"O valor com desconto ficou de {desconto}")

    elif valor >= 500:
        print("O desconto é de 15% :)")
        desconto = valor * 0.15
        print(f"O valor com desconto ficou de {desconto}")

compra()