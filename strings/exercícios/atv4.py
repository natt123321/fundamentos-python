def limpar_texto(texto):
    texto_limpo = texto.strip()

    # remove espaços da esquerda e da direita
    return texto_limpo


texto_1 = input("Digite um texto (com espaços) : ")

print(f"Texto antes: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")