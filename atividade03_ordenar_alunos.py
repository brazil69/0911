def ordenar_alunos(nomes, dados):
    for limite in range(len(nomes) - 1, 0, -1):
        for i in range(limite):
            if nomes[i].casefold() > nomes[i + 1].casefold():
                nomes[i], nomes[i + 1] = nomes[i + 1], nomes[i]
                dados[i], dados[i + 1] = dados[i + 1], dados[i]
