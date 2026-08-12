def loginsimples():
    senha = "1234"
    usuario = "admin"

    usuario_input = input("Qual o usuario?")
    senha_input = input("Qual sua senha?")


    if usuario_input == usuario and senha_input == senha:
        print("Login realizado com sucesso")
    elif usuario_input == usuario:
        print("Senha incorreta")
    else:
        print("Usuário não encontrado")


loginsimples()