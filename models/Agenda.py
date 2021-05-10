from models.Evento import *
from datetime import datetime, timedelta
from models.ListaClientes import ListaClientes
from models.Cliente import Cliente
from helpers.helper import getnum, getAnswer
from models.ListaProcedimentos import *

class Agenda:
    def __init__(self):
        self.agenda = []

    def novoEvento(self, clientes, procedimentos):
        print("\nInsira 0 para cancelar a qualquer momento")

        #Pega o ID do cliente
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
            clienteID = clientes.clientes[cliente].id_cliente
            break

        #Pega o ID do animal
        while True:
            clientes.clientes[cliente].printData(False, True)
            nome = input("Nome do animal: ")
            if nome == '0':
                return

            animalID = -1
            for animal in range(len(clientes.clientes[cliente].pets)):
                if clientes.clientes[cliente].pets[animal].nome == nome:
                    animalID = clientes.clientes[cliente].pets[animal].id_pet
            if animalID == -1:
                print("Animal não encontrado")
                continue
            break

        #Pega a data
        while True:
            data = input("Data e o horário no formato (dd/mm/aa hh:mm): ")
            if data == 0:
                return
            try:
                data = datetime.strptime(data, "%d/%m/%y %H:%M")
            except:
                print("Entrada inválida")
                continue
            break
        
        #Pega o procedimento e a sua duração
        while True:
            nome = input("Procedimento: ")
            if nome == "0":
                return


            procedimentoID = -1
            for procedimento in range(len(procedimentos.procedimentos)):
                if procedimentos.procedimentos[procedimento].nome == nome:
                    procedimentoID = procedimentos.procedimentos[procedimento].id_procedimento
                    duracao = procedimentos.procedimentos[procedimento].tempo
            if procedimentoID == -1:
                print("Procedimento não encontrado")
                procedimentos.procedimentos.listarProcedimentos
                continue
            break
        
        posicao = self.encontrarPosicao(data)
        if posicao == -1:
            self.agenda.append(Evento(clienteID, animalID, procedimentoID, data, data + duracao))
        else:
            self.agenda.insert(posicao, Evento(clienteID, animalID, procedimentoID, data, data + duracao))

    def encontrarPosicao(self, data):
        for posicao in range(len(self.agenda)):
            if data < self.agenda[posicao].dataInicio:
                return posicao
        return -1