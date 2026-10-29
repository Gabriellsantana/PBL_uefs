#ARQUIVO IMPORTADO NO ARQUIVO PRINCIPAL main.py

def criar_matriz(tamanho):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(" ")

        matriz.append(linha)

    return matriz


def mostra_matriz(m_matriz):
    tamanho = len(m_matriz)

    # Mostra os números acima  das colunas
    print("   ", end="")
    for coluna in range(1, tamanho + 1):
        print(f"{coluna:5}", end="") # X 3 espaço de difernça x 
             
    print() 
    for i in range(tamanho):
        print(f"{i + 1:2}-> ", end="")

        for j in range(tamanho):
            print(f"[{m_matriz[i][j]:3}]", end="")

        print()


        
