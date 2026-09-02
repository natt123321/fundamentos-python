def analisar_texto(texto, letra):
    qtde_caracteres = len(texto)

    # contar a qtde de ocorrencias

    qtde_letra = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra

texto_2 = input("Digite seu texto: ")
letra = input("Digite uma letra: ")
caracteres, letras = analisar_texto(texto_2, letra)

print(f"Total de caracteres: {caracteres}")
print(f"Total de letras: {letras}")