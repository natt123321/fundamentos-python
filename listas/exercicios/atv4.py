def mostrarprodutos(produtos):
    for produto in produtos:
        print(f"O(A) convidado(a) da lista é: {produto}")


lista_de_produtos = ["Arroz", "Feijão", "Banana", "Maçã", "Pão", "Bolacha"]
mostrarprodutos(lista_de_produtos)

def remover_produto(produtos, produto):
    if produto not in produtos:
        print("Este nome não existe na lista")
    else:
        produtos.remove(produto)
        print(f"O nome {produto} foi removido na lista {produtos}")

remover_produto(lista_de_produtos, produto ="Pão")