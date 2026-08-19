def somar_ate(numero):
    soma = 0
    for i in range (1, numero + 1):
        soma = soma + i

    return soma

numero = int(input("Insira um numero inteiro: "))
resultado = somar_ate(numero)

print(resultado)


somar_ate(numero)