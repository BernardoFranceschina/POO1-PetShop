class Client:
    def __init__(self, name, email, number, cpf, pets = [], income = 0):
        self.name = name
        self.email = email
        self.number = number
        self.cpf = cpf
        self.pets = pets
        self.income = income
    
    def addPet(self):
        while True:
            self.pets.append(Pet(input("Espécie: "), input("Nome: "), input("Raça: "), input("Cor: ")))
            if getAnswer("Deseja cadastrar outro animal a este dono?(S/N) ") == "N":
                break

class Pet:
    def __init__(self, animalType, name, breed, color):
        self.animalType = animalType
        self.name = name
        self.breed = breed
        self.color = color

def findClient(clients):
    name = input("Qual o nome do cliente? ")
    foundClients = []

    for i in range(len(clients)):
        if clients[i].name == name:
            foundClients.append(i)

    if foundClients == []:
        print("Nenhum cliente encontrado")
        return None

    else: return foundClients

def choosefromlist(text, options, clients, exitOption):
    print(text)
    for i in range(len(options)):
        if isinstance(clients[options[i]], Client):
            print(f"\n{i+1}: Cliente:", clients[options[i]].name, "Email:", clients[options[i]].email, "CPF:", clients[options[i]].cpf, "Animais:", end="")
            for j in clients[options[i]].pets:
                print(j.name, end=" ") 
        else:
            print(f"{i+1}: Animal:", clients[options[i]].name, "Espécie:", clients[options[i]].animalType, "Raça:", clients[options[i]].breed, "Cor:", clients[options[i]].color)

    if exitOption:
        return int(getAnswer("", [str(x) for x in range(len(options) + 1)]))
    else: return int(getAnswer("", [str(x) for x in range(1, len(options) + 1)])) - 1
    

def printList(clientDetails, pets, clients):
    for i in clients:
        print("Nome:", i.name, end=" ")
        if clientDetails:
            print("Email:", i.email, "Telefone:", i.number, "CPF:", i.cpf, end=" ")
        if animals:
            print("Animais: ", end="")
            for j in i.pets:
                print(j.name, end=" ")

def getnum(question, amount = 1, min = 'n', max = 'n', type = 'i', separator = " "):
    def isvalidinput(list1):
        counter = 0
        for i in list1:
            if i == "":
                return False
            for j in i:
                j = ord(j)
                if j == 46:
                    if counter == 0:
                        counter =+ 1
                    else: return False

                elif j < 48 or j > 57:
                    if j != 45:
                        return False
        return True

    print(question, end=" ")
    while True:
        text = input().split(separator)

        if amount != 'n':
            if not len(text) == amount:
                print("Por favor, insira", amount, "número" if amount == 1 else "números")
                continue
        else: amount = len(text)

        if not isvalidinput(text):
            print("Por favor, insira apenas números.")
            continue

        if type == 'i':
            for n in range(amount):
                text[n] = int(text[n])
        else:
            for n in range(amount):
                text[n] = float(text[n])

    
        error = False
        if isinstance(min, list):
            for i in range(amount):
                if min[i] != 'n':
                    if text[i] < min[i]:
                        error = True
                        print(f"Os números inseridos devem ser maiores que {min}")
                        break
            if error: continue

        elif min != 'n':
            for i in range(amount):
                if text[i] < min:
                    error = True
                    print(f"Os números inseridos devem ser maiores que {min}")
            if error: continue

        if isinstance(max, list):
            for i in range(amount):
                if max[i] != 'n':
                    if text[i] > max[i]:
                        error = True
                        print(f"Os números inseridos devem ser menores que {max}")
                        break
            if error: continue
        
        elif max != 'n':
            for i in range(amount):
                if text[i] > max:
                    error = True
                    print(f"Os números inseridos devem ser menores que {max}")
            if error: continue
        
        break      

    return text[0] if amount == 1 else text

def getAnswer(text, options = ['S', 'N']):
    while True:
        answer = input(text).strip().upper()
        if not (answer in options):
            print("Comando inválido")
        else: return answer