from helpers.helper import *
from models.Agenda import Agenda
from models.Cliente import Cliente
from models.ListaClientes import ListaClientes
from models.ListaProcedimentos import ListaProcedimentos
from models.Pet import Pet
from models.Procedimento import Procedimento
from models.Trabalho import Trabalho

clientes = ListaClientes()
agenda = Agenda()
procedimentos = ListaProcedimentos()

def main():
    while True:
        option = input("Selecione uma opção:\n1) Clientes\n2) Agenda\n3) Procedimentos\n0) Encerrar o programa\n")
        print()
        if option == "1":
            menuClientes()
        elif option == "2":
            menuAgenda()
        elif option == "3":
            menuProcedimentos()
        elif option == "0":
            return
        else:
            print("Comando inválido")

def menuAgenda():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar novo horário\n2) Excluir horário\n3) Exibir consultas do dia\n4) Exibir consultas de amanhã\n0) Voltar\n")
        if option == "1":
            print()
        elif option == "2":
            print()
        elif option == "3":
            print()
        elif option == "0":
            return
        else:
            print("Comando inválido")

def menuProcedimentos():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar procedimento\n2) Excluir procedimento\n3) Exibir todos procedimentos\n0) Voltar\n")
        if option == "1":
            procedimentos.novoProcedimento()
        elif option == "2":
            procedimentos.excluirProcedimento(input("Nome: "))
        elif option == "3":
            procedimentos.listarProcedimentos()
        elif option == "0":
            return
        else:
            print("Comando inválido")

def menuClientes():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar cliente\n2) Selecionar cliente\n3) Exibir todos os cadastros\n0) Voltar\n")
        if option == "1":
            clientes.novoCliente()
        elif option == "2":
            selecionarCliente()
        elif option == "3":
            clientes.printLista(True, True)
        elif option == "0":
            return
        else:
            print("Comando inválido")

def selecionarCliente():
    nome = input("Nome/CPF do Cliente: ")

    clienteIndex = clientes.encontrarCliente(nome)
    if clienteIndex == -1:
        print("Cliente não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais?(S/N) ") == 'S':
            clientes.printLista(False, True)  ##printList(False, True, clientes)
        return
    if clienteIndex == -2:
        return

    print("\nCliente selecionado:", clientes.clientes[clienteIndex].nome)
    while True:
        option = input(
            "Selecione uma opção:\n1) Novo animal\n2) Editar cadastro\n3) Excluir cadastro\n4) Exibir informações\n0) Voltar ao menu principal\n\n")
        if option == "1":
            clientes.clientes[clienteIndex].novoPet()
        elif option == "2":
            clientes.clientes[clienteIndex].editarCliente()
        elif option == "3":
            if getAnswer(f'Deseja excluir este cliente?') == "S":
                clientes.clientes[clienteIndex].excluirCliente()
                del (clientes.clientes[clienteIndex])
                return
        elif option == "4":
            clientes.clientes[clienteIndex].printData(True, True)
        elif option == "0":
            return
        else:
            print("Comando inválido")


main()
