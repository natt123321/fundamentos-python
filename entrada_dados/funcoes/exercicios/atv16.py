def pesopessoa():
    peso = float(input("Qual seu peso?"))
    return peso

def alturapessoa():
    altura = float(input("Qual sua altura?"))
    return altura

def imcpessoa():
    imc = peso / (altura * altura)
    return imc

peso = pesopessoa()
altura = alturapessoa()
imc = imcpessoa()

print(f"Seu IMC é de {imc}")


