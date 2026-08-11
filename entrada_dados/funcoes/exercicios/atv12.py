def precoproduto():
    produto = float(input("Qual o valor do produto? "))
    return produto

def percentualdesconto():
    desconto = 3 / 100
    return desconto

def produtocomdesconto ():
    produtodesconto = produto * desconto
    return produtodesconto

produto = precoproduto()
desconto = percentualdesconto()
produtodesconto = produtocomdesconto()

print(f"O valor do seu produto com desconto é {produtodesconto}")