from models.Trabalho import *
class Agenda:
    def __init__(self):
        self.trabalhos = []

    def novoTrabalho(self, fk_id_pet, data, horario, procedimento):
        self.trabalhos.append(Trabalho(fk_id_pet, data, horario, procedimento))

##    def excluirTrabalho(self, horario):
        #fazer