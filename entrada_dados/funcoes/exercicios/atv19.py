def consumoemKWH():
    consumo = float(input("Qual o consumo em KWH?"))
    return consumo

def preçodoKWH():
    preço = float(input("Qual o valor do KWH?"))
    return preço

def valordaconta():
    valor = consumo * preço
    return valor

consumo = consumoemKWH()
preço = preçodoKWH()
valor = valordaconta()

print(f"O valor da conta é de R$ {valor}")