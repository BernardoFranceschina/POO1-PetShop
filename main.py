from helpers.helper import *
from models.Agenda import Agenda
from models.Cliente import Cliente
from models.ListaClientes import ListaClientes
from models.Pet import Pet
from models.Procedimento import Procedimento
from models.Trabalho import Trabalho

clientes = ListaClientes()
agenda = Agenda()

def main():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar cliente\n2) Novo evento\n3) Selecionar cliente\n4) Selecionar animal\n5) Exibir todos os cadastros\n0) Encerrar o programa\n\n")
        print()
        if option == "1":
            clientes.novoCliente()
        elif option == "2":
            print("Fazer")      #agenda.novoTrabalho       Falta fazer essa função
        elif option == "3":
            selecionarCliente()
        elif option == "4":
            print("Fazer")      #fazer
        elif option == "5":
            clientes.printLista(True, True)
        elif option == "0":
            print("Encerrando")
            return
        else: print("Comando inválido")

def selecionarCliente():
    nome = input("Nome/CPF do Cliente: ")

    clienteIndex = clientes.encontrarCliente(nome)
    if clienteIndex == -1:
        print("Cliente não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais?(S/N) ") == 'S':
            clientes.printLista(False, True)    ##printList(False, True, clientes)
        return
    if clienteIndex == -2:
        return

    
    print("\nCliente selecionado:", clientes.clientes[clienteIndex].nome)
    while True:
        option = input("Selecione uma opção:\n1) Novo animal\n2) Editar cadastro\n3) Excluir cadastro\n4) Exibir informações\n0) Voltar ao menu principal\n\n")
        if option == "1":
            clientes.clientes[clienteIndex].novoPet()
        elif option == "2":
            print("Fazer")  #Fazer
        elif option == "3":
            print("Fazer")  #Fazer
        elif option == "4":
            clientes.clientes[clienteIndex].printData(True, True)
        elif option == "0":
            return
        else: print("Comando inválido")

main()