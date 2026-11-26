# =======================================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 2 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
#========================================================================================




class Transacao:
    def __init__(self, remetente, destinatario, valor):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor


class Participante:
    def __init__(self, id_p, nome):
        self.id = id_p
        self.nome = nome
        self.transacoes = []  

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def pegar_transacao(self, indice):
        if 0 <= indice < len(self.transacoes):
            return self.transacoes[indice]
        return None


class Sistema:
    def __init__(self):
        self.participantes = {}  # Dicionário -> chave: id, valor: objeto Participante
        self.transacoes = []     # Lista geral de todas as transações

    def cadastrar(self, id_p, nome):
        if id_p in self.participantes or nome == "":
            return False
        self.participantes[id_p] = Participante(id_p, nome)
        return True

    def registrar_transacao(self, id_rem, id_dest, valor):
        if valor <= 0:
            return False
        if id_rem not in self.participantes or id_dest not in self.participantes:
            return False

        nova = Transacao(id_rem, id_dest, valor)
        self.transacoes.append(nova)

        # Adiciona na lista de quem enviou
        self.participantes[id_rem].adicionar_transacao(nova)

        # Adiciona na lista de quem recebeu (só se não for transferência para si mesmo)
        if id_rem != id_dest:
            self.participantes[id_dest].adicionar_transacao(nova)

        return True


# --- MENU PRINCIPAL ---

sistema = Sistema()

while True:
    print("\n--- GAME-CON POCKET ---")
    print("1 - Cadastrar participante")
    print("2 - Registrar transação")
    print("3 - Ver e acessar transações de um participante")
    print("0 - Sair")

    opcao = input("Opção: ")

    match opcao:
        case "1":
            try:
                id_p = int(input("ID numérico: "))
                nome = input("Nome (fictício): ")
                if sistema.cadastrar(id_p, nome):
                    print("Participante cadastrado!")
                else:
                    print("Erro: ID já existe ou nome vazio.")
            except ValueError:
                print("Erro: o ID precisa ser um número inteiro.")

        case "2":
            try:
                id_rem = int(input("ID de quem envia: "))
                id_dest = int(input("ID de quem recebe: "))
                valor = float(input("Valor: "))
                if sistema.registrar_transacao(id_rem, id_dest, valor):
                    print("Transação registrada!")
                else:
                    print("Erro: verifique os IDs e o valor.")
            except ValueError:
                print("Erro: digite apenas números válidos.")

        case "3":
            try:
                id_p = int(input("ID do participante: "))
                if id_p not in sistema.participantes:
                    print("Participante não encontrado.")
                else:
                    p = sistema.participantes[id_p]
                    print(f"\nTransações de {p.nome}:")

                    # Lista todas as transações daquele participante
                    for i in range(len(p.transacoes)):
                        t = p.transacoes[i]
                        print(f"[{i}] De {t.remetente} para {t.destinatario} - R$ {t.valor:.2f}")

                    # Acessa uma transação específica pelo índice
                    if len(p.transacoes) > 0:
                        indice = int(input("Digite o número [indice] da transação para acessar: "))
                        escolhida = p.pegar_transacao(indice)
                        if escolhida is not None:
                            print(f"Acessada -> Remetente: {escolhida.remetente} | Destinatário: {escolhida.destinatario} | Valor: R$ {escolhida.valor:.2f}")
                        else:
                            print("Índice inválido.")
            except ValueError:
                print("Erro: digite um número inteiro.")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida.")