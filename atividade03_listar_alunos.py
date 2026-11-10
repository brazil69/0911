from atividade03_mostrar_boletim import mostrar_boletim


def listar_alunos(nomes, dados):
    print("\n--- Lista de alunos ---")
    for i in range(len(nomes)):
        mostrar_boletim(nomes[i], dados[i])
