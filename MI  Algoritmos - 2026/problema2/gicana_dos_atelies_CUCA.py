import os

codigo_encerramento = 0.0


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
    codigo_encerramento  = input("CRIE NOVAMENTE CÓDIGO: ");
    os.system("cls")
# Informa que o código foi aceito
print("\033[32mCódigo registrado com sucesso\033[0m")
# Pausa o programa até o usuário pressionar ENTER
input("\nPrecione [ENTER] para continaur ... . . . . . ")
os.system("cls")



print("\033[1mBem-vindo GiCanA dOs AtElieS\033[0m".center(50))

print()
print("              [1] JOGAR")
print("              [2] OPÇÕES")
print("              [3] SAIR")
print()
