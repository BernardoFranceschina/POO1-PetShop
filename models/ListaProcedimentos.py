from models.Procedimento import Procedimento
class ListaProced:
    def __init__(self):
        self.proced = []

    def novoProced(self, nome, valor, tempo, descricao):
        self.proced.append(Procedimento(nome, valor, tempo, descricao))

##    def excluirProced(self, idnome):
        #fazer -- permitir pesquisa por ID ou por Nome, identificando qual deles o usuário usou como entrada