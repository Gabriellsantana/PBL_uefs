# =======================================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 3 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
# =======================================================================================

from modelos import Sistema
import funcoes
import os

# Cria o objeto principal do sistema e carrega os arquivos JSON anteriores
sistema = Sistema()
sistema.carregar_dados()


# Limpa a tela do terminal de acordo com o sistema operacional
def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


opcao = ""
# Laço principal que mantém o menu funcionando até o operador escolher sair com valor 0
while opcao != "0":
    print("\n   GAME-CON BAHIA POCKET - SISTEMA DE PAGAMENTOS\n")

    print("  [1] Cadastrar participante")
    print("  [2] Fazer transferência [$]")
    print("  [3] Consultar histórico de um participante")
    print("  [4] Listar participantes por mínimo de transações")
    print("  [5] Listar todos usuarios cadastrados")
    print("  [6] Listar todas as transações já registradas")
    print("  [0] Sair do sistema\n")
    opcao = input("Digite a opção desejada: ").strip()

    limpar_tela()
    match opcao:
        case "1":
            funcoes.cadastrar(sistema)
        case "2":
            funcoes.registrar_transferencia(sistema)
        case "3":
            funcoes.historico_e_volume(sistema)
        case "4":
            funcoes.filtrar_participantes(sistema)
        case "5":
            funcoes.listar_participantes(sistema)
        case "6":
            funcoes.listar_transacoes(sistema)
        case "0":
            sistema.salvar_dados()
            print("Dados salvos. Encerrando o sistema...")
            break
        case _:
            print("Opção inválida! Digite um número de 0 a 6.")