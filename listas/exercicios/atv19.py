notas = [7.5, 6.0, 8.5, 9.0, 5.5]


# 1. Adicionar uma nota
def adicionar_nota(notas, nota):
    notas.append(nota)
    return notas


# 2. Inserir uma nota em uma posição
def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)
    return notas


# 3. Adicionar várias notas
def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)
    return notas


# 4. Remover uma nota
def remover_nota(notas, nota):
    notas.remove(nota)
    return notas


# 5. Remover a última nota
def remover_ultima_nota(notas):
    return notas.pop()


# 6. Encontrar a posição de uma nota
def encontrar_nota(notas, nota):
    return notas.index(nota)


# 7. Informar a quantidade de notas
def quantidade_notas(notas):
    return len(notas)


# 8. Ordenar as notas
def ordenar_notas(notas):
    return sorted(notas)


# 9. Mostrar as notas em ordem inversa
def notas_inversas(notas):
    return list(reversed(notas))


# 10. Calcular a soma das notas
def somar_notas(notas):
    return sum(notas)


# 11. Calcular a média da turma
def calcular_media(notas):
    return sum(notas) / len(notas)


print("1. Adicionar nota:", adicionar_nota(notas, 10))
print("2. Inserir nota:", inserir_nota(notas, 8.0, 1))
print("3. Adicionar várias notas:", adicionar_varias_notas(notas, [7.0, 9.5]))
print("4. Remover nota:", remover_nota(notas, 6.0))
print("5. Remover última nota:", remover_ultima_nota(notas))
print("6. Posição da nota:", encontrar_nota(notas, 8.5))
print("7. Quantidade de notas:", quantidade_notas(notas))
print("8. Notas ordenadas:", ordenar_notas(notas))
print("9. Notas inversas:", notas_inversas(notas))
print("10. Soma das notas:", somar_notas(notas))
print("11. Média da turma:", calcular_media(notas))