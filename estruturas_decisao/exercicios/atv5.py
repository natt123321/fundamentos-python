def notaaluno():
    nota: int = int(input("Qual sua nota?"))

    if nota >= 0 and nota <= 4:
        print("Poxa, que pena que você foi mal :( mas você consegue melhorar!")
    elif nota == 5 or nota == 6:
        print("Foi um resultado regular, mas não se entristeça!")
    elif nota == 7 or nota == 8:
        print("Parabéns! Foi uma nota boa :)")
    elif nota == 9 or nota == 10:
        print("Parabéns, foi uma nota excelente! Você devia se orgulhar ^_^")

notaaluno()