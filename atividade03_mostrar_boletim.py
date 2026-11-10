from atividade03_calcular_media import calcular_media
from atividade03_definir_situacao import definir_situacao


def mostrar_boletim(nome, dados):
    notas = dados[:2]
    faltas = dados[2]
    media = calcular_media(notas)
    desempenho = "Desempenho em Queda" if notas[0] > notas[1] else "Desempenho em Evolução"

    print(f"\nBoletim de {nome}")
    print(f"Nota 1: {notas[0]:.1f}")
    print(f"Nota 2: {notas[1]:.1f}")
    print(f"Média: {media:.1f}")
    print(f"Faltas: {faltas}")
    print(desempenho)
    print(f"Situação: {definir_situacao(notas, faltas)}")
