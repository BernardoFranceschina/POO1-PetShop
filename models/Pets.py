class Pet:
    def __init__(self, especie, nome, raca, cor, id_pet):
        self.especie = especie
        self.nome = nome
        self.raca = raca
        self.cor = cor

class Vip(Pet):
    def __init__(self, peso, altura, vacinas, especie, nome, raca, cor, planoSaude):
        self.peso = peso
        self.altura = altura
        self.vacinas = vacinas
        self.planoSaude = planoSaude
        super().__init__(especie, nome, raca, cor)

