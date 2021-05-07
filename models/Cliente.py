class Cliente:
    def __init__(self, id_cliente, nome, email, telefone, cpf, pets=[], gasto=0):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        self.pets = pets
        self.gasto = gasto
