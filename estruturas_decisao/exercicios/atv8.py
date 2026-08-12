def faixaetaria():
    idade: int = int(input("Qual sua idade?"))

    if idade >= 0 and idade <= 12:
        print("Você é uma criança, que bonitinha! :3")
    elif idade >= 13 and idade <= 17:
        print("Você é um adolescente, aproveite bem!")
    elif idade >= 18 and idade <= 59:
        print("Você é um adulto, tire um tempo pra descansar depois de tanto trabalhar")
    elif idade >= 60:
        print("Você é um idoso, descanse bastante!")

faixaetaria()