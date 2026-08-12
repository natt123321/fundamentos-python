def temperaturacelsius():
    temperatura: int = int(input("Qual a temperatura?"))

    if temperatura < 15:
        print("Nossa, que frio é esse?")
    elif temperatura > 15 and temperatura <= 20:
        print("Hmmm até que está agradável")
    elif temperatura > 25:
        print("Eita, que calor!")

temperaturacelsius()