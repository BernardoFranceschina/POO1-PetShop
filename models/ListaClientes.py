from Cliente import Cliente
from helper import getAnswer

class ListaClientes:
    def __init__(self):
        self.clientes = []

    def novoCliente(self, nome, email, telefone, cpf, pets=[], gasto=0):
        self.clientes.append(cliente(input("Nome: "), input("Email: "), input("Número de telefone: "), input("CPF: ")))
        if getAnswer("Deseja cadastrar um animal deste dono? (s/n)") == 'S':
            self.clientes[-1].addPet()

##    def excluirCliente(self, idnome):
        #fazer -- permitir pesquisa por ID ou por Nome, identificando qual deles o usuário usou como entrada