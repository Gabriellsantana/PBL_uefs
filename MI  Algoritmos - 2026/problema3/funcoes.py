# =======================================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 3 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
# =======================================================================================


# Le um número inteiro e repete caso o usuário digite letras ou símbolos
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


# Le um número decimal e repete caso o usuário digite texto inválido
def ler_float(mensagem):
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            return float(texto)
        except ValueError:
            print("Entrada inválida! Digite um valor numérico válido (ex: 50.00).")


# Le um nome e repete caso o usuário digite números ou deixe vazio
def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome != "" and nome.replace(" ", "").isalpha():
            return nome
        print("Entrada inválida! Digite um nome usando apenas letras (sem números).")


# Busca o nome de um participante pelo ID para exibir nas listagens
def buscar_nome(sistema, id_participante):
    usuario = sistema.buscar_usuario(id_participante)
    if usuario is not None:
        return usuario.nome
    return "Desconhecido"


# Opção [1]: Pede os dados do participante e envia para o sistema cadastrar
def cadastrar(sistema):
    print("\n--- CADASTRAR PARTICIPANTE ---")
    id_p = ler_inteiro("Digite o ID numérico: ")
    nome = ler_nome("Digite o nome (fictício): ")
    tipo = input("Você é: [1] Visitante  [2] Expositor: ").strip()

    if tipo != "1" and tipo != "2":
        print("Erro: escolha 1 para Visitante ou 2 para Expositor.")
        return

    sucesso, mensagem = sistema.cadastrar_usuario(id_p, nome, tipo)
    print(mensagem)


# Opção [2]: Pede os dados da transferência e envia para o sistema registrar
def registrar_transferencia(sistema):
    print("\n REGISTRAR TRANSFERÊNCIA $ \n")
    pagante = ler_inteiro("ID remetente: ")
    recebedor = ler_inteiro("ID destinatário: ")
    valor = ler_float("Valor da transferência R$: ")

    sucesso, mensagem = sistema.registrar_transacao(pagante, recebedor, valor)
    print(mensagem)


# Opção [3]: Mostra o histórico e os totais enviado/recebido de um participante
def historico_e_volume(sistema):
    print("\n HISTÓRICO E VOLUME FINANCEIRO\n")
    id_p = ler_inteiro("Digite o ID do participante: ")
    participante = sistema.buscar_usuario(id_p)

    if participante is None:
        print("Erro: participante não encontrado.")
        return

    print(f"\nParticipante: {participante}")
    historico = sistema.consultar_historico(id_p)

    if len(historico) == 0:
        print("Nenhuma movimentação registrada para este participante.")
    else:
        print("Transações realizadas:")
        for i in range(len(historico)):
            t = historico[i]
            nome_pag = buscar_nome(sistema, t.pagante)
            nome_rec = buscar_nome(sistema, t.recebedor)

            if t.eh_autotransferencia():
                tipo_op = "Conferência"
            elif t.pagante == id_p:
                tipo_op = "Enviada"
            else:
                tipo_op = "Recebida"

            print(
                f"  [{i + 1}] {tipo_op} | De: {t.pagante} ({nome_pag}) "
                f"-> Para: {t.recebedor} ({nome_rec}) | R$ {t.valor:.2f}"
            )

    enviado, recebido = sistema.calcular_volume(id_p)
    print(f"\nTotal enviado:  R$ {enviado:.2f}")
    print(f"Total recebido: R$ {recebido:.2f}")


# Opção [4]: Lista em ordem crescente de ID quem atingiu o mínimo de transações
def filtrar_participantes(sistema):
    print("\n FILTRAR POR MÍNIMO DE TRANSAÇÕES \n")
    limite = ler_inteiro("Quantidade mínima de transações: ")

    if limite < 0:
        print("Erro: o limite mínimo não pode ser negativo.")
        return

    encontrados = sistema.filtrar_por_minimo(limite)

    if len(encontrados) == 0:
        print(f"Nenhum participante atingiu o mínimo de {limite} transação(ões).")
        return

    print(f"\nParticipantes com pelo menos {limite} transação(ões):")
    for item in encontrados:
        participante = item[0]
        qtd = item[1]
        print(f"  {participante} | Participações: {qtd}")


# Opção [5]: Lista todos os participantes cadastrados
def listar_participantes(sistema):
    print("\nPARTICIPANTES CADASTRADOS\n")
    lista = sistema.listar_usuarios()

    if len(lista) == 0:
        print("Nenhum participante cadastrado ainda.")
        return

    for participante in lista:
        print(f"  {participante}")


# Opção [6]: Lista todas as transações registradas no evento
def listar_transacoes(sistema):
    print("\n--- TODAS AS TRANSAÇÕES REGISTRADAS ---")
    lista = sistema.listar_transacoes()

    if len(lista) == 0:
        print("Nenhuma transação registrada ainda.")
        return

    for i in range(len(lista)):
        t = lista[i]
        nome_pag = buscar_nome(sistema, t.pagante)
        nome_rec = buscar_nome(sistema, t.recebedor)

        print(
            f"  [{i + 1}] Remetente: {t.pagante} ({nome_pag}) -> "
            f"Destinatário: {t.recebedor} ({nome_rec}) | Valor: R$ {t.valor:.2f}"
        )