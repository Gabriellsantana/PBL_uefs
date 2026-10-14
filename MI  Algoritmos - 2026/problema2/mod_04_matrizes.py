def criar_matriz(tamanho):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(0)

        matriz.append(linha)

    return matriz