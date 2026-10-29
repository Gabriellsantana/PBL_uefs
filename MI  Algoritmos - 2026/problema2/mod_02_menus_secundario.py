#ARQUIVO IMPORTADO NO ARQUIVO PRINCIPAL main.py
#Arquivo secundário responsável pelos menus de configuração da partida.


def escolha_bancada():#fução determina bancada que jogador que ultlizar 
    # Mantém o menu em repetição para permitir que o jogador corrija
    #uma escolha inválida sem precisar reiniciar o programa.
    while True:
            print("\nEscolha a bancada para partida:")
            print("\n1 - Bancada de ensaio (6x6)")
            print("2 - Bancada de montagem (8x8)")
            print("3 - Bancada de véspera (10x10)\n")
            try:
             escolha = int(input("Opção: ")) # tratando espaço em braco e  especial 
           
             if escolha == 1:
                return 6, "Ensaio"
    
             elif escolha == 2:
                return 8, "Montagem"
    
             elif escolha == 3:
                return 10, "Véspera"
             else:
                print("Não correspodem a umas das opções entre 1 a 3.")
            except ValueError:
             print("Entrada inválida! \033[31mValueError\033[0m. Tente novamente.")

             
def escolher_modo():# Escolehndo modo de jogo advesario no usuario
    while True:
        
        print("\nModo do adversário:")
        print("\n1 - Novato")
        print("2 - Veterano\n")
         # Recebe a opção como texto, evitando conversões desnecessária                 # e removendo espaços que poderiam invalidar uma entrada correta.
        escolha = input("Opção: ").strip()

        if escolha == "1":
            return "Novato"

        elif escolha == "2":
            return "Veterano"

        else:
            print("Opção inválida.")