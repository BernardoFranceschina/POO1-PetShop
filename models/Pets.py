import itertools

class Pet:

    id_iter = itertools.count(1)

    def __init__(self, especie, nome, raca, cor):
        self.especie = especie
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.id_pet = next(Pet.id_iter)


class Vip(Pet):
    def __init__(self, peso, altura, vacinas, especie, nome, raca, cor, planoSaude):
        self.peso = peso
        self.altura = altura
        self.vacinas = vacinas
        self.planoSaude = planoSaude
        super().__init__(especie, nome, raca, cor)

