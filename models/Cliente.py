from Pet import Pet
class Cliente:
    def __init__(self, id_cliente, nome, email, telefone, cpf, pets=[], gasto=0):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = pets
        self.gasto = gasto

    def novoPet(self):
        while True:
            self.pets.append(Pet(input("Espécie: "), input("Nome: "), input("Raça: "), input("Cor: ")))
            if getAnswer("Deseja cadastrar outro animal a este dono?(S/N) ") == "N":
                break

    def printData(self, detalhes, pets):
        print("\nNome:", self.nome, end=" ")
        if detalhes:
            print("Email:", self.email, "Telefone:", self.telefone, "CPF:", self.cpf, end=" ")
        if pets:
            print("-- Animais: ", end="")
            for j in self.pets:
                print(j.name, end=", ")
