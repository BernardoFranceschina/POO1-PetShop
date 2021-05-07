from PetShopStruct import *
clients = []

def main():
    while True:
        option = input("\n\nSelecione uma opção:\n1) Cadastrar cliente\n2) Cadastrar animal\n3) Consultar dados\n5) Alterar dados de um\n\n")
        if option == "1":
            registerClient()
        elif option == "2":
            registerPet()
        elif option == "3":
            printData()         #Mudar nome
        elif option == "4":
            print("cu")
        elif option == "5":
            print("Encerrando o programa.")
            return
        else: print("Comando inválido")

def registerClient():
    clients.append(Client(input("Nome: "), input("Email: "), input("Número de telefone: "), input("CPF: ")))
    if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
        clients[-1].addPet()
    
def registerPet():
    while True:
        name = input("Qual o dono do animal? ")
        clientIndex = findClient(name, clients)
        if clientIndex == []:
            print("Cliente não encontrado.")
            if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
                printList(False, True, clients)
                continue

        elif len(clientIndex) == 1:
            clients[clientIndex[0]].addPet()
            break

        else:
            clients[choosefromlist("Mais de um cliente com este nome encontrado. Escolha um da seguinte lista:", clientIndex, clients, exitOption=False)].addPet()
            break

def printData():
    name = input("Nome do cliente ou animal: ")
    objIndex = findClient(name, clients) + findPet(name, clients)

    if objIndex == []:
        print("Cliente/animal não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            printList(False, True, clients)

    elif len(objIndex) == 1:
        if isClientIndex(objIndex[0]):
            clients[objIndex[0]].printData(True, True)
        else:
            clients[objIndex[0][0]].pets[objIndex[0][1]].printData(True)

    else:
        choice = choosefromlist("Mais de um cliente/animal com este nome encontrado. Escolha um da seguinte lista:", objIndex, clients, exitOption=False)
        if isClientIndex(objIndex[choice]):
            clients[objIndex[choice]].printData(True, True)
        else:
            clients[objIndex[choice][0]].pets[objIndex[choice][1]].printData(True)

main()