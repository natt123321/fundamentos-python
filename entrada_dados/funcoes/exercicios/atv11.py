def valorhoratrabalhada():
    valor = float(input("Qual o valor da hora trabalhada? "))
    return valor

def qtdehoratrabalhada():
    horas = float(input("Quantas horas você trabalhou? "))
    return horas

def valorsalario():
    salario = valor * horas
    return salario

valor = valorhoratrabalhada()
horas = qtdehoratrabalhada()
salario = valorsalario()

print(f"O seu salário é {salario}")