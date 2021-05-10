from datetime import date, datetime, timedelta
from models.ListaProcedimentos import *
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

    def excluirEvento(self):
        del self

    def editarEvento(self):
        option = input("Qual informação deseja editar?\n1) Cliente e animal\n2) Procedimento\n3) Data")
        if (option == '1'):
            print()
        elif(option == '2'):
            print()
        elif(option == '3'):
            while True:
                print(f'Data anterior: {self.dataInicio}')
                data = input("Data e o horário no formato (dd/mm/aa hh:mm): ")
                if data == 0:
                    return
                try:
                    data = datetime.strptime(data, "%d/%m/%y %H:%M")
                    self.dataInicio = data
                    # indexProcedimento = encontrarProcedimento(self.procedimento)         Pegar o procedimento para poder definir data final
                    self.dataFim = data+
                except:
                    print("Entrada inválida")
                    continue
                break
