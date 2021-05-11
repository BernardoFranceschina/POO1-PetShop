import itertools
from helpers.helper import *
from datetime import timedelta
id_iter = itertools.count(1)
class Procedimento:
    def __init__(self, nome, valor, tempo, descricao):
        self.id_procedimento = next(id_iter)
        self.nome = nome
        self.valor  = valor
        self.descricao = descricao
        self.tempo = tempo

    def excluirProcedimentossss(self):
        del self

    def editar(self):
        while True:
            option = input("Qual informação deseja editar?\n1) Nome\n2) Valor\n3) Descrição\n4) Tempo\n0) Voltar")
            if (option == '1'):
                self.nome = input('Novo nome: ')
                return
            elif (option == '2'):
                self.valor = input('Novo valor: ')
                return
            elif (option == '3'):
                self.descricao = input("Nova descricao: ")
                return
            elif (option == '4'):
                duracao = getnum("Duração(hh:mm): ", 2, 0, [24, 60], separator=":")
                duracao = timedelta(hours=duracao[0], minutes=duracao[1])
                self.tempo = duracao
            elif(option == '0'):
                return
            else: print("Opção inválida")