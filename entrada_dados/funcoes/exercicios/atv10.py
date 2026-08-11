def temperaturaemcelsius():
    celsius = float(input("Qual a temperatura em celsius? "))
    return celsius

def temperaturaemfahrenheit():
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

celsius = temperaturaemcelsius()
fahrenheit = temperaturaemfahrenheit()

print(f"A temperatura em fahrenheit é {fahrenheit}")