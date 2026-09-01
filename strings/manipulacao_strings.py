# Converter texto para maiúsculas e minúsculas

def formatar_nome(nome):
    # nome em maiusculo
    nome_maiusculo = nome.upper()

    # nome em minusculo
    nome_minusculo = nome.lower()

    # nome com primeira letra maiuscula
    nome_camel_case = nome.capitalize()
    return (nome_maiusculo, nome_minusculo, nome_camel_case)


nome = input("Digite seu nome: ")

 # print(formatar_nome(nome)[0])

nome_maiusculo, nome_minusculo, nome_camel_case = formatar_nome(nome)
print(f"Nome maiúsculo: {nome_maiusculo}")
print(f"Nome minusculo: {nome_minusculo}")
print(f"Nome camel case: {nome_camel_case}")

# remover espaços desnecessarios

def limpar_texto(texto):
    texto_limpo = texto.strip()

    # remove espaços da esquerda .lstrip
    # remove espaços da direita  .rstrip
    return texto_limpo

texto_1 = "   Aprendendo Python    "
print(f"Texto antes: {texto_1}")
print(f"Texto depois: {limpar_texto(texto_1)}")

# substituir palavras
def trocar_cidade(texto):
    texto_trocado = texto.replace("São Paulo", "Piracicaba")
    return texto_trocado

cidade = "Eu moro em São Paulo"
print(trocar_cidade(cidade))

# contar caracteres ou ocorrencias

def analisar_texto(texto, letra):
    qtde_caracteres = len(texto)

    # contar a qtde de ocorrencias

    qtde_letra = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra

texto_2 = input("Digite seu texto: ")
letra = input("Digite uma letra: ")
caracteres, letras = analisar_texto(texto_2, letra)

print(f"Total de caracteres: {caracteres}")
print(f"Total de letras_a: {letras}")

# verificar se uma palavra esta presente
def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    # retorna um booleano (true ou false)
    return palavra_presente

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"A palavra está presente na frase? {verificar_palavra(frase, palavra)}")

# encontre a posição de uma palavra

def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase_2 = input("Digite uma nova frase: ")
palavra_2 = input("Digite uma palavra para saber sua posicao: ")

print(f"A posição da palavra é {encontrar_posicao_palavra(frase_2, palavra_2)}")