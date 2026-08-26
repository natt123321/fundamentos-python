def mostrarprodutos(produtos):
    for produto in produtos:
        print(f"O(A) produto da lista é: {produto}")


lista_de_produtos = ["Arroz", "Feijão", "Banana", "Maçã", "Pão", "Bolacha"]

mostrarprodutos(lista_de_produtos)


def remover_produto(produtos, produto):
    if produto not in produtos:
        print("Este produto não existe na lista")
    else:
        produtos.remove(produto)
        print(f"O produto {produto} foi removido da lista {produtos}")


remover_produto(lista_de_produtos, produto="Pão")


def remover_produto_pelo_indice(produtos, posicao):
    produto = produtos[posicao]
    produtos.pop(posicao)
    print(f"O produto da posicao {posicao}, é {produto} foi removido!")


remover_produto_pelo_indice(lista_de_produtos, posicao=4)