from atividade03_calcular_media import calcular_media


def definir_situacao(notas, faltas):
    if faltas > 20:
        return "Reprovado por Faltas"

    media = calcular_media(notas)
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado por Nota"
