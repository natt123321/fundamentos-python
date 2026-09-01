def vender_produto(produto):
    estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

    if produto in estoque:
        estoque.remove(produto)
    else:
        print(f"O produto {produto} não está disponível.")

    return estoque


print(vender_produto("Mouse"))