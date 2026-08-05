def exibir_mensagem():
    print("Hello World!! ^_^")


def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2
    print(f"O total da soma é {total}")

def calcularmedia():
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    total = (nota1 + nota2) / 2
    return total

exibir_mensagem()
somar()

nota_final = calcularmedia()
print(f"A nota final é {nota_final}")