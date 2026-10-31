# ==============================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 2 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
# ==============================================================================

#IMPORTAÇÕES
import os
import mod_03_regras_jogo 
import mod_02_menus_secundario
import mod_04_matrizes
import mod_05_mecanicas

#VARIAVEIS GLOBAIS
codigo_encerramento = 0.0
acertos = 0
erros = 0
casas_cantadas = 0
rodadas = 0
placar_do_dia = []

#FUNÇOES 
def limpar_tela():#Limpa a tela do terminal de acordo com o sistema operacional
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#CÓDIDO PRINCIPAL

# Essa parte do código utiliza a função isdigit para verificar se todos os caracteres presentes dentro da variável codigo_encerramento são números e, caso não sejam,o while continuará executando...

print("\n[-------Administrador. Cuca----------]\n");
print("CRIE O CÓDIGO DE ENCERRAMENTO: ",end="");
# Pede ao usuário para criar um código de encerramento
codigo_encerramento = input();
# Continua pedindo o código enquanto ele não tiver apenas números
while not codigo_encerramento.isdigit():
    # Informa ao usuário que o código digitado é inválido
    print("\033[31mCódigo inválido. Digite apenas números.\033[0m");
     # Pede um novo código
    codigo_encerramento  = input("\nCRIE NOVAMENTE CÓDIGO: ");
    limpar_tela()
# Informa que o código foi aceito
print("\033[32mCódigo registrado com sucesso\033[0m")
# Pausa o programa até o usuário pressionar ENTER
input("\nPressione [ENTER] para continuar ... . . . . . ")
limpar_tela()


# Essa parte código  abaixo utiliza  o while e match"case" para manter toda instrutura do jogo rodando (código prinicipal) em loop que é controlado por um variavel recebida e solicitada ao jogador atraves  do menu e o match case direciona o jagador algumas das opções escolhida do menu...

opcao_menu = 0
while opcao_menu != "4": #laço de repetição que se repeti enquanto a variavel opcao_menu for diferente de 3
  print()
  print("\033[1mBem-vindo GiCanA dOs AtElieS\033[0m".center(50))

  print()
  print("              [1] JOGAR")
  print("              [2] REGRAS")
  print("              [3] PLACAR")
  print("              [4] SAIR")
  print() 
  opcao_menu = input() # solicitando usuario uma  valor do menu ,nesse momento não utilize try excepet para trata exceçoes de entrada pois macth case esta fazendo isso trazendo um reposta  para qualquer dado digitado fora dos case especeficos sem quebra o programa

  
  match opcao_menu:# caso 1 onde acontece o jogo
      case "1":
        #seleção da bancada e do modo
        tamanho, nome = mod_02_menus_secundario.escolha_bancada()

        # CRIAÇÃO DAS BANCTADAS DA PARTIDA

        # Duas matrizes reais (com as peças) e duas de rastreio (com acertos/erros)
        matriz_real_totem = mod_04_matrizes.criar_matriz(tamanho) 
        matriz_rastreio_totem = mod_04_matrizes.criar_matriz(tamanho) 

        matriz_rastreio_jogador = mod_04_matrizes.criar_matriz(tamanho)
        matriz_real_jogador = mod_04_matrizes.criar_matriz(tamanho)

        print(f"\nBancada escolhida: {nome}")
        print(f"Tamanho: {tamanho}x{tamanho}")
    
        modo = mod_02_menus_secundario.escolher_modo()
      
        input("\nPrecione [enter] para continuar ... . . . . . ")
        print()
        limpar_tela()

        #POSICIONAMENTO DAS PEÇAS
        print()
        print("--- PREPARAÇÃO DAS PEÇAS ---")
        mod_05_mecanicas.posicionar_pecas_jogador(matriz_real_jogador, tamanho)
        mod_05_mecanicas.posicionar_pecas_automatico(matriz_real_totem, tamanho) 

        #VARIAVEIS DE CONTROLE PARA PARTIDA ATUAL
        pontuacao = 0
        usos_olho = 3
        rodadas = 0
        lista_vizinhos_totem = [] 
        
        #LAÇO DA PARTIDA ATUAL RODANDO 
        while True:
            limpar_tela()
            
            print(f"--- PONTUAÇÃO: {pontuacao} ---\n".center(60))
            
            # Exibe as duas bancadas na tela em todas as rodadas
            print("->Bancada Do TOTEM ")
            mod_04_matrizes.mostra_matriz(matriz_rastreio_totem)
            print()
            print("->Bancada Jogador-Play1") 

            mod_04_matrizes.mostra_matriz(matriz_real_jogador)
            mod_03_regras_jogo.legendas_acerto_erros()

            print("Sua vez!")
            print("Escolha uma acão\n")
            acao = input(f"[1] Jogar [2] Desistir [3] Olho Clínico ({usos_olho} usos): ")

            # OPÇÃO 2: DESISTÊNCIA -- DENTRO DO LAÇO DA PARTIDA
            if acao == '2':
                print("Você desistiu!")

                mod_05_mecanicas.registrar_partida(placar_do_dia, nome, modo, "Desistência", rodadas, pontuacao)

                # Exibe o resumo da partida
                mod_05_mecanicas.exibir_resumo_partida("Desistência", rodadas, nome, matriz_real_totem, matriz_rastreio_totem, matriz_real_jogador, matriz_rastreio_jogador, usos_olho, pontuacao, tamanho)   

                input("Pressione [enter] para voltar ao menu principal...")          
                break # Encerra o laço da partida e volta ao menu principal

            #OPÇÃO 3: OLHO CLÍNICO -- DENTRO DO LAÇO DA PARTIDA   
            elif acao == '3':
                if usos_olho > 0:
                    usos_olho, pontuacao = mod_05_mecanicas.usar_olho_clinico(matriz_real_totem, usos_olho, pontuacao)
                else:
                    print("Você não tem mais usos do Olho Clínico!")
                input("Pressione [enter] para continuar...")
                continue #Retorna ao início da escolha 123 sem passar a vez para o Totem

            #OPÇÃO 1: JOGA -- DENTRO DO LAÇO DA PARTIDA   
            elif acao == '1':
                try:
                    linha = int(input(f"\nLinha=[1 a {tamanho}]: ")) - 1
                    coluna = int(input(f"Coluna=[1 a {tamanho}]: ")) - 1

                    # Checa se a posição está dentro do tabuleiro/validação de limites lógicos da bancada
                    if 0 <= linha < tamanho and 0 <= coluna < tamanho:

                        #TRAVA DE CASA REPETIDA: Se já tiver 'X' ou 'o', avisa e não gasta o turno
                        # Validação de casa já mostrada anteriormente
                        if matriz_rastreio_totem[linha][coluna] != " ":
                            print(
                                "\n\033[33mVocê já cantou essa casa antes! Escolha outra posição.\033[0m"
                            )
                            input("Pressione [enter] para tentar de novo...")
                            continue  #Volta para o início do loop partida sem passar a vez para o Totem

                        #Resolução da jogada do jogador
                        if matriz_real_totem[linha][coluna] != " ":
                            print("\nBuUh! você acertou uma peça :)")
                            matriz_rastreio_totem[linha][coluna] = "X"
                            pontuacao += 10

                            # PEGA O NOME DA PEÇA DESTRUÍDA E EXIBE
                            peca_destruida = mod_05_mecanicas.verificar_peca_destruida(
                                matriz_real_totem, matriz_rastreio_totem, linha, coluna
                            )
                            if peca_destruida:
                                print(f"\033[32mPARABÉNS! Você destruiu completamente: {peca_destruida} (+50 pts bônus)!\033[0m")
                                pontuacao += 50
                        else:
                            print("\nÁgua!não tinha peça aqui :(")
                            matriz_rastreio_totem[linha][coluna] = "o"
                            pontuacao -= 5
                            if pontuacao < 0:
                                pontuacao = 0

                    else:
                        print("\nCoordenada fora da bancada!")
                        input("Pressione [enter] para tentar de novo...")
                        continue  # Não gasta o turno se digitou coordenada fora do tabuleiro

                except ValueError:
                    print("\nEntrada inválida! Digite apenas números.")
                    input("Pressione [enter] para tentar de novo...")
                    continue  #Não gasta o turno se digitou algo errado

                input("\nPressione [enter] para o turno do Totem...")

                #VEZ DO TOTEM (NOVATO/VETERANO-UTOMÁTICO)
                print("\nVez do TOTEM!")
                if modo == "Novato":
                    linha_bancada, coluna_bancada = (
                        mod_05_mecanicas.sortear_jogada_novato(
                            matriz_rastreio_jogador
                        )
                    )
                else:
                    linha_bancada, coluna_bancada = (
                        mod_05_mecanicas.sortear_jogada_veterano(
                            matriz_rastreio_jogador, lista_vizinhos_totem
                        )
                    )

                if linha_bancada != -1:
                    print(f"O totem escolheu na casa ({linha_bancada + 1}, {coluna_bancada + 1}). ")

                    if matriz_real_jogador[linha_bancada][coluna_bancada] not in [" ","X", "o"]:
                        print("\033[31mO Totem acertou uma peça sua!\033[0m")
                        matriz_rastreio_jogador[linha_bancada][coluna_bancada] = "X"
                        
                        # 2. VERIFICA SE DESTRUIU A PEÇA JOGADOR
                        peca_totem = mod_05_mecanicas.verificar_peca_destruida(matriz_real_jogador, matriz_rastreio_jogador, linha_bancada, coluna_bancada)
                        if peca_totem:
                            print(f"\033[31mATENÇÃO: O Totem destruiu totalmente seu/sua {peca_totem}!\033[0m")
                            if modo == "Veterano":
                              lista_vizinhos_totem.clear()
                        elif modo == "Veterano":
                            mod_05_mecanicas.adicionar_vizinhos(linha_bancada,coluna_bancada,lista_vizinhos_totem,)
                    else:
                        print("\033[32mO Totem deu água!\033[0m")
                        matriz_rastreio_jogador[linha_bancada][coluna_bancada] = "o"

                #CHECAGEM DE VITÓRIA E DERROTA
                total_alvos = mod_05_mecanicas.total_casas_pecas(tamanho)
                acertos_jogador = mod_05_mecanicas.contar_acertos(matriz_rastreio_totem)
                acertos_totem = mod_05_mecanicas.contar_acertos( matriz_rastreio_jogador)

                #VERIFICANDO SE JOGADOR VENCEU 

                # Condição de Vitória do Jogador
                if acertos_jogador == total_alvos:
                    pontuacao += 200  #Bônus de vitória
                    limpar_tela()
                    print()
                    print("  PARABÉNS! VOCÊ DESTRUIU TODAS AS PEÇAS DO TOTEM!")
                    print(f"   VITÓRIA! Pontuação Final: {pontuacao}")
                    print()
                    mod_05_mecanicas.registrar_partida(placar_do_dia, nome, modo, "Vitória", rodadas + 1, pontuacao)

                    input("Pressione [enter] para ver o resumo. . .")
                    limpar_tela()

                    mod_05_mecanicas.exibir_resumo_partida("Vitória", rodadas + 1, nome, matriz_real_totem,matriz_rastreio_totem, matriz_real_jogador,matriz_rastreio_jogador,usos_olho, pontuacao, tamanho)

                    input("Pressione [enter] para sair. . .")
                    break  # Encerra a partida

                #TESTA SE O TOTEM VENCEU
                elif acertos_totem == total_alvos:
                    limpar_tela()
                    print()
                    print( "  O TOTEM DESTRUIU TODAS AS SUAS PEÇAS! VOCÊ PERDEU." )
                    print(f"   DERROTA. Pontuação Final: {pontuacao}")
                    print()

                    mod_05_mecanicas.registrar_partida(placar_do_dia,nome,modo,"Derrota",rodadas + 1,pontuacao,)

                    input("Pressione [enter] para ver o resumo...")
                    limpar_tela()
    
                    mod_05_mecanicas.exibir_resumo_partida("Derrota", rodadas + 1, nome,matriz_real_totem,matriz_rastreio_totem, matriz_real_jogador,matriz_rastreio_jogador,usos_olho, pontuacao, tamanho)

                    input("Pressione [enter] para voltar ao menu principal...")
                    break  # Encerra a partida

                rodadas += 1
                input("\nFim do turno. Pressione [enter] para continuar...")
            else:
                print("Opção inválida.")
        

      case"2":# REGRAS DO JOGO
          limpar_tela()
          #EXEBIDNO TEXTO APENAS
          mod_03_regras_jogo.mostrar_regras()

      case"3":#PLACA DO JOGO 
           limpar_tela()
           mod_05_mecanicas.exibir_placar(placar_do_dia)
           input("Pressione [enter] para voltar ao menu principal...")
           
      case"4":# encerrando laço de repetiçao/jogo 
          while True:
           print()
           encerra = input("Confirme o código:")
           input("\nPrecione QUALQUER TECLA para continaur ... . . . . . ")
           limpar_tela()
           if encerra == codigo_encerramento:
               print("Totem encerrado.. . . .")
               break
           else:
               print("\033[31mCódigo inválido.\033[0m");
              
      case _:
          print("\033[31mOPÇÃO INVALIDA escolha opoção que esta no menu :)\033[0m");
          
