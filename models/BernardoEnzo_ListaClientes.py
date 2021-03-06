#Bernardo Carlos Franceschina - 20203080
#Enzo Bassani - 20200398
from models.BernardoEnzo_Cliente import Cliente
from helpers.BernardoEnzo_helper import getAnswer, getnum, choosefromlist


class ListaClientes:
    def __init__(self):
        self.clientes = []
        self.vips = 0

    def novoCliente(self):
        self.clientes.append(Cliente(input("Nome: "), input("Email: "), input("Número de telefone: "), getnum("CPF:")))
        if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
            self.clientes[-1].novoPet(self)

    def encontrarCliente(self, info, ID=False):
        if ID:                                              #busca por ID
            for cliente in range(len(self.clientes)):
                if self.clientes[cliente].nome == info:
                    return cliente
            return -1

        else:
            if info.isnumeric():
                info = int(info)
                for cliente in range(len(self.clientes)):   #busca por CPF
                    if self.clientes[cliente].cpf == info:
                        return cliente
                return -1

            else:
                info = info.capitalize()
                foundClients = []
                for cliente in range(len(self.clientes)):   #busca por nome. Caso haja mais de um, pede para o usuário escolher um.
                    if self.clientes[cliente].nome == info:
                        foundClients.append(cliente)

                if foundClients == []:
                    return -1
                elif len(foundClients) == 1:
                    return foundClients[0]
                else:
                    choice = choosefromlist("Mais de um cliente com este nome encontrado. Escolha uma opção da seguinte lista:", foundClients, self.clientes, isClient=True, exitOption=True)
                    if choice == -1:
                        return -2
                    else: return foundClients[choice]

    def printLista(self, detalhes, pets):
        for cliente in self.clientes:
            cliente.printData(detalhes, pets)

    def encontrarPet(self, info):
        foundPets = []
        for cliente in range(len(self.clientes)):
            for pet in range(len(self.clientes[cliente].pets)):
                if self.clientes[cliente].pets[pet].nome == info:
                    foundPets.append([cliente, pet])
    
        return foundPets

#    def excluirPet(self, nome):
#        for cliente in range(len(self.clientes)):
#            for pet in range(len(self.clientes[cliente].pets)):
#                if self.clientes[cliente].pets[pet].nome == nome:
#                    del (self.clientes[cliente].pets[pet])

