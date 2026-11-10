from atividade03_ler_nota import ler_nota


def cadastrar_alunos(nomes, dados):
    print("\n--- Cadastro dos alunos ---")
    for i in range(len(nomes)):
        print(f"\nAluno {i + 1}")
        nomes[i] = input("Nome: ").strip()
        while not nomes[i]:
            print("O nome não pode ficar vazio.")
            nomes[i] = input("Nome: ").strip()

        dados[i][0] = ler_nota(1)
        dados[i][1] = ler_nota(2)

        while True:
            try:
                faltas = int(input("Total de faltas: "))
                if faltas >= 0:
                    dados[i][2] = faltas
                    break
                print("O total de faltas não pode ser negativo.")
            except ValueError:
                print("Digite um número inteiro válido.")
