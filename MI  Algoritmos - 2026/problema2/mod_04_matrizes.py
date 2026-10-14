def criar_matriz(tamanho):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(0)

        matriz.append(linha)

    return matriz


def mostra_matriz(m_matriz):
    tamanho = len(m_matriz)

    # Mostra os números das colunas
    print("   ", end="")
    for coluna in range(1, tamanho + 1):
        print(f"{coluna:3}", end="") # X 3 espaço de difernça x 
        
    print() 
    print()
    # Mostra o número da linha e seus valores
    for i in range(tamanho):
        print(f"{i + 1:2}->", end="")

        for j in range(tamanho):
            print(f"{m_matriz[i][j]:3}", end="")

        print()
