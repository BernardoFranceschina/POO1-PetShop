from helpers.helper import *
from models.Pets import *


class Cliente:
    def __init__(self, nome, email, telefone, cpf, pets=[], gasto=0):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = pets
        self.gasto = gasto
