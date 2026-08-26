def mostrarprodutos(produtos):
    for produto in produtos:
        print(f"O(A) produto da lista é: {produto}")


lista_de_produtos = ["Arroz", "Feijão", "Banana", "Maçã", "Pão", "Bolacha"]

mostrarprodutos(lista_de_produtos)

def encontrar_posicao_pelo_produto(produtos, produto):
    if produto not in produtos:
        print("Produto não encontrado")
    else:
        posicao = produtos.index(produto)
        print(f"A posicao do nome {produto} é {posicao}")

encontrar_posicao_pelo_produto(lista_de_produtos, produto = "Banana")