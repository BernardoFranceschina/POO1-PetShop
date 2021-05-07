#cliente
def getcliente(nome, clientes):
    foundclientes = []

    for i in range(len(clientes)):
        if clientes[i].nome == nome:
            foundclientes.append(i)

    else:
        return foundclientes
def choosefromlist(text, options, clientes, exitOption):
    print(text)
    for i in range(len(options)):
        if isclienteIndex(options[i]):
            print(f"\n{i + 1}: Cliente -- ", end="")
            clientes[options[i]].printData(True, True)
        else:
            print(f"{i + 1}: Animal -- ", end="")
            clientes[options[i][0]].pets[options[i][1]].printData(True)

    if exitOption:
        return int(getAnswer("", [str(x) for x in range(len(options) + 1)]))
    else:
        return int(getAnswer("", [str(x) for x in range(1, len(options) + 1)])) - 1
def isclienteIndex(index):
    if isinstance(index, int):
        return True
    else:
        return False
def printList(clienteDetails, pets, clientes):
    for cliente in clientes:
        cliente.printData(clienteDetails, pets)
def addPet(self):
            while True:
                self.pets.append(Pet(input("Espécie: "), input("Nome: "), input("Raça: "), input("Cor: ")))
                if getAnswer("Deseja cadastrar outro animal a este dono?(S/N) ") == "N":
                    break

#pet
def printData(self, detalhes, trash=0):
        print("\nNome:", self.nome, "\nEspécie:", self.especie, end=" ")
        if detalhes:
            print("\nRaça:", self.breed, "\nCor:", self.color)
def getPet(nome, clientes):
    foundPets = []

    for cliente in range(len(clientes)):
        for pet in range(len(clientes[cliente].pets)):
            if clientes[cliente].pets[pet].nome == nome:
                foundPets.append([cliente, pet])

    else:
        return foundPets
def printData(self, detalhes, pets):
        print("\nNome:", self.nome, end=" ")
        if detalhes:
            print("Email:", self.email, "Telefone:", self.telefone, "CPF:", self.cpf, end=" ")
        if pets:
            print("Animais: ", end="")
            for pet in self.pets:
                print(pet.nome, end=", ")
