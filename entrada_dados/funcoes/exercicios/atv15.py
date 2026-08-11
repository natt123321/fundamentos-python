def idadeemanos():
    idade = int(input("Qual sua idade? "))
    return idade

def idadeemmeses():
    idademeses = idade * 12
    return idademeses

def idadeemdias():
    idadedias = idade * 365
    return idadedias

idade = idadeemanos()
idademeses = idadeemmeses()
idadedias = idadeemdias()

print(f"Sua idade normal é {idade} anos, em meses é {idademeses} e em dias é {idadedias}")