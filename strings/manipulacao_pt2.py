# Dividir uma string em partes
import urllib


def separar_nome(nome_completo):
    partes =  nome_completo.split()
    return partes

nome_completo = input("Digite um nome: ")
print(f"Nome em partes: {separar_nome(nome_completo)}")

# juntar strings
def criar_nome_completo(partes):
    nome_completo = " ,".join(partes)
    return nome_completo

partes_nome = ["Natalia", "Gamero", "Scognamiglio"]
print(f"A junção das partes do nome é {criar_nome_completo(partes_nome)}")

# verificar o inicio e o final de uma string
def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_br = url.endswith(".br")
    return inicia_com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f"Utiliza https? {tem_https}")
print(f"Termina com .br? {tem_br}")

# verificar se a string contém somente números
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print("O valor digitado é uma idade válida")
    else:
        print("Digite somente números")

idade = input("Digite uma idade: ")
validar_idade(idade)

# verificar se a string contém somentes letras

def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
        print("O nome digitado é válido")
    else:
        print("O nome deve conter apenas letras")

nome = input("Digite um nome: ")
validar_nome(nome)

#verificar se a string contém letras e números
def validar_usuario(usuario):
    usuario_valido = usuario.isalnum()
    if usuario_valido:
        print("Usuário válido")
    else:
        print("Utilize apenas letras e números")

nome_usuario = input("Digite seu nome: ")
validar_usuario(nome_usuario)

#analisando uma frase
def analisar_frase(frase, palavra):
    frase_limpa = frase.strip().lower()

    qtde_caracteres = len(frase_limpa)
    qtde_palavras = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra)

    print(f"Frase completa: {frase_limpa}")
    print(f"Total de caracteres: {qtde_caracteres}")
    print(f"Total de palavras: {qtde_palavras}")
    print(f"Ocorrencias da palavra pesquisada: {ocorrencia_palavra}")

frase_input = input("Digite uma frase: ")
ocorrencia_palavra = input("Digite uma palavra para contar a ocorrencia: ")

analisar_frase(frase_input, ocorrencia_palavra)