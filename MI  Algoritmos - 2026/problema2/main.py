import os
# importando função em aqruivo fora do arquivo main
import mod_03_regras_jogo 
import mod_02_menus_secundario
import mod_04_matrizes
import mod_05_mecanicas

#Função 
def limpar_tela():#Limpa a tela do terminal de acordo com o sistema operacional
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

#Variaves do programa
codigo_encerramento = 0.0
acertos = 0
erros = 0
casas_cantadas = 0
rodadas = 0
placar_do_dia = []

#CÓDIDO PRINCIPAL

# Essa parte do código utiliza a função isdigit para verificar se todos os caracteres presentes dentro da variável codigo_encerramento são números e, caso não sejam,o while continuará executando...

print("\n[-------Adiministrado do Cuca----------]\n");
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
input("\nPrecione [ENTER] para continaur ... . . . . . ")
limpar_tela()


# Essa parte código  abaixo utiliza  o while e match"case" para manter toda instrutura do jogo rodando em loop que é controlado por um variavel recebida e solicitada ao jogador atraves  do menu e o match case direciona o jagador algumas das opções escolhida do menu...


opcao_menu = 0
while opcao_menu != "3": # laço de repetição que se repeti enquanto a variavel opcao_menu for diferente de 3
  print()
  print("\033[1mBem-vindo GiCanA dOs AtElieS\033[0m".center(50))

  print()
  print("              [1] JOGAR")
  print("              [2] REGRAS")
  print("              [3] SAIR")
  print() 
  opcao_menu = input() # solicitando usuario uma  valor do menu ,nesse momento não utilize try excepet para trata exceçoes de entrada põois macth case esta fazendo isso trazendo um reposta  para qualquer dodo digitado fora dos case especeficos 

  
  match opcao_menu:# caso 1 onde acontece o jogo
      case "1":
        tamanho, nome = mod_02_menus_secundario.escolha_bancada()
        
      
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

         # --- PREPARAÇÃO DAS PEÇAS ---
        print()
        print("--- PREPARAÇÃO DAS PEÇAS ---")
        mod_05_mecanicas.posicionar_pecas_jogador(matriz_real_jogador, tamanho)

        mod_05_mecanicas.posicionar_pecas_automatico(matriz_real_totem, tamanho) 

        # Variáveis da partida (LIMPAS E SEM DUPLICAÇÃO)
        pontuacao = 0
        usos_olho = 3
        rodadas = 0
        lista_vizinhos_totem = [] 
        
        # O laço principal da partida (Substituiu o partida_rodando)
        while True:
            limpar_tela()
            
            print(f"--- PONTUAÇÃO: {pontuacao} ---\n".center(60))

            print("->Bancada Do TOTEM ")
            mod_04_matrizes.mostra_matriz(matriz_rastreio_totem)
            print()
            print("->Bancada Jogador-Play1") 
            mod_04_matrizes.mostra_matriz(matriz_real_jogador)
            
            print("\nSua vez!")
            print("Escolha uma acão\n")
            acao = input(f"[1] Jogar [2] Desistir [3] Olho Clínico ({usos_olho} usos): ")
            
            if acao == '2':
                print("Você desistiu!")
                # Chama o Ranking para salvar a desistência
                mod_05_mecanicas.registrar_partida(placar_do_dia, nome, modo, "Desistência", rodadas, pontuacao)
                
                break
                
            elif acao == '3':
                if usos_olho > 0:
                    usos_olho, pontuacao = mod_05_mecanicas.usar_olho_clinico(matriz_real_totem, usos_olho, pontuacao)
                else:
                    print("Você não tem mais usos do Olho Clínico!")
                input("Pressione [enter] para continuar...")
                continue
                
            elif acao == '1':
                # JOGADA DO JOGADOR
                try:
                    linha = int(input(f"\nLinha=[1 a {tamanho}]: ")) - 1
                    coluna = int(input(f"Coluna=[1 a {tamanho}]: ")) - 1

                    # 1. Checa se a posição está dentro do tabuleiro
                    if 0 <= linha < tamanho and 0 <= coluna < tamanho:

                        # 2. TRAVA DE CASA REPETIDA: Se já tiver 'X' ou 'o', avisa e não gasta o turno
                        if matriz_rastreio_totem[linha][coluna] != " ":
                            print(
                                "\n\033[33mVocê já cantou essa casa antes! Escolha outra posição.\033[0m"
                            )
                            input("Pressione [enter] para tentar de novo...")
                            continue  # Volta para o início do loop sem passar a vez para o Totem

                        # 3. Se a casa for nova, resolve o tiro
                        if matriz_real_totem[linha][coluna] != " ":
                            print("\nBOOOM! Você acertou uma peça!")
                            matriz_rastreio_totem[linha][coluna] = "X"
                            pontuacao += 10
                        else:
                            print("\nÁgua! Não tinha peça aqui.")
                            matriz_rastreio_totem[linha][coluna] = "o"
                            pontuacao = max(0, pontuacao - 5)

                    else:
                        print("\nCoordenada fora da bancada!")
                        input("Pressione [enter] para tentar de novo...")
                        continue  # Não gasta o turno se digitou coordenada fora do tabuleiro

                except ValueError:
                    print("\nEntrada inválida! Digite apenas números.")
                    input("Pressione [enter] para tentar de novo...")
                    continue  # Não gasta o turno se digitou algo errado

                input("\nPressione [enter] para o turno do Totem...")

                #Momento  do toyem (Novato e Veterano)
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
                    print(
                        f"O totem escolheu na casa ({linha_bancada + 1}, {coluna_bancada + 1})!"
                    )

                    # CHECAGEM Só é acerto se NÃO for espaço, NÃO for X e NÃO for o
                    if matriz_real_jogador[linha_bancada][coluna_bancada] not in [" ", "X", "o"]:
                        print("\033[31mO Totem acertou uma peça sua!\033[0m")
                        matriz_rastreio_jogador[linha_bancada][coluna_bancada] = "X"
                        matriz_real_jogador[linha_bancada][coluna_bancada] = "X"
                        
                        if modo == "Veterano":
                            mod_05_mecanicas.adicionar_vizinhos(
                                linha_bancada,
                                coluna_bancada,
                                lista_vizinhos_totem,
                            )
                    else:
                        print("\033[32mO Totem deu água!\033[0m")
                        matriz_rastreio_jogador[linha_bancada][coluna_bancada] = "o"
                        matriz_real_jogador[linha_bancada][coluna_bancada] = "o"
                rodadas += 1
                input("\nFim do turno. Pressione [enter] para continuar...")
            else:
                print("Opção inválida.")
        

      case"2":#caso 2 regras do mjogo
          limpar_tela()
          mod_03_regras_jogo.mostrar_regras()

      case"3":# encerrando laço de repetiçao/jogo 
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
          
