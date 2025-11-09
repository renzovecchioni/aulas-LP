class Fruta:
    def __init__(self, nome):
        self.nome = nome 
    def envelhecer_na_despensa(self):
        print(f"{self.nome} esta envelhecendo na despensa enquanto vc pede ifood.")

banana = Fruta("banana")
banana.envelhecer_na_despensa()

#Raiz
Fruta.envelhecer_na_despensa(banana)
print("#"*40)

maca =  Fruta("maca")
print(maca.__dict__)
print(vars(maca))
print("#"*40)

maca.peso = 1
maca.validade = "31/12/2025"
print(maca.__dict__)

print(maca.nome)
print(maca.peso)
print(maca.validade)
print("#"*40)

del maca.__dict__["validade"]
del maca.__dict__["peso"]
print(maca.__dict__)
maca.__dict__["tipo"] = "Gala"
print(maca.__dict__)