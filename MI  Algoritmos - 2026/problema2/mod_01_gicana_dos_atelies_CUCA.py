import os
import mod_03_funcao_regras_jogo # importando função em aqruivo de funcao_regras_jogo.py secundario 
import mod_02_menus_secundario
import mod_04_matrizes

#Função programa principal

def limpar_tela():#Limpa a tela do terminal de acordo com o sistema operacional
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



#Variaves do programa
codigo_encerramento = 0.0
opcao_menu = 0
acertos = 0
erros = 0
casas_cantadas = 0
rodadas = 0


# O que essa parte faz?
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


# Essa parte do código  abaixo utiliza  o while e match"case" para manter toda instrutura do jogo rodando em loop que é controlado por um variavel recebida e solicitada ao jogador atrsvaes do menu e o match case direciona o jagador algumas das opções escolhida do menu...

while opcao_menu != "3": # laço de repetição que se repeti até que o 3 seja digitado
  print()
  print("\033[1mBem-vindo GiCanA dOs AtElieS\033[0m".center(50))

  print()
  print("              [1] JOGAR")
  print("              [2] REGRAS")
  print("              [3] SAIR")
  print() 
  opcao_menu = input() # solicitando usuario uma  valor do menu

  
  match opcao_menu:
      case"1":
        tamanho, nome = mod_02_menus_secundario.escolha_bancada() #Chamada de Função
        matriz = mod_04_matrizes.criar_matriz(tamanho)  #Chamada de Função

        print(f"\nBancada escolhida: {nome}")
        print(f"Tamanho: {tamanho}x{tamanho}")
    
        modo = mod_02_menus_secundario.escolher_modo() #Chamada de Função
      
        input("\nPrecione [enter] para continaur ... . . . . . \n")
        mod_04_matrizes.mostra_matriz(matriz)  #Chamada de Função
        

      case"2":
          limpar_tela()
          mod_03_funcao_regras_jogo.mostrar_regras()
      case"3":
          while True:
           print()
           encerra = input("Confirme o código:")
           input("\nPrecione QUALQUER TECLA para continaur ... . . . . . ")
           limpar_tela()
           if encerra == codigo_encerramento:
               print("Totem encerrado.. . . .")
           else:
               print("\033[31mCódigo inválido.\033[0m");
              
      case _:
          print("\033[31mOPÇÃO INVALIDA escolha opoção que esta no menu :)\033[0m");
          
