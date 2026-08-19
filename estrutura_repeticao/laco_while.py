def mostrarnumerowhile():
    contador = 0
    while contador <= 10:
        contador += 1
        print(f"Contagem atual: {contador}")

# mostrarnumerowhile()

def contagem_regressiva():
    valor_contagem = int(input("Digite um número maior que 10: "))
    if valor_contagem < 10:
        print("Valor inválido :/")
    else:
        while valor_contagem >= 1:
            print(f"Contagem regressiva: {valor_contagem}")
            valor_contagem -= 1
        print("Decolando!!!!!!!!!!!!")

#contagem_regressiva()

def soma_com_while():
    while True:
        num_1 = int(input("Digite o primeiro número:"))
        num_2 = int(input("Digite o segundo número:"))

        if num_1 == 0:
            break
        else:
            soma = num_1 + num_2
            print(f"O resultado do soma é: {soma}")

        soma = num_1 + num_2
        print(f"O resultado da soma é {soma}")

soma_com_while()
