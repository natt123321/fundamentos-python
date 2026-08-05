def calcularmedia():
    nota1 = float(input("Qual a primeira nota? "))
    nota2 = float(input("Qual a segunda nota? "))
    nota3 = float(input("Qual a terceira nota? "))
    total = (nota1 + nota2 + nota3) / 3
    return total

nota_final = calcularmedia()
print(f"A nota final é {nota_final}")