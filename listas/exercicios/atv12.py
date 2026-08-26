def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A media das notas é {media}")

notas_semestre = [7, 8, 9, 10, 6.5, 7.5, 5, 4]
calcular_media(notas_semestre)
