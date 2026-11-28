# =======================================================================================
# UNIVERSIDADE ESTADUAL DE FEIRA DE SANTANA (UEFS)
# CURSO: ENGENHARIA DE COMPUTAÇÃO
# DISCIPLINA: EXA854 - MI ALGORITMOS (PROBLEMA 3 - 2026.2)
# AUTOR: Gabriel Do Nascimento Santana
# DECLARAÇÃO DE AUTORIA: Declaro que este código foi desenvolvido por mim de
# forma individual, respeitando todas as regras de autoria do problema.
# =======================================================================================

import json
import os


# Classe mãe que representa qualquer participante do evento
class Participante:
    def __init__(self, id_participante, nome, tipo="Participante"):
        self.id_participante = id_participante
        self.nome = nome
        self.tipo = tipo

    # Converte o objeto em dicionário para conseguir salvar no arquivo JSON
    def para_dicionario(self):
        return {"id_participante": self.id_participante,"nome": self.nome,"tipo": self.tipo}

    # Define como o participante aparece quando usamos print()
    def __str__(self):
        return f"ID: {self.id_participante} | Nome: {self.nome} ({self.tipo})"


# Classe filha que herda atributos e métodos de Participante
class Visitante(Participante):
    def __init__(self, id_participante, nome):
        super().__init__(id_participante, nome, "Visitante")


# Classe filha que herda atributos e métodos de Participante
class Expositor(Participante):
    def __init__(self, id_participante, nome):
        super().__init__(id_participante, nome, "Expositor")


# Classe que representa uma transferência financeira entre participantes
class Transacao:
    def __init__(self, pagante, recebedor, valor):
        self.pagante = pagante        # ID de quem envia o dinheiro
        self.recebedor = recebedor    # ID de quem recebe o dinheiro
        self.valor = valor            # Valor numérico maior que zero

    # Verifica se um participante participou desta transação (enviando ou recebendo)
    def envolve_usuario(self, id_participante):
        return self.pagante == id_participante or self.recebedor == id_participante

    # Verifica se o remetente é igual ao destinatário (operação de conferência)
    def eh_autotransferencia(self):
        return self.pagante == self.recebedor

    # Converte o objeto em dicionário para salvar no arquivo JSON
    def para_dicionario(self):
        return {
            "pagante": self.pagante,"recebedor": self.recebedor,"valor": self.valor}

    def __str__(self):
        return f"De ID {self.pagante} para ID {self.recebedor} | Valor: R$ {self.valor:.2f}"


# Classe principal que controla cadastros, transações, consultas e arquivos
class Sistema:
    def __init__(self):
        self.participantes = {}  # Dicionário: chave = ID (int), valor = objeto Participante
        self.transacoes = []     # Lista que guarda os objetos Transacao
        self.arq_participantes = "participantes.json"
        self.arq_transacoes = "transacoes.json"

    # CADASTRO E CONSULTA DE PARTICIPANTES 

    def cadastrar_usuario(self, id_participante, nome, tipo):
        # Exige ID numérico maior que zero
        if id_participante <= 0:
            return False, "Erro: o ID deve ser maior que zero."

        # Impede cadastro duplicado sem sobrescrever quem já existe
        if id_participante in self.participantes:
            return False, "Erro: já existe um participante com esse ID."

        # Impede nome vazio ou com números/símbolos
        nome_limpo = nome.strip()
        if nome_limpo == "" or not nome_limpo.replace(" ", "").isalpha():
            return False, "Erro: o nome deve conter apenas letras sem números."

        # Cria o objeto da classe filha escolhida
        if tipo == "2":
            novo = Expositor(id_participante, nome_limpo)
        else:
            novo = Visitante(id_participante, nome_limpo)

        # Salva no dicionário e grava no arquivo JSON
        self.participantes[id_participante] = novo
        self.salvar_dados()
        return True, "Participante cadastrado com sucesso!"

    # Busca um participante pelo ID no dicionário
    def buscar_usuario(self, id_participante):
        if id_participante in self.participantes:
            return self.participantes[id_participante]
        return None

    # Retorna uma lista com todos os participantes em ordem numérica crescente de ID
    def listar_usuarios(self):
        ids = list(self.participantes.keys())
        ids.sort()  # Ordena os números inteiros ex: ID 2 vem antes do ID 10

        lista_ordenada = []
        for id_p in ids:
            lista_ordenada.append(self.participantes[id_p])
        return lista_ordenada

    #REGISTRO E LISTAGEM DE TRANSAÇÕES 

    def registrar_transacao(self, pagante, recebedor, valor):
        # Recusa valores menores ou iguais a zero
        if valor <= 0:
            return False, "Erro: o valor da transferência deve ser maior que zero."

        # Exige que remetente e destinatário estejam cadastrados
        if pagante not in self.participantes:
            return False, "Erro: o remetente não está cadastrado."

        if recebedor not in self.participantes:
            return False, "Erro: o destinatário não está cadastrado."

        # Permite pagante == recebedor autotransferência
        nova = Transacao(pagante, recebedor, valor)
        self.transacoes.append(nova)
        self.salvar_dados()
        return True, "Transação registrada com sucesso!"

    def listar_transacoes(self):
        return self.transacoes

    # HISTÓRICO, VOLUME FINANCEIRO E FREQUÊNCIA 

    # Retorna todas as transações de um usuário sem repetir autotransferência
    def consultar_historico(self, id_participante):
        historico = []
        for t in self.transacoes:
            if t.envolve_usuario(id_participante):
                historico.append(t)
        return historico

    # Apura separadamente o total enviado e o total recebido por participante
    def calcular_volume(self, id_participante):
        total_enviado = 0.0
        total_recebido = 0.0

        for t in self.transacoes:
            # Dois 'if' separados garantem que na autotransferência o valor
            # entre uma vez no total enviado e uma vez no total recebido
            if t.pagante == id_participante:
                total_enviado += t.valor
            if t.recebedor == id_participante:
                total_recebido += t.valor

        return total_enviado, total_recebido

    # Filtra participantes com transações >= limite em ordem numérica crescente de ID
    def filtrar_por_minimo(self, limite):
        contagem = {}
        for id_p in self.participantes:
            contagem[id_p] = 0

        for t in self.transacoes:
            # Conta 1 participação para quem enviou
            if t.pagante in contagem:
                contagem[t.pagante] += 1

            # Só conta para quem recebeu se não for autotransferência (conta 1 vez)
            if not t.eh_autotransferencia():
                if t.recebedor in contagem:
                    contagem[t.recebedor] += 1

        ids_aprovados = []
        for id_p in contagem:
            if contagem[id_p] >= limite:
                ids_aprovados.append(id_p)

        ids_aprovados.sort()  # Ordena os IDs numericamente

        resultado = []
        for id_p in ids_aprovados:
            resultado.append([self.participantes[id_p], contagem[id_p]])
        return resultado

    #PERSISTÊNCIA EM JSON 

    def salvar_dados(self):
        try:
            lista_part = []
            for p in self.participantes.values():
                lista_part.append(p.para_dicionario())

            with open(self.arq_participantes, "w", encoding="utf-8") as arq_p:
                json.dump(lista_part, arq_p, indent=4, ensure_ascii=False)

            lista_trans = []
            for t in self.transacoes:
                lista_trans.append(t.para_dicionario())

            with open(self.arq_transacoes, "w", encoding="utf-8") as arq_t:
                json.dump(lista_trans, arq_t, indent=4, ensure_ascii=False)

        except OSError as erro:
            print(f"Erro ao salvar os arquivos: {erro}")

    def carregar_dados(self):
        # 1. Carrega participantes (funciona sem arquivo ou com arquivo vazio)
        try:
            with open(self.arq_participantes, "r", encoding="utf-8") as arq_p:
                conteudo = arq_p.read().strip()

            if conteudo != "":
                dados = json.loads(conteudo)
                for item in dados:
                    id_p = int(item["id_participante"])
                    nome = str(item["nome"])
                    tipo = item["tipo"]

                    if tipo == "Expositor":
                        self.participantes[id_p] = Expositor(id_p, nome)
                    else:
                        self.participantes[id_p] = Visitante(id_p, nome)

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, ValueError, KeyError, TypeError):
            backup = self.arq_participantes + ".backup"
            if os.path.exists(self.arq_participantes):
                os.replace(self.arq_participantes, backup)
            print(f"Aviso: '{self.arq_participantes}' inválido. Backup salvo em '{backup}'.")

        # 2. Carrega transações (funciona sem arquivo ou com arquivo vazio)
        try:
            with open(self.arq_transacoes, "r", encoding="utf-8") as arq_t:
                conteudo = arq_t.read().strip()

            if conteudo != "":
                dados = json.loads(conteudo)
                for item in dados:
                    pagante = int(item["pagante"])
                    recebedor = int(item["recebedor"])
                    valor = float(item["valor"])

                    self.transacoes.append(Transacao(pagante, recebedor, valor))

        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, ValueError, KeyError, TypeError):
            backup = self.arq_transacoes + ".backup"
            if os.path.exists(self.arq_transacoes):
                os.replace(self.arq_transacoes, backup)
            print(f"Aviso: '{self.arq_transacoes}' inválido. Backup salvo em '{backup}'.")