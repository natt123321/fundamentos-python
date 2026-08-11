def numeros():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    return A, B


def antes(A, B):
    print("Antes:")
    print(f"A = {A}")
    print(f"B = {B}")


def troca(A, B):
    A, B = B, A

    return A, B


def depois(A, B):
    print("Depois:")
    print(f"A = {A}")
    print(f"B = {B}")


A, B = numeros()

antes(A, B)

A, B = troca(A, B)

depois(A, B)