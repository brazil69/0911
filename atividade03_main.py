from atividade03_buscar_aluno import buscar_aluno
from atividade03_cadastrar_alunos import cadastrar_alunos
from atividade03_exibir_menu import exibir_menu
from atividade03_listar_alunos import listar_alunos
from atividade03_mostrar_boletim import mostrar_boletim
from atividade03_ordenar_alunos import ordenar_alunos


def main():
    nomes = [""] * 5
    dados = [[0.0, 0.0, 0] for _ in range(5)]

    cadastrar_alunos(nomes, dados)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                listar_alunos(nomes, dados)
            case "2":
                ordenar_alunos(nomes, dados)
                print("\nAlunos ordenados em ordem alfabética.")
                listar_alunos(nomes, dados)
            case "3":
                ordenar_alunos(nomes, dados)
                nome_procurado = input("Digite o nome do aluno: ").strip()
                indice = buscar_aluno(nomes, nome_procurado)
                if indice >= 0:
                    mostrar_boletim(nomes[indice], dados[indice])
                else:
                    print("Aluno não encontrado.")
            case "0":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida. Tente novamente.")
