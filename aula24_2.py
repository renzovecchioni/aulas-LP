class Emap:
    def __new__(cls, *args, **kwargs):
        print("Podemos fazer o que quisermos antes da instancia ser criada")
        object_ = super().__new__(cls)
        print("POdemos fazer o que quisermos depois da instancia ser criada")
        
        return object_
    def __init__(self, nr_alunos):
        print("POdemos fazer o que quisermos antes da instancia ser inicializada")
        self.nr_alunos = nr_alunos
        print("Podemos fazer o que quisermos depois da instancia ser inicializada")

# escola_nutella = Emap(42)
# print(escola_nutella.nr_alunos)

escola_raiz = object.__new__(Emap)
escola_raiz.__init__(666)
print(escola_raiz.nr_alunos)