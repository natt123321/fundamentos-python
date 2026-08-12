def calculoimc():
    peso = float(input("Qual o seu peso?"))
    altura = float(input("Qual a sua altura?"))

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Você está abaixo do peso")

    elif imc >= 18.5 and imc <= 24.9:
        print("Seu peso está regular")

    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")

    elif imc >= 30:
        print("Obesidade")

calculoimc()