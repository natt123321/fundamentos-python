def saldodisponivel():
    saldo = float(input("Qual seu saldo?"))
    sacada = float(input("Qual valor deseja sacar?"))

    if sacada > saldo:
        print("Saldo insuficiente :(")
    elif sacada <= 0:
        print("Valor inválido :/")
    else:
        print("Sacada realizada com sucesso! :)")
        novosaldo = saldo - sacada
        print(f"Seu novo saldo é {novosaldo}")

saldodisponivel()
