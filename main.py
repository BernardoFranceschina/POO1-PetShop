from helpers.helper import *
from models import *

clientes = []

def main():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar Cliente\n2) Cadastrar animal\n3) Consultar dados\n5) Alterar dados de um\n\n")
        if option == "1":
            registercliente()
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

def registercliente():
    clientes.novoCliente()
    
def registerPet():
    nome = input("Qual o dono do animal? ")
    clienteIndex = getcliente(nome, clientes)
    if clienteIndex == []:
        print("Cliente não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            printList(False, True, clientes)

    elif len(clienteIndex) == 1:
        clientes[clienteIndex[0]].addPet()

    else:
        clientes[choosefromlist("Mais de um Cliente com este nome encontrado. Escolha um da seguinte lista:", clienteIndex, clientes, exitOption=False)].addPet()
        
def printData():
    nome = input("Nome do Cliente ou animal: ")
    objIndex = getcliente(nome, clientes) + getPet(nome, clientes)

    if objIndex == []:
        print("Cliente/animal não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            printList(False, True, clientes)

    elif len(objIndex) == 1:
        if isclienteIndex(objIndex[0]):
            clientes[objIndex[0]].printData(True, True, clientes)
        else:
            clientes[objIndex[0][0]].pets[options[0][1]].printData(True)

    else:
        choice = choosefromlist("Mais de um Cliente/animal com este nome encontrado. Escolha um da seguinte lista:", objIndex, clientes, exitOption=False).printData(True, True)


main()