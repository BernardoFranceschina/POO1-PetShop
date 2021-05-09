import itertools
id_iter = itertools.count(1)
class Pet:
    def __init__(self, especie, nome, raca, cor):
        self.id_pet = next(id_iter)
        self.especie = especie
        self.nome = nome
        self.raca = raca
        self.cor = cor

    def printData(self, detalhes):
        print("Nome:", self.nome, "| Espécie:", self.especie, end=" ")
        if detalhes:
            print("| Raça:", self.raca, "| Cor:", self.cor)

class Vip(Pet):
    def __init__(self, id_pet, especie, nome, raca, cor, peso, altura, vacinas, planoSaude):
        self.peso = peso
        self.altura = altura
        self.vacinas = vacinas
        self.planoSaude = planoSaude
        super().__init__(id_pet, especie, nome, raca, cor)
