import random 
import mod_04_matrizes  


# Validando  a peça cabe na bancada e não fica em cima de outra peça já colocada
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

# Cuida do posicionamento das peças do jogador (manual ou automático via menu)
def posicionar_pecas_jogador(matriz_real_jogador, tamanho):
    pecas = obter_lista_pecas(tamanho)

    print("\n [1] Posicionar Manualmente  [2] Espalhar Automaticamente: ")
    escolha = input("Opção: ").strip()

    if escolha == "2":
        posicionar_pecas_automatico(matriz_real_jogador, tamanho)
        print(
            "\n\033[32mSua bancada foi preenchida automaticamente com sucesso!\033[0m"
        )
        return

    for peca in pecas:
        nome_peca = peca[0]
        tamanho_peca = peca[1]
        sigla_peca = peca[2]

        while True:
            print(f"\n--- POSICIONANDO: {nome_peca} ({tamanho_peca} casas) ---")
            mod_04_matrizes.mostra_matriz(matriz_real_jogador)

            try:
                linha = int(input(f"\nLinha inicial (1 a {tamanho}): ")) - 1
                coluna = int(input(f"Coluna inicial (1 a {tamanho}): ")) - 1
                orientacao = input(
                    "Orientação (H para horizontal, V para vertical): "
                ).upper()

                if orientacao not in ["H", "V"]:
                    print(
                        "\033[31mErro: Digite apenas H ou V para a orientação.\033[0m"
                    )
                    continue

                if validando_posicao_escolhida(
                    matriz_real_jogador,
                    linha,
                    coluna,
                    tamanho_peca,
                    orientacao,
                ):
                    for i in range(tamanho_peca):
                        if orientacao == "H":
                            matriz_real_jogador[linha][coluna + i] = sigla_peca
                        elif orientacao == "V":
                            matriz_real_jogador[linha + i][coluna] = sigla_peca
                    print(f"\n{nome_peca} posicionada com sucesso!")
                    break
                else:
                    print(
                        "\033[31mPosição inválida! Passa da borda ou cai sobre outra peça.\033[0m"
                    )
            except ValueError:
                print(
                    "\033[31mEntrada inválida! Digite apenas números inteiros.\033[0m"
                )

# Executa o recurso do Olho Clínico: lê uma área 3x3 e desconta 30 pontos com piso em zero
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

# Sorteia uma casa vazia aleatória na bancada do jogador (IA Modo Novato)
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

# Seleciona uma casa vizinha da lista ou volta ao sorteio aleatório se a lista acabar (Totem Modo Veterano)
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

#Calcula e adiciona as coordenadas vizinhas (cima, baixo, esquerda, direita) após um acerto do Totem
def adicionar_vizinhos(linha, coluna, lista_vizinhos):
    lista_vizinhos.append((linha - 1, coluna)) # Cima
    lista_vizinhos.append((linha + 1, coluna)) # Baixo
    lista_vizinhos.append((linha, coluna - 1)) # Esquerda
    lista_vizinhos.append((linha, coluna + 1)) # Direita


#Ranking
#Salva os dados da partida concluída dentro da lista principal do placar
def registrar_partida(placar, bancada_nome, modo, resultado, rodadas, pontuacao):
    """Guarda a partida na matriz do placar do dia."""
    # Adiciona uma lista com os dados dentro da lista principal (placar)
    placar.append([bancada_nome, modo, resultado, rodadas, pontuacao])

def exibir_placar(placar):

    print("\n")
    print("PLACAR DO DIA".center(65))
    print()
    
    if len(placar) == 0:
        print("Nenhuma partida registrada ainda.".center(65))
    else:
        # Ordena a lista baseada no índice 4 que é a pontuação
        placar.sort(key=lambda x: x[4], reverse=True)
        print(f"{'Bancada':<12} | {'Modo':<10} | {'Resultado':<12} | {'Rodadas':<7} | {'Pts'}")
        print()
        for p in placar:
            print(f"{p[0]:<12} | {p[1]:<10} | {p[2]:<12} | {p[3]:<7} | {p[4]}")
    print()

#Retorna a lista oficial com o nome, tamanho e sigla de cada peça de acordo com a bancada escolhida
def obter_lista_pecas(tamanho):
    #etorna a lista de peças padrão de acordo com o tamanho da bancada.
    if tamanho == 6:
        return [
            ["Armadura", 3, "A1"],
            ["Capa", 2, "C1"],
            ["Capa", 2, "C2"],
            ["Elmo", 1, "E1"],
            ["Elmo", 1, "E2"],
        ]
    elif tamanho == 8:
        return [
            ["Par de Asas", 4, "AS1"],
            ["Armadura", 3, "A1"],
            ["Capa", 2, "C1"],
            ["Capa", 2, "C2"],
            ["Elmo", 1, "E1"],
            ["Elmo", 1, "E2"],
        ]
    elif tamanho == 10:
        return [
            ["Par de Asas", 4, "AS1"],
            ["Armadura", 3, "A1"],
            ["Armadura", 3, "A2"],
            ["Capa", 2, "C1"],
            ["Capa", 2, "C2"],
            ["Capa", 2, "C3"],
            ["Elmo", 1, "E1"],
            ["Elmo", 1, "E2"],
            ["Elmo", 1, "E3"],
            ["Elmo", 1, "E4"],
        ]
    return []

# Posiciona todas as peças aleatoriamente na matriz sem ultrapassar limites ou sobrepor peças
def posicionar_pecas_automatico(matriz_real, tamanho):
    #Espalha as peças aleatoriamente sem sobreposição e sem ultrapassar bordas.
    pecas = obter_lista_pecas(tamanho)

    for peca in pecas:
        tamanho_peca = peca[1]
        sigla_peca = peca[2]

        posicionou = False
        while not posicionou:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            orientacao = random.choice(["H", "V"])

            if validando_posicao_escolhida(
                matriz_real, linha, coluna, tamanho_peca, orientacao
            ):
                for i in range(tamanho_peca):
                    if orientacao == "H":
                        matriz_real[linha][coluna + i] = sigla_peca
                    elif orientacao == "V":
                        matriz_real[linha + i][coluna] = sigla_peca
                posicionou = True

# Verifica se todas as casas da peça atingida viraram 'X' e retorna o nome da peça destruída
def verificar_peca_destruida(matriz_real, matriz_rastreio, linha, coluna):
    sigla_peca = matriz_real[linha][coluna]
    tamanho = len(matriz_real)
    
    # Percorre a bancada procurando se ainda existe alguma casa desta peça sem 'X'
    for l in range(tamanho):
        for c in range(tamanho):
            if matriz_real[l][c] == sigla_peca:
                if matriz_rastreio[l][c] != "X":
                    return None  # Ainda não foi destruída por completo
                    
    # Retorna o nome da peça para o jogo anunciar na tela
    if sigla_peca.startswith("A") and not sigla_peca.startswith("AS"):
        return "Armadura"
    elif sigla_peca.startswith("AS"):
        return "Par de Asas"
    elif sigla_peca.startswith("C"):
        return "Capa"
    elif sigla_peca.startswith("E"):
        return "Elmo"
        
    return "Peça"

# Retorna a quantidade total de casas ocupadas por peças no tamanho de bancada selecionado
def total_casas_pecas(tamanho):
    #Retorna o número total de casas ocupadas por peças de acordo com a bancada.
    if tamanho == 6:
        return 9  # 3 + 2 + 2 + 1 + 1
    elif tamanho == 8:
        return 13  # 4 + 3 + 2 + 2 + 1 + 1
    elif tamanho == 10:
        return 20  # 4 + 3 + 3 + 2 + 2 + 2 + 1 + 1 + 1 + 1
    return 0

# Conta quantas marcas de acerto 'X' existem na bancada de rastreio
def contar_acertos(matriz_rastreio):
    #Conta quantos 'X' existem na bancada de rastreio.
    acertos = 0
    tamanho = len(matriz_rastreio)
    for l in range(tamanho):
        for c in range(tamanho):
            if matriz_rastreio[l][c] == "X":
                acertos += 1
    return acertos

#Conta quantas peças da bancada foram completamente destruídas ao longo do jogo
def contar_pecas_destruidas_total(matriz_real, matriz_rastreio, tamanho):
    """Conta quantas peças da bancada foram completamente destruídas."""
    pecas = obter_lista_pecas(tamanho)
    completadas = 0

    for peca in pecas:
        sigla = peca[2]
        destruida = True

        for l in range(tamanho):
            for c in range(tamanho):
                if matriz_real[l][c] == sigla and matriz_rastreio[l][c] != "X":
                    destruida = False
                    break

        if destruida:
            completadas += 1

    return completadas

#Calcula o aproveitamento (%) e exibe a tela de estatísticas com as duas bancadas reveladas por inteiro
def exibir_resumo_partida(
    resultado,
    rodadas,
    bancada_nome,
    matriz_real_totem,
    matriz_rastreio_totem,
    matriz_real_jogador,
    matriz_rastreio_jogador,
    usos_olho,
    pontuacao,
    tamanho,
):
    #Exibe a tela com o resumo detalhado da partida e revela as duas bancadas por inteiro.
    acertos = contar_acertos(matriz_rastreio_totem)
    erros = 0

    for l in range(tamanho):
        for c in range(tamanho):
            if matriz_rastreio_totem[l][c] == "o":
                erros += 1

    casas_cantadas = acertos + erros
    aproveitamento = (
        (acertos / casas_cantadas * 100) if casas_cantadas > 0 else 0.0
    )

    pecas_totem_completadas = contar_pecas_destruidas_total(
        matriz_real_totem, matriz_rastreio_totem, tamanho
    )
    pecas_jogador_completadas = contar_pecas_destruidas_total(
        matriz_real_jogador, matriz_rastreio_jogador, tamanho
    )
    usos_olho_gastos = 3 - usos_olho

    print("\n" + "-" * 55)
    print(" RESUMO FINAL DA PARTIDA ".center(55, "-"))
    print("-" * 55)
    print(f"Resultado: {resultado}")
    print(f"Bancada Escolhida: {bancada_nome}")
    print(f"Total de Rodadas: {rodadas}")
    print(f"Casas Cantadas por Você: {casas_cantadas}")
    print(f"Acertos: {acertos} | Erros: {erros}")
    print(f"Aproveitamento do Jogador: {aproveitamento:.1f}%")
    print(f"Peças do Totem Destruídas por Você: {pecas_totem_completadas}")
    print(f"Suas Peças Destruídas pelo Totem: {pecas_jogador_completadas}")
    print(f"Usos do Olho Clínico Gastos: {usos_olho_gastos}/3")
    print(f"Pontuação Final: {pontuacao}")
    print()

    #Revelação das duas bancadas completas
    print("\n  BANCADA DO TOTEM REVELADA ")
    mod_04_matrizes.mostra_matriz(matriz_real_totem)

    print("\n BANCADA REVELADA JOGADOR ")
    mod_04_matrizes.mostra_matriz(matriz_real_jogador)
    print()