def buscar_aluno(nomes, nome_procurado):
    inicio = 0
    fim = len(nomes) - 1
    procurado = nome_procurado.casefold()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = nomes[meio].casefold()

        if nome_meio == procurado:
            return meio
        if nome_meio < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
