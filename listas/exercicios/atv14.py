def mostrarprodutos(produtos):
    for produto in produtos:
        print(f"O(A) produto da lista é: {produto}")


lista_de_produtos = ["Arroz", "Feijão", "Banana", "Maçã", "Pão", "Bolacha"]

mostrarprodutos(lista_de_produtos)

def adicionar_produtos(produtos, novos_produtos):
    produtos.extend(novos_produtos)
    print(f"Os novos produtos {novos_produtos} foram inseridos na lista {produtos}")

novos_produtos = ["Salgadinho", "Macarrão", "Batata", "Lasanha"]
adicionar_produtos(lista_de_produtos, novos_produtos)

def remover_produto(produtos, produto):
    if produto not in produtos:
        print("Este produto não existe na lista")
    else:
        produtos.remove(produto)
        print(f"O produto {produto} foi removido na lista {produtos}")

remover_produto(lista_de_produtos, produto = "Banana")