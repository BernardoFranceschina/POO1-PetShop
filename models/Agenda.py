class Agenda:
    def __init__(self):
        self.trabalhos = []

    def setTrabalhos(self, trabalho):
        self.trabalhos.append(trabalho)

    def getTrabalhos(self):
        return self