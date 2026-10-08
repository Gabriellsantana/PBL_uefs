import os
from funcao_regras_jogo import mostrar_regras # importando função em aqruivo de funcao_regras_jogo.py secundario 

# ===========================================================================
#funçes e modularização do sistema:

def limpar_tela():#Limpa a tela do terminal de acordo com o sistema operacional
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ===========================================================================
#Variaves do programa
codigo_encerramento = 0.0
opcao_menu = 0

# ===========================================================================
# O que essa parte faz?
# Essa parte do código utiliza a função isdigit para verificar se todos os caracteres presentes dentro da variável codigo_encerramento são números e, caso não sejam,o while continuará executando...

print("\n[-------Adiministrado do Cuca----------]\n");
print("CRIE O CÓDIGO DE ENCERRAMENTO: ",end="");
# Pede ao usuário para criar um código de encerramento
codigo_encerramento = input();
# Continua pedindo o código enquanto ele não tiver apenas números
while not codigo_encerramento.isdigit():
    # Informa ao usuário que o código digitado é inválido
    print("\033[31mCódigo inválida. Digite apenas números.\033[0m");
     # Pede um novo código
    codigo_encerramento  = input("\nCRIE NOVAMENTE CÓDIGO: ");
    limpar_tela()
# Informa que o código foi aceito
print("\033[32mCódigo registrado com sucesso\033[0m")
# Pausa o programa até o usuário pressionar ENTER
input("\nPrecione [ENTER] para continaur ... . . . . . ")
limpar_tela()


while opcao_menu != "3": # laço de repetição para todo menu todo jogo
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
          print("ate aqui ok")
      case"2":
          limpar_tela()
          mostrar_regras()
      case"3":
          print("Totem encerrado.. . . .")
      case _:
          print("\033[31mOPÇÃO INVALIDA escolha opoção que esta no menu :)\033[0m");
          
