def adicionar_cliente(fila, cliente):
    fila.append(cliente)
    print(f"O cliente {cliente} entrou na fila.")


def atender_cliente(fila):
    if len(fila) > 0:
        cliente = fila.pop(0)
        return cliente
    else:
        return None


fila_de_clientes = []

while True:
    cliente = input("Digite o nome do cliente (ou 'sair' para encerrar): ")

    if cliente == "sair":
        break

    adicionar_cliente(fila_de_clientes, cliente)


print(f"\nFila de atendimento: {fila_de_clientes}")

cliente_atendido = atender_cliente(fila_de_clientes)

print(f"O cliente atendido foi: {cliente_atendido}")

print(f"Fila após o atendimento: {fila_de_clientes}")