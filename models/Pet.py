class Pet:
    def __init__(self, especie, nome, raca, cor):
        self.especie = especie
        self.nome = nome.capitalize()
        self.raca = raca
        self.cor = cor

    def printData(self, detalhes):
        print("Nome:", self.nome.ljust(20), "| Espécie:", self.especie.ljust(20), end=" ")
        if detalhes:
            print("| Raça:", self.raca.ljust(20), "| Cor:", self.cor.ljust(15))

class Vip(Pet):
    def __init__(self, especie, nome, raca, cor, peso, altura, vacinas, planoSaude):
        self.peso = peso
        self.altura = altura
        self.vacinas = vacinas
        self.planoSaude = planoSaude
        super().__init__(especie, nome, raca, cor)

    def printVipData(self):
        print("Peso: ", self.peso.ljust(20), "| Vacinado:", self.vacinas.ljust(20), "| Plano de saude:", self.vacinas.ljust(20), end=" ")

