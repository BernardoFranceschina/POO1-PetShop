# Bernardo Carlos Franceschina - 20203080
# Enzo Bassani - 20200398
from models.BernardoEnzo_Pet import *
from helpers.BernardoEnzo_helper import getAnswer
class Cliente:
    def __init__(self, nome, email, telefone, cpf):
        self.nome = nome.capitalize()
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = []
        self.gasto = 0

    def novoPet(self, clientes):
        while True:
            while True:
                nomeRepetido = False
                nomePet = input("Nome: ").capitalize()
                for cliente in range(len(clientes.clientes)):
                    for pet in range(len(clientes.clientes[cliente].pets)):
                        if clientes.clientes[cliente].pets[pet].nome == nomePet:
                            print("\nNome ja cadastrado, por favor insira outro nome")
                            nomeRepetido = True
                            break
                if not nomeRepetido:
                    break
            especiePet = input("Espécie: ")
            racaPet = input("Raça: ")
            corPet = input("Cor: ")
            if getAnswer(f'Deseja que {nomePet} seja VIP? (S/N)') == 'S':
                pesoPet = input("Peso: "),
                alturaPet = input("Altura: "),
                vacinadoPet = input("Vacinado? (S/N)"),
                planoSaudePet = input("Plano de Saude(Caso não tenha deixe em branco): ")
                clientes.vips += 1
                self.pets.append(Vip(especiePet, nomePet, racaPet, corPet, pesoPet, alturaPet, vacinadoPet, planoSaudePet))
            else: self.pets.append(Pet(especiePet, nomePet, racaPet, corPet))

            if getAnswer("Deseja cadastrar outro animal a este dono? (S/N) ") == "N":
                break

    def editarCliente(self):
        while True:
            option = input("Qual informação deseja editar?\n1) E-mail\n2) Telefone\n0) Voltar")
            if(option == '1'):
                self.email = input('Novo E-mail: ')
                return
            elif (option == '2'):
                self.telefone = input('Novo telefone: ')
                return
            elif(option == '0'):
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
        print()
