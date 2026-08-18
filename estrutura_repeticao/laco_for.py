# Laço for simples
import time

def mostrarnumero():
    for i in range(1,6):
        print(f"O número atual é {i}")
        time.sleep(5)

mostrarnumero()

def mostrarnumeroalternado():
    for num in range(0, 20, 2):
        print(f"O número atual é {num}")

mostrarnumeroalternado()

def somarnumeros():
    total = 0
    for valor in range(1, 20):
        total += valor
    print(total)

somarnumeros()

def mostrarnumerospares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f"numeros pares {numero}")

mostrarnumerospares()

def sacoladefrutas():
    frutas = ["Maçã", "Morango", "Jabuticaba", "Blueberry", "Limão", "Pêssego"]
    for fruta in frutas:
        print(f"Na minha sacola contém {frutas}")


sacoladefrutas()

def lacoaninhado():
    nomes = ["Natalia", "Carlos", "Lorena", "Mariana", "Nicolas", "Yasminn", "Yasmin"]
    notas = [8, 9, 10]
    for nome in nomes:
        print(f"Nome do aluno {nome}")
        for nota in notas:
            print(f"Nota do aluno {nota}")

lacoaninhado()


