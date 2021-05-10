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

        #Pega o CPF do cliente e o nome
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
            clienteCPF = clientes.clientes[cliente].cpf
            clienteNome = clientes.clientes[cliente].nome
            break

        #Pega o nome do animal
        while True:
            clientes.clientes[cliente].printData(False, True)
            nome = input("Nome do animal: ")
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


            procedimentoNome = -1
            for procedimento in range(len(procedimentos.procedimentos)):
                if procedimentos.procedimentos[procedimento].nome == nome:
                    procedimentoNome = procedimentos.procedimentos[procedimento].nome
                    duracao = procedimentos.procedimentos[procedimento].tempo
            if procedimentoNome == -1:
                print("Procedimento não encontrado")
                if getAnswer("Deseja ver a lista de procedimentos?(S/N) ") == 'S':
                    procedimentos.listarProcedimentos()
                continue
            break
        
        posicao = self.encontrarPosicao(data)
        if posicao == -1:
            self.agenda.append(Evento(clienteCPF, clienteNome, animalNome, procedimentoNome, data, data + duracao))
        else:
            self.agenda.insert(posicao, Evento(clienteCPF, clienteNome, animalNome, procedimentoNome, data, data + duracao))

    def encontrarPosicao(self, data):
        for posicao in range(len(self.agenda)):
            if data < self.agenda[posicao].dataInicio:
                return posicao
        return -1
    
    def selecionarEvento(self, clientes):
        print("Insira 0 a qualquer momento para voltar")
        while True:
            data = input("Data do evento (dd/mm/aa): ")
            if data == "0":
                return
            try:
                data = datetime.strptime(data, "%d/%m/%y")
            except:
                print("Entrada inválida")
                continue
            break
        data = data.date()
        eventos = []
        for eventoIndex in range(len(self.agenda)):
            if self.agenda[eventoIndex].dataInicio.date() == data:
                eventos.append(eventoIndex)
            if self.agenda[eventoIndex].dataInicio.date() > data:
                break
        if eventos == []:
            print("Nenhum evento encontrado")
            return -1
        
        print("Selecione um dos seguintes eventos:")
        for i in range(len(eventos)):
            print(f"{i + 1}: ", end='')
            self.agenda[eventos[i]].printEvento(False, True, True)

        return eventos[int(getAnswer("\n", [str(x) for x in range(1, len(eventos) + 1)])) - 1]