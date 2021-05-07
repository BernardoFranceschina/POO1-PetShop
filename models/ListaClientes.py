from Cliente import Cliente
from helper import getAnswer
import itertools
id_iter = itertools.count()

class ListaClientes:
    def __init__(self):
        self.clientes = []

    def novoCliente(self, nome, email, telefone, cpf, pets=[], gasto=0):
        self.clientes.append(cliente(next(ListaClientes.id_iter), input("Nome: "), input("Email: "), input("Número de telefone: "), input("CPF: ")))
        if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
            self.clientes[-1].novoPet()

    def encontrarCliente(self, nome):
        foundClients = []

        for cliente in range(len(self.clientes)):
            if self.clientes[cliente].nome == nome:
                foundClients.append(cliente)
        return foundClients

    def printLista(self, detalhes, pets):
        for cliente in self.clientes:
            cliente.printData(detalhes, pets)

    def encontrarPet(self, nome):
        foundPets = []
    
        for cliente in range(len(self.clientes)):
            for pet in range(len(self.clientes[cliente].pets)):
                if self.clientes[cliente].pets[pet].name == name:
                    foundPets.append([cliente, pet])
    
        return foundPets


##    def excluirCliente(self, IDnome):
        #fazer -- permitir pesquisa por ID ou por Nome, identificando qual deles o usuário usou como entrada