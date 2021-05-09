from models.Procedimento import Procedimento
class ListaProcedimentos:
    def __init__(self):
        self.procedimentos = []

    def novoProcedimento(self):
        self.procedimentos.append(Procedimento(input("Nome: "), input("Valor: "), input("Descrição: "), input("Tempo: ")))

    def listarProcedimentos(self):
        for procedimento in self.procedimentos:
            print(f'-----\nNome: {procedimento.nome}\nValor: {procedimento.valor}\nDescrição: {procedimento.descricao}\nTempo: {procedimento.tempo}')

    def excluirProcedimento(self, nome):
        for procedimento in range(len(self.procedimentos)):
            if self.procedimentos[procedimento].nome == nome:
                self.procedimentos[procedimento].excluirProcedimentossss()
                del(self.procedimentos[procedimento])