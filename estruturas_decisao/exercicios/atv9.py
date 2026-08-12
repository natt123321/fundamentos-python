def calculadora():
    numero1: int = int(input("Qual o primeiro numero?"))
    numero2: int = int(input("Qual o segundo numero?"))
    operação = input("Qual operação deseja fazer? +, -, * ou /?")

    if operação == "*":
        multiplicação = numero1 * numero2
        print(f"O resultado é {multiplicação}")

    elif operação == "/":
        divisão = numero1 / numero2
        print(f"O resultado é {divisão}")

    elif operação == "+":
        adição = numero1 + numero2
        print(f"O resultado é {adição}")

    elif operação == "-":
        subtração = numero1 - numero2
        print(f"O resultado é {subtração}")

calculadora()