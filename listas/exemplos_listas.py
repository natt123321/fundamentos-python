def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Natalia", "Carlos", "Lorena", "Mariana", "Nicolas", "Yasminn"]
mostrar_nomes(lista_de_nomes)

# adicionando um novo nome no final da lista

def adicionar_nomes(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nomes(lista_de_nomes, nome = "Yasmin")

# adicionando novo nome em uma posição especifica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posicao {posicao} da lista {nomes}")

adicionar_nome_posicao(lista_de_nomes, nome = "Nayara", posicao = 4)

# juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")

novos_nomes = ["Torajo", "Morajo", "Zulmi", "Linn", "Azedo", "Pessy", "Jay", "Margo"]
juntar_nomes(lista_de_nomes, novos_nomes)

# removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido na lista {nomes}")

remover_nome_pelo_valor(lista_de_nomes, nome = "Nayara")

# removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posicao {posicao}, é {nomes[posicao]} foi removido!")

remover_nome_pelo_indice(lista_de_nomes, posicao = 4)

# descobrindo a posicao (index) pelo nome
def encontrar_posicao_pelo_nome(nomes, nome):
    if nome not in nomes:
        print("Nome não encontrado")
    else:
        posicao = nomes.index(nome)
        print(f"A posicao do nome {nome} é {posicao}")

encontrar_posicao_pelo_nome(lista_de_nomes, nome = "Carlos")

# contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

ordenar_nomes(lista_de_nomes)

# operações matematicas
# calcular media

def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A media das notas é {media}")

notas_semestre = [7, 8, 9, 10, 6.5, 7.5, 5, 4]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    notas_ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return notas_ordenadas, media

notas_ordenadas, media = gerenciar_notas(notas_semestre, nova_nota = 3.5)
print(f"Notas ordenadas = {notas_ordenadas}")
print(f"A media das notas é de {media}")

# Lista de listas
def adicionar_produto(produtos, produto):
    produto.append(produto)
    print(f"Minha lista de produtos: {produtos[0][0]}")

lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50]
]
novo_produto = ["Coca-cola", 2, 8.00]
adicionar_produto(lista_produtos, novo_produto)

def quantidade_total_produtos(produtos):
    quantidade = []
    for produto in produtos:
        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"A quantidade total de produtos é {quantidade_produtos}")

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

        return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f"O valor total dos produtos é {preco_total_produtos}")