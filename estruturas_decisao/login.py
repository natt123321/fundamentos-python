def login():
    email = "nataliascogna@gmail.com"
    senha = "1234"

    email_input = input("Qual seu email?")
    senha_input = input("Qual sua senha?")
    codigo_secreto = "1234567890"

    if email_input == email and senha_input == senha:
        print("Usuario logado :)")
        admin = input("Deseja acessar a area admin? S/N")
        if admin == "S":
            codigo_secreto_input = input("Qual o codigo admin?")
            if codigo_secreto_input == codigo_secreto:
                print("Acesso liberado :)")

            else:
                print("Codigo incorreto :/")

        elif admin == "N":
            print("Logado como usuario comum")

        else:
            print("Opção invalida")

    else:
        print("Email ou senha incorreto")

login()