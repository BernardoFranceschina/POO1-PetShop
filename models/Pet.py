import itertools
id_iter = itertools.count(0)
class Pet:
    def __init__(self, id_pet, especie, nome, raca, cor):
        self.id_pet = id_pet
        self.especie = especie
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.id_pet = next(Pet.id_iter)

    def printData(self, detalhes):
        print("\nNome:", self.nome, "\nEspécie:", self.especie, end=" ")
        if detalhes:
            print("\nRaça:", self.raca, "\nCor:", self.cor)

class Vip(Pet):
    def __init__(self, id_pet, especie, nome, raca, cor, peso, altura, vacinas, planoSaude):
        self.peso = peso
        self.altura = altura
        self.vacinas = vacinas
        self.planoSaude = planoSaude
        super().__init__(id_pet, especie, nome, raca, cor)
