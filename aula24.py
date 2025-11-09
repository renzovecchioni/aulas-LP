class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self._arma = None 
    def atacar(self):
        if self._arma is not None:
            print(f"{self.nome} ataca com {self._arma.nome}")
        else:
            print(f"{self.nome} atacou com as proprias maos")
    def equipar_arma(self, nome):
        self._arma = Arma(nome)
    
    def __del__(self):
        print(f"Removendo {self.nome}")
class Arma:
    def __init__(self, nome):
        self.nome = nome 
    def __str__(self):
        print(f"Eu sou a arma do {self.nome}")
    def __del__(self):
        print(f"Removendo {self.nome}")
    
#driver code
guerreiro = Guerreiro("Miyamoto Musachi")
guerreiro.atacar()
guerreiro.equipar_arma("wakizashi")
guerreiro.atacar()

del guerreiro 