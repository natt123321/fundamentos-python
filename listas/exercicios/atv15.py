def mostrar_notas(notas):
    for nota in notas:
        print(f"A nota da lista é: {nota}")


lista_de_notas = [9.5, 8, 7, 5, 7.5, 6]
mostrar_notas(lista_de_notas)

def adicionar_notas(notas, nota):
    notas.append(nota)
    print(notas)

adicionar_notas(lista_de_notas, nota = 6.5)

def remover_nota(notas, nota):
    if nota not in notas:
        print("Esta nota não existe na lista")
    else:
        notas.remove(nota)
        print(f"A nota {nota} foi removido na lista {notas}")

remover_nota(lista_de_notas, nota = "5")


def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A media das notas é {media}")

notas_semestre = [9.5, 8, 7, 5, 7.5, 6]
calcular_media(notas_semestre)