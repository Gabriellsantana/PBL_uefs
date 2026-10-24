import random 
import mod_04_matrizes  

# algumas partes especifica do código desse arquivos esta comentada que envolvam metodos usados da bibliotca random é  para raciocinio logico claro 


def validando_posicao_escolhida(matriz,linha,coluna,tamanho_peca,orientacao):

    tamanhoMatriz = len(matriz)
    if orientacao ==  "H":
       if coluna + tamanho_peca > tamanhoMatriz:
           return False #passou a borda
    elif orientacao == "V":
        if linha + tamanho_peca > tamanhoMatriz:
            return False #passou a borda

    # verifica sobre posição >ESPAÇOS OCUPADOS<
    for i in range(tamanho_peca):
        if orientacao == "H":
            # Olha para as próximas casas na mesma linha
            if matriz[linha][coluna + i] != " ":
                return False # Já existe uma peça aqui
                
        elif orientacao == "V":
            # Olha para as próximas casas na mesma coluna
            if matriz[linha + i][coluna] != " ": 
                return False # Já existe uma peça aqui
    return True

def posicionar_pecas_jogador(matriz_real_jogador, tamanho):
    if tamanho == 6:
        pecas = [["Armadura", 3, "A1"], ["Capa", 2, "C1"], ["Capa", 2, "C2"], ["Elmo", 1, "E1"], ["Elmo", 1, "E2"]]
    elif tamanho == 8:
        pecas = [["Par de Asas", 4, "AS1"], ["Armadura", 3, "A1"], ["Capa", 2, "C1"], ["Capa", 2, "C2"], ["Elmo", 1, "E1"], ["Elmo", 1, "E2"]]
    elif tamanho == 10:
        pecas = [["Par de Asas", 4, "AS1"], ["Armadura", 3, "A1"], ["Armadura", 3, "A2"], ["Capa", 2, "C1"], ["Capa", 2, "C2"], ["Capa", 2, "C3"], ["Elmo", 1, "E1"], ["Elmo", 1, "E2"], ["Elmo", 1, "E3"], ["Elmo", 1, "E4"]]

    print("\n[1]posicionar Manualmente [2]espalhar automaticamente: ")
    escolha = input("Opção: ").strip()

    if escolha == "2":
        print("Opção automática em breve!")
        return

    for peca in pecas:
        nome_peca = peca[0]
        tamanho_peca = peca[1]
        sigla_peca = peca[2]
        
        while True:
            # 1. MOSTRA A MATRIZ ATUALIZADA PARA O JOGADOR VER
            print("\nDica: Primeiro escolha posição incial da peça depois o setindo que ela ficara")
            print("Ex: Casa (1,1) em 'H' ocupará as casas [(1,1),(1,2) e (1,3)] peça inciou na 1,1 e cresceu para direta [x]>+[x]>+[x]")
            print("[H] para horizontal cresce para a DIREITA [V]  para vertical cresce para BAIXO\n")

            print(f"\n--- POSICIONANDO: {nome_peca} ({tamanho_peca} casas) ---")
            mod_04_matrizes.mostra_matriz(matriz_real_jogador)
            
            try:
                linha = int(input(f"\nLinha inicial (1 a {tamanho}): ")) - 1
                coluna = int(input(f"Coluna inicial (1 a {tamanho}): ")) - 1
                orientacao = input("Orientação (H para horizontal, V para vertical): ").upper()
                
                # 2. TRAVA DE SEGURANÇA PARA ACEITAR APENAS H OU V
                if orientacao != "H" and orientacao != "V":
                    print("\033[31mErro: Digite apenas H ou V para a orientação.\033[0m")
                    continue # Ignora o resto e pede a mesma peça de novo
                
                if validando_posicao_escolhida(matriz_real_jogador, linha, coluna, tamanho_peca, orientacao):
                    for i in range(tamanho_peca):
                        if orientacao == "H":
                            matriz_real_jogador[linha][coluna + i] = sigla_peca 
                        elif orientacao == "V":
                            matriz_real_jogador[linha + i][coluna] = sigla_peca
                    
                    print(f"\n{nome_peca} posicionada com sucesso!")
                    break 
                else:
                    print("\033[31mPosição inválida! Passa da borda ou cai sobre outra peça. Tente de novo.\033[0m")
                    
            except ValueError:
                print("\033[31mEntrada inválida! Digite apenas números para linha e coluna.\033[0m")

def usar_olho_clinico(bancada_real_totem,usos_restantes,pontuacao):
    tamanho = len(bancada_real_totem)
    coordenada_valida = False

    while not coordenada_valida:
        try:
            print(f"\nOlho Clínico! Usos restantes: {usos_restantes}")
            linha = int(input(f"Linha (1 a {tamanho}): "))-1
            coluna = int(input(f"Coluna (1 a {tamanho}): "))-1
            
            if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                coordenada_valida = True
            else:
                print("Coordenada fora da bancada! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            
    pecas_encontradas = 0
    linha_inicio = max(0, linha - 1)
    linha_fim = min(tamanho, linha + 2)
    coluna_inicio = max(0, coluna - 1)
    coluna_fim = min(tamanho, coluna + 2)
    
    for r in range(linha_inicio, linha_fim):
        for c in range(coluna_inicio, coluna_fim):
            if bancada_real_totem[r][c] != " ": # '~' é o espaço vazio
                pecas_encontradas += 1
                
    usos_restantes -= 1
    pontuacao = max(0, pontuacao - 30) # Garante que não fica negativo
        
    print(f"\nO Olho Clínico achou {pecas_encontradas} casas ocupadas nessa área!")
    print(f"Penalidade de -30 pontos pontuação atual: {pontuacao}.")
    
    return usos_restantes, pontuacao

def sortear_jogada_novato(bancada_rastreio_jogador):
    tamanho = len(bancada_rastreio_jogador)
    casas_vazias = []
    
    for l in range(tamanho):
        for c in range(tamanho):
            if bancada_rastreio_jogador[l][c] == " ":
                casas_vazias.append((l, c))
                
    if len(casas_vazias) > 0:
        escolha = random.choice(casas_vazias)
        return escolha[0], escolha[1]
    return -1, -1

def sortear_jogada_veterano(bancada_rastreio_jogador, lista_vizinhos):
    tamanho = len(bancada_rastreio_jogador)
    opcoes_validas = []
    
    for coord in lista_vizinhos:
        l, c = coord
        if 0 <= l < tamanho and 0 <= c < tamanho:
            if bancada_rastreio_jogador[l][c] == " ":
                opcoes_validas.append((l, c))
                
    if len(opcoes_validas) > 0:
        escolha = random.choice(opcoes_validas) # usando metodo especifico da Biblioteca rondom "choice" para sorte valores dentro da lista 
        lista_vizinhos.remove(escolha)
        return escolha[0], escolha[1]
    else:
        lista_vizinhos.clear()
        return sortear_jogada_novato(bancada_rastreio_jogador)

def adicionar_vizinhos(linha, coluna, lista_vizinhos):
    lista_vizinhos.append((linha - 1, coluna)) # Cima
    lista_vizinhos.append((linha + 1, coluna)) # Baixo
    lista_vizinhos.append((linha, coluna - 1)) # Esquerda
    lista_vizinhos.append((linha, coluna + 1)) # Direita


#Ranking
def registrar_partida(placar, bancada_nome, modo, resultado, rodadas, pontuacao):
    """Guarda a partida na matriz do placar do dia."""
    # Adiciona uma lista com os dados dentro da lista principal (placar)
    placar.append([bancada_nome, modo, resultado, rodadas, pontuacao])

def exibir_placar(placar):

    print("\n" + "=" * 65)
    print("PLACAR DO DIA".center(65))
    print("=" * 65)
    
    if len(placar) == 0:
        print("Nenhuma partida registrada ainda.".center(65))
    else:
        # Ordena a lista baseada no índice 4 que é a pontuação
        placar.sort(key=lambda x: x[4], reverse=True)
        print(f"{'Bancada':<12} | {'Modo':<10} | {'Resultado':<12} | {'Rodadas':<7} | {'Pts'}")
        print("-" * 65)
        for p in placar:
            print(f"{p[0]:<12} | {p[1]:<10} | {p[2]:<12} | {p[3]:<7} | {p[4]}")
    print("=" * 65 + "\n")