class Animal:
    def __init__(self, nome, especie):
        self.nome = nome 
        self.especie = especie 
    def morrer(self):
        return f"{self.nome} morreu"
    def __str__(self):
        return f"{self.nome}  eh da especie {self.especie}"
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "cachorro")
        self.raca = raca 
    def morrer(self):
        return f"{self.nome} foi para a fazenda onde vivera feliz para sempre"
    def latir(self):
        return f"{self.nome} esta latindo"
    def __repr__(self):
        class_ = type(self).__name__ 
        return (f"{class_}(nome={self.nome!r})"
                f"(raca={self.raca!r})"
                f"(especie={self.especie!r})")
    def __str__(self):
        return f"{self.nome}, eh um(a) {self.raca}"

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "gato")
        self.raca = raca 
    def morrer(self):
        return f"{self.nome} esgotou suas 7 vidas"
    def miar(self):
        return f"{self.nome} esta miando"

cachorro_1 = Cachorro("Au au", "Vira-Lata")
print(cachorro_1)
print("#"*40)
print(ascii(cachorro_1))
print(f"{cachorro_1!a}")

gato_1 = Gato("Miau", "Vira-lata")
print(gato_1)
print(str(gato_1))
print(f"{gato_1!s}")
