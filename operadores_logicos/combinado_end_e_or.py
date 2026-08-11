# Operadores and e or

def posso_entrar_no_show():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade?"))
    nome_esta_na_lista = bool(input("Seu nome tá na lista?"))

    posso_entrar = (nome_esta_na_lista or POSSUI_INGRESSO) and idade >= 18

    print(f"Vou conseguir entrar? {posso_entrar}")

posso_entrar_no_show()
