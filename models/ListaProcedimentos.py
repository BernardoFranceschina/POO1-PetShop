from models.Procedimento import Procedimento
from helpers.helper import getnum
from datetime import timedelta
class ListaProcedimentos:
    def __init__(self):
        self.procedimentos = []

    def novoProcedimento(self):

        duracao = getnum("Duração(hh:mm): ", 2, 0, [24, 60], separator=":")
        duracao = timedelta(hours = duracao[0], minutes= duracao[1])

        self.procedimentos.append(Procedimento(input("Nome: "), input("Valor: "), duracao, input("Descrição: ")))

    def listarProcedimentos(self):
        for procedimento in self.procedimentos:
            print(f'-----\nNome: {procedimento.nome} | Valor: {procedimento.valor} | Descrição: {procedimento.descricao} | Tempo: {procedimento.tempo}')

    def excluirProcedimento(self, procedimento):
        del(self.procedimentos[procedimento])

    def encontrarProcedimento(self, nome):
        for procedimento in range(len(self.procedimentos)):
            if self.procedimentos[procedimento].nome == nome:
                return procedimento
        return -1