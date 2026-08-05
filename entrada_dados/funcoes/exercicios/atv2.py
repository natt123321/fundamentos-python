def saudacao():
    nome = input("Qual seu nome? ")
    print(f"Seja bem-vindo, {nome}!")

    return nome

def ano():
    idade = input("Qual sua idade? ")
    print(f"Voce tem {idade} anos, certo")

    return idade

nome = saudacao()
idade = ano()
print(f"{nome} possui {idade} anos")
