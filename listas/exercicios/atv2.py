def inserir_aluno(alunos):
    for aluno in alunos:
        print(f"O nome na lista é: {aluno}")


lista_de_alunos = ["Maria", "Caio", "Laís", "Jonatas", "Gabriel", "Luana"]
inserir_aluno(lista_de_alunos)

def adicionar_aluno_posicao(alunos, aluno, posicao):
    alunos.insert(posicao, aluno)
    print(f"O nome {aluno} foi inserido na posicao {posicao} da lista {alunos}")

adicionar_aluno_posicao(lista_de_alunos, aluno = "Nayara", posicao = 4)
