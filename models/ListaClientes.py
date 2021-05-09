from models.Cliente import Cliente
from helpers.helper import getAnswer
import itertools


class ListaClientes:
    def __init__(self):
        self.clientes = []

    def novoCliente(self):
        self.clientes.append(Cliente(input("Nome: "), input("Email: "), input("Número de telefone: "), input("CPF: ")))
        if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
            self.clientes[-1].novoPet()

    def encontrarCliente(self, info, ID=False):
        foundClients = []
        if ID:
            for cliente in range(len(self.clientes)):
                if self.clientes[cliente].nome == info:
                    foundClients.append(cliente)

        else:
            if info.isnumeric():
                for cliente in range(len(self.clientes)):
                    if self.clientes[cliente].cpf == info:
                        foundClients.append(cliente)
            else:
                for cliente in range(len(self.clientes)):
                    if self.clientes[cliente].nome == info:
                        foundClients.append(cliente)
                
        return foundClients

    def printLista(self, detalhes, pets):
        for cliente in self.clientes:
            cliente.printData(detalhes, pets)

    def encontrarPet(self, info, ID=False):                             #se ID for 1, a função busca pelo ID. Se for 0, busca pelo nome ou CPF.           
        foundPets = []
        if ID:
            for cliente in range(len(self.clientes)):
                for pet in range(len(self.clientes[cliente].pets)):
                    if self.clientes[cliente].pets[pet].id_pet == info:
                        foundPets.append([cliente, pet])


        else:
            for cliente in range(len(self.clientes)):
                for pet in range(len(self.clientes[cliente].pets)):
                    if self.clientes[cliente].pets[pet].nome == info:
                        foundPets.append([cliente, pet])
    
        return foundPets


##    def excluirCliente(self, IDnome):
        #fazer -- permitir pesquisa por ID ou por Nome, identificando qual deles o usuário usou como entrada