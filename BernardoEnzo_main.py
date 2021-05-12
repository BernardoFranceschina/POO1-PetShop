#Bernardo Carlos Franceschina - 20203080
#Enzo Bassani - 20200398
from helpers.BernardoEnzo_helper import *
from models.BernardoEnzo_Agenda import Agenda
from models.BernardoEnzo_ListaClientes import ListaClientes
from models.BernardoEnzo_ListaProcedimentos import ListaProcedimentos
from models.BernardoEnzo_Pet import *
from datetime import date

clientes = ListaClientes()
agenda = Agenda()
procedimentos = ListaProcedimentos()

def main():
    while True:
        option = input("Selecione uma opção:\n1) Clientes\n2) Agenda\n3) Procedimentos\n4) Caixa\n0) Encerrar o programa\n")
        print()
        if option == "1": 
            menuClientes()
        elif option == "2":
            menuAgenda()
        elif option == "3":
            menuProcedimentos()
        elif option == "4":
            menuCaixa()
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
            eventoIndex = agenda.selecionarEvento()
            if eventoIndex == -1:
                print("Procedimento não encontrado")
            else:
                agenda.agenda[eventoIndex].editarEvento(clientes, procedimentos, agenda, eventoIndex)
        elif option == "3":
            eventoIndex = agenda.selecionarEvento()
            if eventoIndex == -1:
                print("Procedimento não encontrado")
            else:
                #agenda.agenda[eventoIndex].excluirEvento()
                agenda.agenda.pop(eventoIndex)
        elif option == "4":
            hoje = date.today()
            agenda.printAgenda(hoje, hoje)
        elif option == "5":
            hoje = date.today()
            hoje.replace(day = hoje.day + 1)
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
        option = input("Selecione uma opção:\n1) Cadastrar cliente\n2) Selecionar cliente\n3) Exibir todos os cadastros\n0) Voltar\n")
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
            clientes.clientes[clienteIndex].novoPet(clientes)
        elif option == "2":
            clientes.clientes[clienteIndex].editarCliente()
        elif option == "3":
            while True:
                optionExcluir = input('Selecione uma opção:\n1) Excluir Cliente\n2) Excluir Animal\n0) Voltar\n')
                if optionExcluir == "1":
                    if getAnswer(f'Deseja excluir este cliente?') == "S":
                        del (clientes.clientes[clienteIndex])
                        return
                elif optionExcluir == "2":
                    clientes.clientes[clienteIndex].printData(False, True)
                    while True:
                        print("Digite 0 para voltar")
                        nomePet = input("Nome: ").capitalize()
                        if nomePet == "0":
                            break
                        petIndex = -1
                        for pet in range(len(clientes.clientes[clienteIndex].pets)):
                            if clientes.clientes[clienteIndex].pets[pet].nome == nomePet:
                                petIndex = pet
                        if petIndex == -1:
                            print("Pet não encontrado")
                            continue
                        else:
                            if getAnswer(f'Deseja excluir este animal? (S/N)') == "S":
                                if isinstance(clientes.clientes[clienteIndex].pets[petIndex], Vip):
                                    clientes.vips -= 1
                                clientes.clientes[clienteIndex].pets.pop(petIndex)
                                break

                elif optionExcluir == "0":
                        break
                else: print("Comando inválido")

        elif option == "4":
            clientes.clientes[clienteIndex].printData(True, True)
        elif option == "0":
            return
        else:
            print("Comando inválido")
    
def menuCaixa():
    while True:
        option = input("\nSelecione uma opção:\n1) Ver fluxo de caixa esperado para o mês atual\n2) Ver fluxo de caixa esperado para este e para os próximos meses\n3) Ver fluxo de caixa dos últimos meses\n4) Ver fluxo de caixa de um período personalizado\n0) Voltar\n")
        if option == "1":
            inicio = date.today()
            fim = inicio
            inicio = inicio.replace(day = 1)
            try:
                fim = fim.replace(day = 31)
            except:
                fim = fim.replace(day = 30)
            print("Fluxo de caixa do mês atual:", agenda.getCaixa(inicio, fim, clientes))
        elif option == "2":
            meses = getnum("Deseja calcular o caixa de quantos meses além do atual? ", 1, 1, 12000)
            inicio = date.today()
            fim = inicio
            inicio = inicio.replace(day = 1)
            fim = fim.replace(year = fim.year + int((fim.month + meses)/12))
            fim = fim.replace(month = (fim.month + meses - 1)%12 + 1)
            try:
                fim = fim.replace(day = 31)
            except:
                fim = fim.replace(day = 30)
            print("Fluxo de caixa do(s)", meses, "próximo(s) mês(es):", agenda.getCaixa(inicio, fim, clientes))

        elif option == "3":
            meses = getnum("Deseja calcular o caixa de quantos dos meses anteriores?", 1, 1, 12000)
            inicio = date.today()
            fim = inicio
            inicio = inicio.replace(day = 1)
            inicio = inicio.replace(year = inicio.year - int((12 - inicio.month + meses)/12))
            inicio = inicio.replace(month = (inicio.month - meses - 1)%12 + 1)
            if fim.month == 1:
                fim = fim.replace(month = 12)
                fim = fim.replace(year = fim.year - 1)
            else: fim = fim.replace(month = fim.month - 1)
            try:
                fim = fim.replace(day = 31)
            except:
                fim = fim.replace(day = 30)
            print("Fluxo de caixa do(s)", meses, "mês(es) anterior(es):", agenda.getCaixa(inicio, fim, clientes))
        elif option == "4":
            inicio = getData("Desde (dd/mm/aa): ", False)
            if inicio == -1:
                continue
            fim = getData("Até (dd/mm/aa): ", False)
            if fim == -1:
                continue
            print("Fluxo de caixa do período:", agenda.getCaixa(inicio, fim, clientes))

        elif option == "0":
            return
        else: print("Comando inválido")
main()