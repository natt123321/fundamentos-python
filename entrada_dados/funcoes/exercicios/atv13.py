def salariofixo():
    salario = float(input("Qual o valor do seu salário? "))
    return salario

def valordasvendas():
    valorvenda = float(input("Qual o valor das suas vendas? "))
    return valorvenda

def percentualdecomissão():
    percentualcomissão = float(input("Qual o valor de comissão? "))
    return percentualcomissão

def vendacomcomissão():
    vendacomissão = valorvenda * (percentualcomissão / 100)
    return vendacomissão

def salariofinal():
    final = salario + vendacomissão
    return final

salario = salariofixo()
valorvenda = valordasvendas()
percentualcomissão = percentualdecomissão()
vendacomissão = vendacomcomissão()
final = salariofinal()

print(f"Seu salario fixo é {final}")
