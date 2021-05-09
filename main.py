from helpers.helper import *
from models.Agenda import Agenda
from models.Cliente import Cliente
from models.ListaClientes import ListaClientes
from models.Pet import Pet
from models.Procedimento import Procedimento
from models.Trabalho import Trabalho

clientes = ListaClientes()

def main():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar Cliente\n2) Cadastrar animal\n3) Consultar dados\n5) Alterar dados de um\n\n")
        if option == "1":
            clientes.novoCliente()
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

    
def registerPet():
    nomeCPF = input("Qual o dono do animal? Nome/CPF: ")
    clienteIndex = clientes.encontrarCliente(nomeCPF)

    if clienteIndex == []:
        print("Cliente não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            clientes.printLista(False, True)    ##printList(False, True, clientes)

    elif len(clienteIndex) == 1:
        clientes.clientes[clienteIndex[0]].novoPet()

    else:
        clientes.clientes[choosefromlist("Mais de um Cliente com este nome encontrado. Escolha um da seguinte lista:", clienteIndex, clientes, exitOption=False)].novoPet()
        
def printData():
    nome = input("Nome/CPF do Cliente ou nome do animal: ")
    objIndex = clientes.encontrarCliente(nome) + clientes.encontrarPet(nome)

    if objIndex == []:
        print("Cliente/animal não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais? ") == 'S':
            clientes.printLista(False, True)

    elif len(objIndex) == 1:
        if isclienteIndex(objIndex[0]):
            clientes.clientes[objIndex[0]].printData(True, True)
        else:
            clientes.clientes[objIndex[0][0]].pets[objIndex[0][1]].printData(True)

    else:
        choice = choosefromlist("Mais de um Cliente/animal com este nome encontrado. Escolha um da seguinte lista:", objIndex, clientes, exitOption=False)
        choice = choosefromlist("Mais de um cliente/animal com este nome encontrado. Escolha um da seguinte lista:", objIndex, clients, exitOption=False)
        if isclienteIndex(objIndex[choice]):
            clients[objIndex[choice]].printData(True, True)
        else:
            clients[objIndex[choice][0]].pets[objIndex[choice][1]].printData(True)

main()