def aluno_aprovado():
    nota1 = float(input("Qual sua primeira nota?"))
    nota2 = float(input("Qual sua segunda nota?"))

    media = (nota1 + nota2) / 2

    if media >= 6:
        print("Aluno aprovado")
    elif media >= 5 and media < 6:
            print("Aluno reprovado")

aluno_aprovado()

