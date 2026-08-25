def jogo_adivinhacao(numero_secreto):
    while True:
        palpite = int(input("Tente adivinhar o número: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite > numero_secreto:
            print("Seu palpite é maior que o número secreto.")
        else:
            print("Seu palpite é menor que o número secreto.")


numero_secreto = 25
jogo_adivinhacao(numero_secreto)