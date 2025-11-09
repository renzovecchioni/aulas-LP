class Cachorro:
    """ 
    Classe que representa um cachorro
    """
    # cls -> Cachorro
    contador_cachorros = 0
    def __init__(self, nome, raca, idade):
        self.nome = nome 
        self.raca = raca 
        self.idade = idade 
        Cachorro.contador_cachorros += 1
    def latir(self):
        return "Au Au!"
    @classmethod
    def get_numero_cachorros(cls):
        return cls.contador_cachorros
    @classmethod 
    def from_String(cls, string_cachorro): 
        nome, raca, idade = string_cachorro.split(",")
        return cls(nome, raca, idade)
    
cachorro_1 = Cachorro("Cacau", "Lulu", "7")
cachorro_2 = Cachorro("PEPE", "Labrador", "18")

print(Cachorro.contador_cachorros)
print(Cachorro.get_numero_cachorros())

cachorro_3= Cachorro.from_String("Jade, Golden, 5")
print(Cachorro.get_numero_cachorros())
print(cachorro_1.contador_cachorros)

print(cachorro_1.latir())