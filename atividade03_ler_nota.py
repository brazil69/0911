def ler_nota(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a Nota {numero_nota} (0 a 10): ").replace(",", "."))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um valor numérico válido.")
