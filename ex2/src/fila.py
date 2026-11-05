
# classe fila
# emitir(tipo): tipo "normal" ou "prioritaria"; outro tipo lança
# ValueError
# Devolve a senha, numerada por tipo: N1, N2, . . . e P1, P2, . . .
# aguardando: quantas senhas esperam atendimento
# chamar(): devolve a próxima senha; fila vazia lança IndexError

# Prioritária passa na frente; dentro de cada tipo
#     vale a ordem de chegada

# Depois de 2 prioritárias seguidas, se houver normal esperando,
#     a fila chama uma normal


class Fila:
    def __init__(self):
        self.lista_prioritaria = []
        return

    def emitir(self, tipo):
        if tipo == "prioritaria":
            senha = "P" + str(len(self.lista_prioritaria) + 1)
            self.lista_prioritaria.append(senha)
            return senha

    def chamar(self):
        raise IndexError

    @property
    def aguardando(self):
        return len(self.lista_prioritaria)
