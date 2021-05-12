from models.Evento import *
from datetime import datetime, timedelta
from models.ListaClientes import ListaClientes
from models.Cliente import Cliente
from helpers.helper import *
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

        #Pega a data
        data = getData("Data e o horário no formato (dd/mm/aa hh:mm): ", True)
        if data == -1:
            return
        
        #Pega o procedimento e a sua duração
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
        procedimentoNome = procedimentos.procedimentos[procedimentoIndex].nome
        duracao = procedimentos.procedimentos[procedimentoIndex].tempo
        
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
    
    def ajustarPosicao(self, eventoIndex):
        evento = self.agenda[eventoIndex]
        self.agenda.pop(eventoIndex)

        novaPosicao = self.encontrarPosicao(evento.dataInicio)
        if novaPosicao == -1:
            self.agenda.append(evento)
        else:
            self.agenda.insert(novaPosicao, evento)

        

    def selecionarEvento(self):
        print("Insira 0 a qualquer momento para voltar")

        data = getData("Data do evento (dd/mm/aa): ", False)
        if data == -1:
            return
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

    def printAgenda(self, inicio, fim):
        periodo = False #Determina se o looping for está passando pelo periodo a ser impresso
        for evento in self.agenda:
            if periodo:
                if fim >= evento.dataInicio.date():
                    evento.printEvento(True, True, True)
                else:
                    break
            elif inicio <= evento.dataInicio.date():
                    evento.printEvento(True, True, True)
                    periodo = True

    def printTodosEventos(self):
        for evento in self.agenda:
            evento.printEvento(True, True, True)

