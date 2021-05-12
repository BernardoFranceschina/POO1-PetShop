from helpers.helper import *
from models.Agenda import Agenda
from models.Cliente import Cliente
from models.ListaClientes import ListaClientes
from models.ListaProcedimentos import ListaProcedimentos
from models.Pet import Pet
from models.Procedimento import Procedimento
from models.Evento import Evento
from datetime import date

#falta permitir editar e excluir o cadastro de um animal
#impedir o usuário de cadastrar um nome repetido para animal do mesmo dono

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
        option = input("\nSelecione uma opção:\n1) Cadastrar novo evento\n2) Editar Evento\n3) Excluir evento\n4) Exibir agenda do dia\n5) Exibir agenda de amanhã\n6) Exibir um período específico\n7) Exibir todos os eventos\n0) Voltar\n")
        if option == "1":
            agenda.novoEvento(clientes, procedimentos)
        elif option == "2":
            eventoIndex = agenda.selecionarEvento(clientes)
            if eventoIndex == -1:
                print("Procedimento não encontrado")
            else:
                agenda.agenda[eventoIndex].editarEvento(clientes, procedimentos, agenda, eventoIndex)
        elif option == "3":
            eventoIndex = agenda.selecionarEvento(clientes)
            if eventoIndex == -1:
                print("Procedimento não encontrado")
            else:
                #agenda.agenda[eventoIndex].excluirEvento()
                agenda.agenda.pop(eventoIndex)
        elif option == "4":
            hoje = date.today()
            agenda.printAgenda(hoje, hoje)
        elif option == "5":
            hoje.day = hoje.day + 1
            agenda.printAgenda(hoje, hoje)
        elif option == "6":
            inicio = getData("Desde (dd/mm/aa): ", False)
            if inicio == -1:
                continue
            fim = getData("Até (dd/mm/aa): ", False)
            if fim == -1:
                continue
            agenda.printAgenda(inicio, fim)
        elif option == "7":
            agenda.printTodosEventos()
        elif option == "0":
            return
        else:
            print("Comando inválido")

def menuProcedimentos():
    while True:
        option = input("\nSelecione uma opção:\n1) Cadastrar procedimento\n2) Editar procedimento\n3) Excluir procedimento\n4) Exibir todos os procedimentos\n0) Voltar\n")
        if option == "1":
            procedimentos.novoProcedimento()
        elif option == "2":
            procedimento = procedimentos.encontrarProcedimento(input("Nome: "))
            if procedimento == -1:
                print("Procedimento não encontrado")
            else: procedimentos.procedimentos[procedimento].editar()
        elif option == "3":
            procedimento = procedimentos.encontrarProcedimento(input("Nome: "))
            if procedimento == -1:
                print("Procedimento não encontrado")
            else: procedimentos.excluirProcedimento(procedimento)
        elif option == "4":
            procedimentos.listarProcedimentos()
        elif option == "0":
            return
        else: print("Comando inválido")

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

    clienteIndex = clientes.encontrarCliente(input("Nome/CPF do Cliente: "))
    if clienteIndex == -1:
        print("Cliente não encontrado.")
        if getAnswer("Deseja ver a lista de clientes e seus animais?(S/N) ") == 'S':
            clientes.printLista(False, True)
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