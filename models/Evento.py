from datetime import date, timedelta
class Evento:
    def __init__(self, clienteCPF, cliente, pet, procedimento, dataInicio, dataFim):
        self.cliente = cliente
        self.clienteCPF = clienteCPF
        self.pet = pet
        self.procedimento = procedimento
        self.dataInicio = dataInicio
        self.dataFim = dataFim

    def printEvento(self, data, hora, detalhes):
        if data:
            print(self.dataInicio.strftime("%d/%m/%y"), end =" ")
        if hora:
            print(self.dataInicio.strftime("%H:%M"), end =" ")
        if detalhes:
            print("| Nome:", self.cliente, "CPF:", self.clienteCPF, "| Animal:", self.pet, end =" ")
        
        print("| Procedimento", self.procedimento)