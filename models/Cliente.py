from models.Pet import Pet
from helpers.helper import getAnswer
import itertools
id_iter = itertools.count()
class Cliente:
    def __init__(self, nome, email, telefone, cpf):
        self.id_cliente = next(id_iter)
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = []
        self.gasto = 0

    def novoPet(self):
        while True:
            self.pets.append(Pet(input("Espécie: "), input("Nome: "), input("Raça: "), input("Cor: ")))
            if getAnswer("Deseja cadastrar outro animal a este dono?(S/N) ") == "N":
                break

    def printData(self, detalhes, pets):
        print("\nNome:", self.nome, end=" ")
        if detalhes:
            print("| Email:", self.email, "| Telefone:", self.telefone, "| CPF:", self.cpf, end=" ")
        if pets:
            print("-- Animais: ", end="")
            for j in self.pets:
                print(j.nome + ("\n" if j == self.pets[-1] else ", "), end="")
