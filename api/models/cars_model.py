from api import mongo

class Cars():
    def __init__(self,nome, modelo, ano, fabricante, combustivel):
        self.nome = nome
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante
        self.combustivel = combustivel