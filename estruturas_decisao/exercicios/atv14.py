def sistemavotação():
    idade: int = int(input("Qual sua idade?"))

    if idade < 16:
        print("Não pode votar")
    elif idade == 16 or idade == 17:
        print("Voto opcional")
    elif idade >= 18 and idade <= 69:
        print("Voto obrigatório")
    elif idade >= 70:
        print("Voto opcional")

sistemavotação()