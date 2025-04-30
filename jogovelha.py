def inicializar_tabuleiro():
    return [" " for _ in range(9)]

def mostrar_tabuleiro(tabuleiro):
    print()
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()

def verificar_vitoria(tabuleiro, jogador):
    # Combinações de vitória
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    for combo in combinacoes:
        if all(tabuleiro[pos] == jogador for pos in combo):
            return True
    return False

def verificar_empate(tabuleiro):
    return " " not in tabuleiro

def jogar():
    tabuleiro = inicializar_tabuleiro()
    jogador_atual = "X"

    while True:
        mostrar_tabuleiro(tabuleiro)
        try:
            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[posicao] != " " or posicao not in range(9):
                print("Posição inválida! Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Digite um número entre 1 e 9.")
            continue

        tabuleiro[posicao] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar()