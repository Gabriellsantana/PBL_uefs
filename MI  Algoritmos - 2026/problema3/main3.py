# =======================================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 2 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
#========================================================================================

#importando classes e modelos de dados
from modelos import Transacao, Participante, Sistema







#programa principal

op = -1
while op!= 0:
    print("\nGAME-CON BAHIA POCKET - SISTEMA DE PAGAMENTOS\n")
    print(""" 
    [1] Cadastrar participante
    [2] Registrar transferência
    [3] Consultar histórico e volume de um participante
    [4] Listar participantes por mínimo de transações
    [5] Listar todos os participantes cadastrados
    [6] Listar todas as transações registradas
    [0] Sair sistema\n   """)
    n = input("Digite opção desejada: ")
    