# Operador and

def podedirigir():
    idade = int(input("Digite sua idade: "))
    TEM_HABILITACAO= True

    autorizado = idade >= 18 and TEM_HABILITACAO

    print(f"Usuário pode dirigir?{autorizado}")

idade = podedirigir()