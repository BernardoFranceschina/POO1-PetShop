from models.Cliente import Cliente
from helpers.helper import getAnswer, choosefromlist


class ListaClientes:
    def __init__(self):
        self.clientes = []

    def novoCliente(self):
        self.clientes.append(Cliente(input("Nome: "), input("Email: "), input("Número de telefone: "), input("CPF: ")))
        if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
            self.clientes[-1].novoPet()

    def encontrarCliente(self, info, ID=False):
        if ID:                                              #busca por ID
            for cliente in range(len(self.clientes)):
                if self.clientes[cliente].nome == info:
                    return cliente
            return -1

        else:
            if info.isnumeric():
                for cliente in range(len(self.clientes)):   #busca por CPF
                    if self.clientes[cliente].cpf == info:
                        return cliente
                return -1

            else:
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
