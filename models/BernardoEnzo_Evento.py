#Bernardo Carlos Franceschina - 20203080
#Enzo Bassani - 20200398
from datetime import date, datetime, timedelta
from helpers.BernardoEnzo_helper import getAnswer
from models.BernardoEnzo_ListaProcedimentos import *
class Evento:
    def __init__(self, clienteCPF, cliente, pet, procedimento, valor, dataInicio, dataFim):
        self.cliente = cliente
        self.clienteCPF = clienteCPF
        self.pet = pet
        self.procedimento = procedimento
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.valor = valor

    def printEvento(self, data, hora, detalhes):
        if data:
            print(self.dataInicio.strftime("%d/%m/%y"), end =" ")
        if hora:
            print(self.dataInicio.strftime("%H:%M"), "-", self.dataFim.strftime("%H:%M"), end =" ")
        print("| Procedimento:", self.procedimento.ljust(20), end =" ")
        if detalhes:
            print("| Nome:", self.cliente.ljust(32), "CPF:", str(self.clienteCPF).ljust(11), "| Animal:", self.pet.ljust(20), end =" ")
        print()

    def editarEvento(self, clientes, procedimentos, agenda, eventoIndex):
        print("Insira 0 a qualquer momento para cancelar e voltar")
        option = input("Qual informação deseja editar?\n1) Cliente e animal\n2) Procedimento\n3) Data\n")
        if (option == '1'):
            while True:                                                                                 
                nome = input("Nome/CPF do cliente: ")
                if nome == '0':
                    return
                cliente = clientes.encontrarCliente(nome)
                if cliente == -1:
                    print("Cliente não encontrado.")
                    if getAnswer("Deseja ver a lista de clientes e seus animais?(S/N) ") == 'S':
                        clientes.printLista(False, True)
                    continue
                break
         
            while True:
                clientes.clientes[cliente].printData(False, True)
                nome = input("Nome do animal: ").capitalize()
                if nome == '0':
                    return

                animalNome = -1
                for animal in range(len(clientes.clientes[cliente].pets)):
                    if clientes.clientes[cliente].pets[animal].nome == nome:
                        animalNome = clientes.clientes[cliente].pets[animal].nome
                if animalNome == -1:
                    print("Animal não encontrado")
                    continue
                break

            self.clienteCPF = clientes.clientes[cliente].cpf
            self.cliente = clientes.clientes[cliente].nome
            self.pet = animalNome
        elif(option == '2'):
            while True:
                nome = input("Procedimento: ")
                if nome == "0":
                    return

                procedimentoIndex = procedimentos.encontrarProcedimento(nome)
                if procedimentoIndex == -1:
                    print("Procedimento não encontrado")
                    if getAnswer("Deseja ver a lista de procedimentos?(S/N) ") == 'S':
                        procedimentos.listarProcedimentos()
                    continue
                break

            self.procedimento = procedimentos.procedimentos[procedimentoIndex].nome
            self.valor = procedimentos.procedimentos[procedimentoIndex].valor
            self.dataFim = self.dataInicio + procedimentos.procedimentos[procedimentoIndex].tempo     
        elif(option == '3'):
            print(f'Data anterior: {self.dataInicio.strftime("%d/%m/%y")}')
            while True:
                data = input("Nova data e o horário no formato (dd/mm/aa hh:mm): ")
                if data == 0:
                    return
                try:
                    data = datetime.strptime(data, "%d/%m/%y %H:%M")
                except:
                    print("Entrada inválida")
                    continue
                break

            duracao = self.dataFim - self.dataInicio
            self.dataInicio = data
            self.dataFim = data + duracao
            agenda.ajustarPosicao(eventoIndex)
        else:
            print("Comando inválido")
