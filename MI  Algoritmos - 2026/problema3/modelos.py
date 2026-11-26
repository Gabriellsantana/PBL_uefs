#ARQUIVO DE CLASSES E MODELOS DE DADOS

#Class

## Molde supremo para criar os particpantes  (visitantes ou expositores)
class Participante:
    def __init__(self, id_participante, nome):
        self.id_participante = id_participante
        self.nome = nome
    # Mostra o participante
    def __str__(self):
        return f"ID: {self.id_participante}  Nome: {self.nome}"

class Visitante(Participante):
    pass  # herda tudo da class Partcipante 
class Expositor(Participante):
    pass  # herda tudo da class Partcipante 
    

class Transacao:
    def __init__(self, pagante, recebedor, valor):
        self.pagante = pagante
        self.recebedor = recebedor
        self.valor = valor

class Sistema:
    def __init__(self):
        self.participantes = []
        self.transacoes = []

    def cadastrar_usuario(self, id_participante, nome):
        novo_participante = Participante(id_participante, nome)
        self.participantes.append(novo_participante)

    def registrar_transacao(self, remetente, destinatario, valor):
        nova_transacao = Transacao(remetente, destinatario, valor)
        self.transacoes.append(nova_transacao)