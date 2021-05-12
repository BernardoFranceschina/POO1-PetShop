#Bernardo Carlos Franceschina - 20203080
#Enzo Bassani - 20200398
from datetime import datetime


def getnum(question, amount=1, min='n', max='n', type='i', separator=" "):
    def isvalidinput(list1):
        counter = 0
        for i in list1:
            if i == "":
                return False
            for j in i:
                j = ord(j)
                if j == 46:
                    if counter == 0:
                        counter = + 1
                    else:
                        return False

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
        else:
            amount = len(text)

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

def getAnswer(text, options=['S', 'N']):
    while True:
        answer = input(text).strip().upper()
        if not (answer in options):
            print("Comando inválido")
        else:
            return answer

def isclienteIndex(index):
    if isinstance(index, int):
        return True
    else: return False

def choosefromlist(text, options, clientes, isClient, exitOption):
    print(text)
    if exitOption:
        print("0: cancelar", end="")
    for i in range(len(options)):
        if isClient:
            print(f"\n{i + 1}: Cliente -- ", end="")
            clientes[options[i]].printData(True, True)
        else:
            print(f"{i + 1}: Animal -- ", end="")
            clientes[options[i][0]].pets[options[i][1]].printData(True)

    if exitOption:
        choice = int(getAnswer("\n", [str(x) for x in range(len(options) + 1)]))
        if choice == 0:
            return -1

        else: return choice - 1
    else:
        return int(getAnswer("\n", [str(x) for x in range(1, len(options) + 1)])) - 1

def getData(texto, hora):
    while True:
        data = input(texto)
        if data == '0':
            return -1
        try:
            if hora:
                data = datetime.strptime(data, "%d/%m/%y %H:%M")
            else:
                data = datetime.strptime(data, "%d/%m/%y").date()
        except:
            print("Entrada inválida")
            continue
        return data