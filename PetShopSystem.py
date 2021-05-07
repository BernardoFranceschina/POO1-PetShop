from PetShopStruct import *
clients = []
                #sonim blainim sinim clevri


def main():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar cliente\n2) Cadastrar animal\n3) Consultar dados\n5) Alterar dados de um\n\n")
        if option == "1":
            registerClient()
        elif option == "2":
            registerPet()
        elif option == "3":
            printData()
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
    clientIndex = findClient(clients)
    if clientIndex == None:
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            printList(False, True, clients)

    elif len(clientIndex) == 1:
        clients[clientIndex[0]].addPet()

    else:
        clients[choosefromlist("Mais de um cliente/animal com este nome encontrado. Escolha um da seguinte lista:", clientIndex, clients, exitOption=False)].addPet()
        
def printData():
    name = input("Nome do cliente ou animal: ")
    for i in clients:
        if i.name == name:
            print("\nNome:", i.name, "\nEmail:", i.email, "\nTelefone:", i.number, "\nCPF:", i.cpf)
            return
        for j in i.pets:
            if j.name == name:
                print("\nNome:", j.name, "\nEspécie:", j.animalType, "\nRaça:", j.breed, "\nCor:", j.color)

main()


#fikoooooooooooooooooof