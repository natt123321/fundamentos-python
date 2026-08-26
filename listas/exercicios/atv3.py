def primeirosconvidados(convidados):
    for convidado in convidados:
        print(f"O(A) convidado(a) da lista é: {convidado}")


lista_de_convidados = ["Maria", "Caio", "Laís", "Jonatas", "Gabriel", "Luana"]
primeirosconvidados(lista_de_convidados)

def adicionarconvidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(f"Os novos convidados {novos_convidados} foram inseridos na lista {convidados}")

novos_convidados = ["Thaís", "Mariana", "Laura", "Lucas"]
adicionarconvidados(lista_de_convidados, novos_convidados)