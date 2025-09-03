def aplicar(objeto, nome, *args, **kwargs):
    if not hasattr(objeto, nome): # Verificar se tem o método
        raise AttributeError(f"{type(objeto).__name__} não tem {nome}") # Raise: "levanta" o erro. Se o erro não for "cortado", o programa é encerrado.
    
    atributo = getattr(objeto, nome) # Atributo é uma "função" que aplica o método "nome" na variável "objeto"
    # Callable: se um método existe e pode ser "invocado" pelo getattr, ele é chamado de "callable"
    
    if callable(atributo): 
        return atributo(*args, **kwargs)
    
    raise TypeError(f"{nome} não é invocável em {type(objeto).__name__}") # Se não for "invocável", ou seja, não for "callable", então "levante" o erro.
    
# Driver Code - Feito primeiramente: começar com o nosso "objetivo", exemplos ou problemas, diminui a chance de erro. Basicamente nos indica aonde queremos chegar.
texto_1 = "  EMAp  "
texto_2 = "banana"

print(aplicar(texto_1, "strip")) # Deve funcionar
# print(aplicar(texto_1, "stripa")) # Deve falhar, "stripa" não existe. A partir dessa linha nada será executado pois o programa foi cortado pelo sistema operacional.
print(aplicar(texto_2, "replace", "a", "@"))