#ARQUIVO IMPORTADO NO ARQUIVO PRINCIPAL main.py

def mostrar_regras():
    print("\n" + "-" * 60)
    print("                REGRAS - GINCANA DOS ATELIÊS")
    print("-" * 60)

    print()
    print("           1. Você escolhe uma das três bancadas.")
    print("                2. Você posiciona suas peças.")
    print("       3. O totem posiciona as peças dele automaticamente.")
    print("           4. Você e o totem jogam alternadamente.")
    print("        5. Você deve descobrir todas as peças do totem.")
    print("            6. O totem tenta descobrir suas peças.")
    print("                       7. Acerto = X.")
    print("                        8. Erro = o.")
    print("          9. Repetir uma casa não vale como jogada.")
    print("       10. O olho clínico mostra quantas casas com peça")
    print("      existem no quadrado 3x3 ao redor da casa escolhida.")
    print()

    print("PONTUAÇÃO")
    print("+10 por casa com peça descoberta")
    print("-5 por casa vazia")
    print("+50 por peça completada")
    print("-30 por olho clínico")
    print("+200 por vitória")
    print("A pontuação mínima é 0.")

def legenda_indices():
     print("\nDica: A posição inicial define onde a peça começa. Na Vertical (V), ela se estende para baixo; na Horizontal (H), para a direita\n")
     print("Escolha a posição inicial com cuidado e verifique se a peça não vai ultrapassar a borda ao ficar deitada ou em pé.\n")
     
def legendas_posição ():
     print("H = Horizontal (deitada na linha)")
     print("V = Vertical (em pé na coluna)\n")

def legendas_acerto_erros():
     print("\nDica: Acerto: x  Erro (Água): o   Pode ser atacada: [ ] \n")