from models.Pet import Pet
from helpers.helper import getAnswer
import itertools
id_iter = itertools.count(1)
class Cliente:
    def __init__(self, nome, email, telefone, cpf):
        self.id_cliente = next(id_iter)
        self.nome = nome.capitalize()
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = []
        self.gasto = 0

    def novoPet(self):
        while True:
            nomePet = input("Nome: ")

            self.pets.append(Pet(input("Espécie: "), nomePet, input("Raça: "), input("Cor: ")))
            if getAnswer("Deseja cadastrar outro animal a este dono?(S/N) ") == "N":
                break

    def editarCliente(self):
        while True:
            option = input("Qual informação deseja editar?\n1) E-mail\n2) Telefone\n3) Voltar")
            if(option == '1'):
                self.email = input('Novo E-mail: ')
                return
            elif (option == '2'):
                self.telefone = input('Novo telefone: ')
                return
            elif(option == '3'):
                return
            else: print("Opção inválida")

    def printData(self, detalhes, pets):
        print("Nome:", self.nome.ljust(32), end=" ")
        if detalhes:
            print("| Email:", self.email.ljust(32), "| Telefone:", self.telefone.ljust(15), "| CPF:", str(self.cpf).ljust(11), end=" ")
        if pets:
            print("-- Animais: ", end="")
            for j in self.pets:
                print(j.nome + ("\n" if j == self.pets[-1] else ", "), end="")
