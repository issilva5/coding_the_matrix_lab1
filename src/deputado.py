#coding: utf-8

class Deputado:
    
    #Construtor da classe
    def __init__(self, nome, estado, partido, votos):
        self.nome = nome
        self.estado = estado
        self.partido = partido
        self.votos = votos

    #Representação em String da classe
    def __str__(self):
        return self.nome + ", " + self.estado + ", " + self.partido
