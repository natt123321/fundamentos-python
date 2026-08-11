# Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("Você tem dinheiro para comprar?"))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Posso gastar?{autorizado}")

posso_comprar()