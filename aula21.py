import sys

class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None 
    def atacar(self):
        if self._arma is not None:
                print(f"{self._nome} ataca com adaga e causa varios pontos..")
        else:
            print(f"{self._nome} ataca com as maos e causa 1 ponto de dano")

class Feiticeiro:
    def __init__(self, nome):
        self._nome = nome
        self._encantamento = None 
    def atacar(self):
        if self._encantamento is not None:
                print(f"{self._nome} lanca seu feitico")
        else:
            print(f"{self._nome} ataca com as maos e causa 1 ponto de dano")

class GrupoAventureiros:
    def __init__(self, nome):
        self._nome = nome
        self._guerreiro = None
        self._feiticeiro = None 

#Driver code

guerreiro_1 = Guerreiro("Atilia, o Huno")
guerreiro_1.atacar()

feiticeiro_1 = Feiticeiro("Gondolf, O Branco")
feiticeiro_1.atacar()

guerreiro_1._arma = True
guerreiro_1.atacar()

feiticeiro_1._encantamento = True
feiticeiro_1.atacar()

grupo_dos_sonhos = GrupoAventureiros("grupo dos sonhos")
grupo_dos_sonhos._guerreiro = guerreiro_1
grupo_dos_sonhos._feiticeiro = feiticeiro_1
print(grupo_dos_sonhos)