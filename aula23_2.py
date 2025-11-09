"""
__Lt__
__Le__
__gt__
__ge__
__eq__
__ne__
__add__
__sub__
__mul__
__floordiv__
__truediv__
__neq__(self)
"""
class Aluno:
    def __init__(self, qi, nr_artigos_publicados):
        self.qi = qi 
        self.nr_ap = nr_artigos_publicados
    
    def __str__(self):
        return f"QI: {self.qi} e Publicações: {self.nr_ap}"
    def __add__(self, other):
        qi_total = (self.qi-100)+(other.qi-100) + 100
        publicacoes_acumuladas = self.nr_ap + other.nr_ap
        return Aluno(qi_total, publicacoes_acumuladas)
    def __gt__(self, other):
        if self.qi >other.qi:
            return True
        elif self.qi == other.qi:
            return self.nr_ap > other.nr_ap 
        else:
            return False
aluno_1 = Aluno(120, 1)
aluno_2 = Aluno(120, 2)
super_aluno = aluno_1 + aluno_2
# super_aluno = aluno_1.__add__(aluno_2)

print(aluno_1)
print(aluno_2)
print(super_aluno)

if aluno_1>aluno_2:
    print("Selecionar aluno 1")
else:
    print("Selecionar aluno 2")