def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


numero = int(input("Digite um número: "))

print(eh_primo(numero))

eh_primo(numero)