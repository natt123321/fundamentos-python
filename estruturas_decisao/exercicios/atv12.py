def acessosenha():
    senha = "python123"

    senha_input = input("Qual sua senha?")

    if senha_input == senha:
        print("Acesso permitido")
    else:
        print("Senha incorreta")

acessosenha()


