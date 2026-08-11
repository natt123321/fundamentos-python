def nomepessoa():
    nome = input("Qual seu nome?")
    return nome

def idadepessoa():
    idade = input("Qual sua idade?")
    return idade

def profissãopessoa():
    profissão = input("Qual sua profissão?")
    return profissão

def cidadepessoa():
    cidade = input("Qual cidade você mora?")
    return cidade

nome = nomepessoa()
idade = idadepessoa()
profissão = profissãopessoa()
cidade = cidadepessoa()

print("======= CADASTRO =======")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Profissão: {profissão}")
print(f"Cidade: {cidade}")
print("========================")