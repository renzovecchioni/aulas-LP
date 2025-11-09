class Foo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
    def public_method(self):
        print("Ola, eu sou o metodo publico")
        self._protected_method()
        self.__private_method()
    def _protected_method(self):
        print("Ola, eu sou o metodo protegido")
        self.__private_method()
    def __private_method(self):
        print("Ola, eu sou o metodo privado")

class Bar(Foo):
    #nao se passa atributo privado por heranca 
    def usando_os_metodos_do_papai(self):
        super()._protected_method()
        super()._Foo__private_method() #Erro semantico


    







#driver code 

'''object_ = Foo()
print(object_.public)
object_.public_method()

#ERRO SEMANTICO
print(object_._protected)
object_._protected_method()

#ERRO SEMANTICO * ERRO SEMANTICO
print(object_._Foo__private)
object_._Foo__private_method()'''

object_ = Bar()
print(object_.public)
object_.public_method()
print(object_._protected)
object_.usando_os_metodos_do_papai()


#ERRO SEMANTICO 
object_._protected_method()

#ERRO SEMANTICO * ERRO SEMANTICO

print(object_._Foo__private)
# print(object_._Bar__private)
