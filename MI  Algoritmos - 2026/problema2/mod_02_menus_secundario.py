#arquivo  secundario que sera chamado no arquivo principal cotendo fuções que projeta interface de menus secundario para nivel do jogo no codigo principal


def escolha_bancada():#fução determina bancada que jogador que ultlizar 
    while True:
            print("\nEscolha a bancada para partida:")
            print("\n1 - Bancada de ensaio (6x6)")
            print("2 - Bancada de montagem (8x8)")
            print("3 - Bancada de véspera (10x10)\n")
    
            escolha = input("Opção: ").strip()
    
            if escolha == "1":
                return 6, "Ensaio"
    
            elif escolha == "2":
                return 8, "Montagem"
    
            elif escolha == "3":
                return 10, "Véspera"

            else:
                print("Opção inválida.")

def escolher_modo():# modo de jogo
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