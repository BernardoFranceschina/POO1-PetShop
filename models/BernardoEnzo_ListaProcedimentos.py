#Bernardo Carlos Franceschina - 20203080
#Enzo Bassani - 20200398
from models.BernardoEnzo_Procedimento import Procedimento
from helpers.BernardoEnzo_helper import getnum
from datetime import timedelta
class ListaProcedimentos:
    def __init__(self):
        self.procedimentos = []

    def novoProcedimento(self):

        duracao = getnum("Duração(hh:mm): ", 2, 0, [24, 60], separator=":")
        duracao = timedelta(hours = duracao[0], minutes= duracao[1])

        self.procedimentos.append(Procedimento(input("Nome: "), getnum("Valor: ", 1, 0), duracao, input("Descrição: ")))

    def listarProcedimentos(self):
        for procedimento in self.procedimentos:
            print(f'Nome: {procedimento.nome.ljust(20)} | Valor: {str(procedimento.valor).ljust(10)} | Tempo: {procedimento.tempo} | Descrição: {procedimento.descricao}')

    def excluirProcedimento(self, procedimento):
        del(self.procedimentos[procedimento])

    def encontrarProcedimento(self, nome):
        for procedimento in range(len(self.procedimentos)):
            if self.procedimentos[procedimento].nome == nome:
                return procedimento
        return -1