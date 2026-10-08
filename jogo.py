# DEMO DE ESTUDO - Gincana dos Ateliês
# Esta versão foi feita para EXECUTAR E ENTENDER o funcionamento do jogo.
# Não use este arquivo como código final de entrega do P2.

import random


# ============================================================
# DADOS DAS BANCADAS
# ============================================================

def obter_configuracao(tamanho):
    if tamanho == 6:
        return [
            ("Armadura", 3, 1),
            ("Capa", 2, 2),
            ("Elmo", 1, 2)
        ]
    elif tamanho == 8:
        return [
            ("Asas", 4, 1),
            ("Armadura", 3, 1),
            ("Capa", 2, 2),
            ("Elmo", 1, 2)
        ]
    else:
        return [
            ("Asas", 4, 1),
            ("Armadura", 3, 2),
            ("Capa", 2, 3),
            ("Elmo", 1, 4)
        ]


# ============================================================
# MATRIZES
# ============================================================

def criar_matriz(tamanho, simbolo="."):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(simbolo)

        matriz.append(linha)

    return matriz


def copiar_matriz(matriz):
    copia = []

    for linha in matriz:
        nova_linha = []

        for valor in linha:
            nova_linha.append(valor)

        copia.append(nova_linha)

    return copia


def mostrar_bancada(matriz, revelar=True):
    tamanho = len(matriz)

    print()
    print("    ", end="")

    for coluna in range(tamanho):
        print(f"{coluna + 1:3}", end="")

    print()

    print("    " + "---" * tamanho)

    for i in range(tamanho):
        print(f"{i + 1:2} |", end="")

        for j in range(tamanho):
            print(f"{matriz[i][j]:3}", end="")

        print()

    print()


# ============================================================
# PEÇAS
# Cada peça é representada por uma tupla:
# (nome, tamanho, numero_da_peca)
# ============================================================

def criar_lista_pecas(tamanho):
    configuracao = obter_configuracao(tamanho)
    pecas = []

    contador = 1

    for item in configuracao:
        nome = item[0]
        tamanho_peca = item[1]
        quantidade = item[2]

        for numero in range(quantidade):
            pecas.append((nome, tamanho_peca, contador))
            contador += 1

    return pecas


# ============================================================
# POSICIONAMENTO
# ============================================================

def posicao_valida(matriz, linha, coluna, comprimento, orientacao):
    tamanho = len(matriz)

    if linha < 0 or linha >= tamanho:
        return False

    if coluna < 0 or coluna >= tamanho:
        return False

    if orientacao == "H":
        if coluna + comprimento > tamanho:
            return False

        for j in range(coluna, coluna + comprimento):
            if matriz[linha][j] != ".":
                return False

    else:
        if linha + comprimento > tamanho:
            return False

        for i in range(linha, linha + comprimento):
            if matriz[i][coluna] != ".":
                return False

    return True


def colocar_peca(matriz, linha, coluna, comprimento, orientacao, identificador):
    if orientacao == "H":
        for j in range(coluna, coluna + comprimento):
            matriz[linha][j] = identificador
    else:
        for i in range(linha, linha + comprimento):
            matriz[i][coluna] = identificador


def posicionar_pecas_automaticamente(matriz, pecas):
    tamanho = len(matriz)

    for peca in pecas:
        nome = peca[0]
        comprimento = peca[1]
        numero = peca[2]

        colocada = False

        while not colocada:
            linha = random.randrange(tamanho)
            coluna = random.randrange(tamanho)

            if random.randrange(2) == 0:
                orientacao = "H"
            else:
                orientacao = "V"

            if posicao_valida(
                matriz, linha, coluna, comprimento, orientacao
            ):
                identificador = f"{numero}"
                colocar_peca(
                    matriz,
                    linha,
                    coluna,
                    comprimento,
                    orientacao,
                    identificador
                )
                colocada = True


def posicionar_pecas_jogador(matriz, pecas):
    print("\nPOSICIONAMENTO DAS SUAS PEÇAS")
    print("Informe linha, coluna e orientação.")
    print("H = horizontal | V = vertical")
    print("Você também pode digitar A para posicionar automaticamente.\n")

    for peca in pecas:
        nome = peca[0]
        comprimento = peca[1]
        numero = peca[2]

        while True:
            mostrar_bancada(matriz)

            print(f"Peça: {nome} | tamanho: {comprimento}")

            escolha = input(
                "Digite linha coluna orientação ou A: "
            ).strip().upper()

            if escolha == "A":
                posicionar_pecas_automaticamente(
                    matriz,
                    pecas[pecas.index(peca):]
                )
                return

            try:
                partes = escolha.split()

                if len(partes) != 3:
                    print("Digite, por exemplo: 2 3 H")
                    continue

                linha = int(partes[0]) - 1
                coluna = int(partes[1]) - 1
                orientacao = partes[2]

                if orientacao not in ["H", "V"]:
                    print("Orientação inválida.")
                    continue

                if not posicao_valida(
                    matriz,
                    linha,
                    coluna,
                    comprimento,
                    orientacao
                ):
                    print("Posição inválida: não cabe ou sobrepõe outra peça.")
                    continue

                identificador = str(numero)

                colocar_peca(
                    matriz,
                    linha,
                    coluna,
                    comprimento,
                    orientacao,
                    identificador
                )

                break

            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente.")


# ============================================================
# ATAQUE
# ============================================================

def criar_matriz_de_tiros(tamanho):
    return criar_matriz(tamanho, "?")


def fazer_jogada_jogador():
    while True:
        entrada = input("Escolha linha e coluna: ").strip()

        try:
            partes = entrada.split()

            if len(partes) != 2:
                print("Digite, por exemplo: 3 5")
                continue

            linha = int(partes[0]) - 1
            coluna = int(partes[1]) - 1

            return linha, coluna

        except ValueError:
            print("Digite apenas números.")


def casa_valida(matriz, linha, coluna):
    tamanho = len(matriz)

    return (
        linha >= 0
        and linha < tamanho
        and coluna >= 0
        and coluna < tamanho
    )


def registrar_tiro(tabuleiro_oculto, tabuleiro_tiros,
                   linha, coluna, simbolo_acerto="X"):
    valor = tabuleiro_oculto[linha][coluna]

    if valor == ".":
        tabuleiro_tiros[linha][coluna] = "o"
        return False, None

    tabuleiro_tiros[linha][coluna] = simbolo_acerto
    return True, valor


def listar_vizinhas(linha, coluna, tamanho):
    vizinhos = []

    possibilidades = [
        (linha - 1, coluna),
        (linha + 1, coluna),
        (linha, coluna - 1),
        (linha, coluna + 1)
    ]

    for posicao in possibilidades:
        i = posicao[0]
        j = posicao[1]

        if i >= 0 and i < tamanho and j >= 0 and j < tamanho:
            vizinhos.append((i, j))

    return vizinhos


# ============================================================
# MODO DO TOTEM
# ============================================================

def jogada_totem_novato(tabuleiro_jogador, tiros_totem):
    tamanho = len(tabuleiro_jogador)

    disponiveis = []

    for i in range(tamanho):
        for j in range(tamanho):
            if tiros_totem[i][j] == "?":
                disponiveis.append((i, j))

    if len(disponiveis) == 0:
        return None

    return random.choice(disponiveis)


def jogada_totem_veterano(tabuleiro_jogador, tiros_totem, alvo):
    tamanho = len(tabuleiro_jogador)

    if alvo is not None:
        vizinhos = listar_vizinhas(
            alvo[0],
            alvo[1],
            tamanho
        )

        disponiveis = []

        for posicao in vizinhos:
            i = posicao[0]
            j = posicao[1]

            if tiros_totem[i][j] == "?":
                disponiveis.append(posicao)

        if len(disponiveis) > 0:
            return random.choice(disponiveis)

    return jogada_totem_novato(tabuleiro_jogador, tiros_totem)


# ============================================================
# PEÇAS COMPLETADAS
# ============================================================

def contar_casas_peca(tabuleiro, identificador):
    quantidade = 0

    for linha in tabuleiro:
        for valor in linha:
            if valor == identificador:
                quantidade += 1

    return quantidade


def pecas_completadas(tabuleiro_original, tiros, pecas):
    completadas = []

    for peca in pecas:
        numero = str(peca[2])
        total = peca[1]
        descobertas = 0

        for i in range(len(tabuleiro_original)):
            for j in range(len(tabuleiro_original)):
                if (
                    tabuleiro_original[i][j] == numero
                    and tiros[i][j] == "X"
                ):
                    descobertas += 1

        if descobertas == total:
            completadas.append(numero)

    return completadas


def todas_pecas_descobertas(tabuleiro, tiros):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] != "." and tiros[i][j] != "X":
                return False

    return True


# ============================================================
# OLHO CLÍNICO
# ============================================================

def usar_olho_clinico(tabuleiro, linha, coluna):
    tamanho = len(tabuleiro)
    quantidade = 0

    inicio_linha = linha - 1
    fim_linha = linha + 1

    inicio_coluna = coluna - 1
    fim_coluna = coluna + 1

    for i in range(inicio_linha, fim_linha + 1):
        for j in range(inicio_coluna, fim_coluna + 1):

            if i >= 0 and i < tamanho and j >= 0 and j < tamanho:
                if tabuleiro[i][j] != ".":
                    quantidade += 1

    return quantidade


def pedir_casa_olho(tamanho):
    while True:
        entrada = input(
            "Casa para o olho clínico (linha coluna): "
        ).strip()

        try:
            partes = entrada.split()

            if len(partes) != 2:
                print("Digite duas posições.")
                continue

            linha = int(partes[0]) - 1
            coluna = int(partes[1]) - 1

            if (
                linha < 0
                or linha >= tamanho
                or coluna < 0
                or coluna >= tamanho
            ):
                print("Casa fora da bancada.")
                continue

            return linha, coluna

        except ValueError:
            print("Entrada inválida.")


# ============================================================
# PONTUAÇÃO
# ============================================================

def calcular_pontuacao(acertos, erros, pecas_completadas_qtd,
                       usos_olho, venceu):
    pontos = 0

    pontos += acertos * 10
    pontos -= erros * 5
    pontos += pecas_completadas_qtd * 50
    pontos -= usos_olho * 30

    if venceu:
        pontos += 200

    if pontos < 0:
        pontos = 0

    return pontos


# ============================================================
# RESUMO
# ============================================================

def mostrar_resumo(resultado, rodadas, casas_cantadas,
                   acertos, erros, aproveitamento,
                   pecas_jogador, pecas_totem,
                   usos_olho, pontuacao,
                   tabuleiro_jogador,
                   tabuleiro_totem):
    print("\n" + "=" * 60)
    print("RESUMO DA PARTIDA")
    print("=" * 60)

    print("Resultado:", resultado)
    print("Rodadas:", rodadas)
    print("Casas cantadas pelo jogador:", casas_cantadas)
    print("Acertos:", acertos)
    print("Erros:", erros)
    print(f"Aproveitamento: {aproveitamento:.1f}%")
    print("Peças completadas pelo jogador:", pecas_jogador)
    print("Peças completadas pelo totem:", pecas_totem)
    print("Usos do olho clínico:", usos_olho)
    print("Pontuação final:", pontuacao)

    print("\nBANCADA DO JOGADOR - REVELADA")
    mostrar_bancada(tabuleiro_jogador)

    print("BANCADA DO TOTEM - REVELADA")
    mostrar_bancada(tabuleiro_totem)

    print("=" * 60)


# ============================================================
# PLACAR DO DIA
# ============================================================

def adicionar_placar(placar, tamanho, modo, resultado,
                     rodadas, pontuacao):
    registro = [
        tamanho,
        modo,
        resultado,
        rodadas,
        pontuacao
    ]

    placar.append(registro)


def mostrar_placar(placar):
    print("\n" + "=" * 60)
    print("PLACAR DO DIA")
    print("=" * 60)

    if len(placar) == 0:
        print("Nenhuma partida registrada.")
        return

    ordenado = []

    for registro in placar:
        ordenado.append(registro)

    # Ordenação simples por pontuação, sem biblioteca extra.
    for i in range(len(ordenado)):
        for j in range(i + 1, len(ordenado)):
            if ordenado[j][4] > ordenado[i][4]:
                temp = ordenado[i]
                ordenado[i] = ordenado[j]
                ordenado[j] = temp

    print("POS | BANCADA | MODO | RESULTADO | RODADAS | PONTOS")

    posicao = 1

    for registro in ordenado:
        tamanho = registro[0]
        modo = registro[1]
        resultado = registro[2]
        rodadas = registro[3]
        pontuacao = registro[4]

        print(
            f"{posicao:3} | "
            f"{tamanho:7} | "
            f"{modo:6} | "
            f"{resultado:9} | "
            f"{rodadas:7} | "
            f"{pontuacao:6}"
        )

        posicao += 1

    print("=" * 60)


# ============================================================
# REGRAS
# ============================================================

def mostrar_regras():
    print("\n" + "=" * 60)
    print("REGRAS - GINCANA DOS ATELIÊS")
    print("=" * 60)

    print("1. Você escolhe uma das três bancadas.")
    print("2. Você posiciona suas peças.")
    print("3. O totem posiciona as peças dele automaticamente.")
    print("4. Você e o totem jogam alternadamente.")
    print("5. Você deve descobrir todas as peças do totem.")
    print("6. O totem tenta descobrir suas peças.")
    print("7. Acerto = X.")
    print("8. Erro = o.")
    print("9. Repetir uma casa não vale como jogada.")
    print("10. O olho clínico mostra quantas casas com peça")
    print("    existem no quadrado 3x3 ao redor da casa escolhida.")
    print()
    print("PONTUAÇÃO")
    print("+10 por casa com peça descoberta")
    print("-5 por casa vazia")
    print("+50 por peça completada")
    print("-30 por olho clínico")
    print("+200 por vitória")
    print("A pontuação mínima é 0.")
    print("=" * 60)


# ============================================================
# ESCOLHAS
# ============================================================

def escolher_bancada():
    while True:
        print("\nEscolha a bancada:")
        print("1 - Bancada de ensaio (6x6)")
        print("2 - Bancada de montagem (8x8)")
        print("3 - Bancada de véspera (10x10)")

        escolha = input("Opção: ").strip()

        if escolha == "1":
            return 6, "Ensaio"

        elif escolha == "2":
            return 8, "Montagem"

        elif escolha == "3":
            return 10, "Véspera"

        else:
            print("Opção inválida.")


def escolher_modo():
    while True:
        print("\nModo do adversário:")
        print("1 - Novato")
        print("2 - Veterano")

        escolha = input("Opção: ").strip()

        if escolha == "1":
            return "Novato"

        elif escolha == "2":
            return "Veterano"

        else:
            print("Opção inválida.")


# ============================================================
# JOGADOR
# ============================================================

def mostrar_estado_jogo(tabuleiro_jogador, tiros_totem):
    print("\n" + "=" * 60)
    print("SUA BANCADA")
    print("=" * 60)
    mostrar_bancada(tabuleiro_jogador)

    print("O QUE VOCÊ JÁ DESCOBRIU DA BANCADA DO TOTEM")
    print("=" * 60)
    mostrar_bancada(tiros_totem)


def jogador_usar_olho(tabuleiro_totem, usos):
    if usos <= 0:
        print("Você não possui mais usos do olho clínico.")
        return usos, False

    linha, coluna = pedir_casa_olho(len(tabuleiro_totem))

    quantidade = usar_olho_clinico(
        tabuleiro_totem,
        linha,
        coluna
    )

    print(
        f"No quadrado 3x3 centrado nessa casa existem "
        f"{quantidade} casas com peça."
    )

    usos -= 1

    return usos, True


# ============================================================
# UMA PARTIDA
# ============================================================

def jogar_partida(tamanho, nome_bancada, modo):
    print("\n" + "=" * 60)
    print("NOVA PARTIDA")
    print("=" * 60)
    print("Bancada:", nome_bancada)
    print("Modo:", modo)

    pecas = criar_lista_pecas(tamanho)

    tabuleiro_jogador = criar_matriz(tamanho)
    tabuleiro_totem = criar_matriz(tamanho)

    tiros_jogador = criar_matriz_de_tiros(tamanho)
    tiros_totem = criar_matriz_de_tiros(tamanho)

    # Jogador posiciona as peças.
    posicionar_pecas_jogador(
        tabuleiro_jogador,
        pecas
    )

    # O totem posiciona automaticamente.
    posicionar_pecas_automaticamente(
        tabuleiro_totem,
        pecas
    )

    print("\nTodas as peças foram posicionadas.")
    print("A partida vai começar!")

    usos_olho = 3

    acertos = 0
    erros = 0
    casas_cantadas = 0
    rodadas = 0

    pecas_jogador_completadas = []
    pecas_totem_completadas = []

    alvo_veterano = None

    vez = "jogador"

    while True:

        if vez == "jogador":
            mostrar_estado_jogo(
                tiros_totem,
                tiros_jogador
            )

            print("Sua vez.")
            print("1 - Fazer jogada")
            print("2 - Usar olho clínico")
            print("3 - Desistir")

            escolha = input("Opção: ").strip()

            if escolha == "2":
                usos_olho, usado = jogador_usar_olho(
                    tabuleiro_totem,
                    usos_olho
                )

                if usado:
                    continue

            elif escolha == "3":
                resultado = "Desistencia"

                aproveitamento = 0

                pontuacao = calcular_pontuacao(
                    acertos,
                    erros,
                    len(pecas_totem_completadas),
                    3 - usos_olho,
                    False
                )

                mostrar_resumo(
                    resultado,
                    rodadas,
                    casas_cantadas,
                    acertos,
                    erros,
                    aproveitamento,
                    len(pecas_totem_completadas),
                    len(pecas_jogador_completadas),
                    3 - usos_olho,
                    pontuacao,
                    tabuleiro_jogador,
                    tabuleiro_totem
                )

                return resultado, rodadas, pontuacao

            elif escolha != "1":
                print("Opção inválida.")
                continue

            linha, coluna = fazer_jogada_jogador()

            if not casa_valida(
                tabuleiro_totem,
                linha,
                coluna
            ):
                print("Casa fora da bancada.")
                continue

            if tiros_totem[linha][coluna] != "?":
                print("Essa casa já foi cantada. Você joga novamente.")
                continue

            casas_cantadas += 1

            acertou, identificador = registrar_tiro(
                tabuleiro_totem,
                tiros_totem,
                linha,
                coluna
            )

            if acertou:
                acertos += 1
                print("ACERTO! X")

                completadas = pecas_completadas(
                    tabuleiro_totem,
                    tiros_totem,
                    pecas
                )

                for peca_id in completadas:
                    if peca_id not in pecas_totem_completadas:
                        pecas_totem_completadas.append(peca_id)
                        print(
                            f"Você completou a peça {peca_id}!"
                        )

                if todas_pecas_descobertas(
                    tabuleiro_totem,
                    tiros_totem
                ):
                    resultado = "Vitoria"

                    if casas_cantadas > 0:
                        aproveitamento = (
                            acertos / casas_cantadas
                        ) * 100
                    else:
                        aproveitamento = 0

                    pontuacao = calcular_pontuacao(
                        acertos,
                        erros,
                        len(pecas_totem_completadas),
                        3 - usos_olho,
                        True
                    )

                    mostrar_resumo(
                        resultado,
                        rodadas,
                        casas_cantadas,
                        acertos,
                        erros,
                        aproveitamento,
                        len(pecas_totem_completadas),
                        len(pecas_jogador_completadas),
                        3 - usos_olho,
                        pontuacao,
                        tabuleiro_jogador,
                        tabuleiro_totem
                    )

                    return resultado, rodadas, pontuacao

            else:
                erros += 1
                print("ERRO! Casa vazia: o")

            vez = "totem"

        else:
            print("\n" + "-" * 60)
            print("VEZ DO TOTEM")
            print("-" * 60)

            if modo == "Novato":
                jogada = jogada_totem_novato(
                    tabuleiro_jogador,
                    tiros_jogador
                )
            else:
                jogada = jogada_totem_veterano(
                    tabuleiro_jogador,
                    tiros_jogador,
                    alvo_veterano
                )

            if jogada is None:
                print("Não há mais casas disponíveis.")
                resultado = "Fim"

                pontuacao = calcular_pontuacao(
                    acertos,
                    erros,
                    len(pecas_totem_completadas),
                    3 - usos_olho,
                    False
                )

                mostrar_resumo(
                    resultado,
                    rodadas,
                    casas_cantadas,
                    acertos,
                    erros,
                    0,
                    len(pecas_totem_completadas),
                    len(pecas_jogador_completadas),
                    3 - usos_olho,
                    pontuacao,
                    tabuleiro_jogador,
                    tabuleiro_totem
                )

                return resultado, rodadas, pontuacao

            linha = jogada[0]
            coluna = jogada[1]

            print(
                f"O totem cantou: "
                f"linha {linha + 1}, coluna {coluna + 1}"
            )

            acertou, identificador = registrar_tiro(
                tabuleiro_jogador,
                tiros_jogador,
                linha,
                coluna
            )

            if acertou:
                print("Totem acertou! X")
                alvo_veterano = (linha, coluna)

                completadas = pecas_completadas(
                    tabuleiro_jogador,
                    tiros_jogador,
                    pecas
                )

                for peca_id in completadas:
                    if peca_id not in pecas_jogador_completadas:
                        pecas_jogador_completadas.append(peca_id)
                        print(
                            f"O totem completou a peça {peca_id}!"
                        )

                if todas_pecas_descobertas(
                    tabuleiro_jogador,
                    tiros_jogador
                ):
                    resultado = "Derrota"

                    if casas_cantadas > 0:
                        aproveitamento = (
                            acertos / casas_cantadas
                        ) * 100
                    else:
                        aproveitamento = 0

                    pontuacao = calcular_pontuacao(
                        acertos,
                        erros,
                        len(pecas_totem_completadas),
                        3 - usos_olho,
                        False
                    )

                    mostrar_resumo(
                        resultado,
                        rodadas,
                        casas_cantadas,
                        acertos,
                        erros,
                        aproveitamento,
                        len(pecas_totem_completadas),
                        len(pecas_jogador_completadas),
                        3 - usos_olho,
                        pontuacao,
                        tabuleiro_jogador,
                        tabuleiro_totem
                    )

                    return resultado, rodadas, pontuacao

            else:
                print("Totem errou! o")

                # No modo veterano, depois de errar,
                # ele volta ao sorteio aleatório.
                alvo_veterano = None

            rodadas += 1
            vez = "jogador"


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    placar = []

    while True:
        print("\n")
        print("=" * 60)
        print("Gincana dos Ateliês")
        print("Duelo na estação de jogos da Pocket")
        print("=" * 60)
        print("1 - Nova partida")
        print("2 - Regras")
        print("3 - Placar do dia")
        print("4 - Encerrar")
        print("=" * 60)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            tamanho, nome_bancada = escolher_bancada()
            modo = escolher_modo()

            try:
                resultado, rodadas, pontuacao = jogar_partida(
                    tamanho,
                    nome_bancada,
                    modo
                )

                adicionar_placar(
                    placar,
                    tamanho,
                    modo,
                    resultado,
                    rodadas,
                    pontuacao
                )

            except Exception as erro:
                # Proteção extra para que uma entrada inesperada
                # não derrube o totem.
                print("\nOcorreu um erro durante a partida.")
                print("A partida foi encerrada com segurança.")
                print("Detalhe técnico:", erro)

        elif escolha == "2":
            mostrar_regras()

        elif escolha == "3":
            mostrar_placar(placar)

        elif escolha == "4":
            print("Totem encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
