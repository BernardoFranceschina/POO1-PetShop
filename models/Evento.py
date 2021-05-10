from datetime import date, timedelta
class Evento:
    def __init__(self, fk_id_cliente, fk_id_pet, fk_id_procedimento, dataInicio, dataFim):
        self.fk_id_pet = fk_id_pet
        self.fk_id_cliente = fk_id_cliente
        self.fk_id_procedimento = fk_id_procedimento
        self.dataInicio = dataInicio
        self.dataFim = dataFim


##    def editar(self):
        #Fazer