import sys

class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None 
    def atacar(self):
        if self._arma is not None:
                print(f"{self._nome} ataca com {self._arma._nome} e causa {self._arma._dano} pontos..")
        else:
            print(f"{self._nome} ataca com as maos e causa 1 ponto de dano")

class Arma1M:
    def __init__(self, nome, dano):
        self._nome = nome
        self._dano = dano 
    def __str__(self):
         return f"A arma \"{self._nome}\" causa ({self._dano}) pontos de dano"
    
#Driver code

guerreiro_1 = Guerreiro("Vercingetorix")
# guerreiro_1.atacar()

guerreiro_2 = Guerreiro("Boudicca")
# guerreiro_2.atacar()

arma_1 = Arma1M("Adaga", 7)
# print(arma_1)

arma_2 = Arma1M("Espada Curta", 13)
# print(arma_2)

guerreiro_1._arma = arma_1
guerreiro_2._arma = arma_2
print("Referencias:",sys.getrefcount(arma_1))
del arma_1

fgv = guerreiro_1._arma
fgv_2 = guerreiro_1._arma
print("Referencias:",sys.getrefcount(guerreiro_1._arma))
guerreiro_1.atacar()
print(guerreiro_1._arma._nome, guerreiro_1._arma._dano)