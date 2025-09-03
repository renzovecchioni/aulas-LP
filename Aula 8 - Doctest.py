import doctest
def soma(num1, num2):
    """
    
    # Esse tipo de documentação auxilia o leitor a entender o código. É interessante o uso de exemplos quando a função é complexa.
    Soma dois números inteiros
    
    :param num1: int
    :param num2: int
    :return: int
    
    >>> soma(7,0)
    7
    
    >>> soma(42,666)
    708
    
    >>> soma(-13,10)
    -3
    
    >>> soma(100, "Carlos Ivan")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    # O "doctest" testa e verifica que o 3° caso deu errado, o esperado era -3 e o resultado está como -4. Caso não tenha nenhum erro o programa roda normalmente.
    return num1 + num2
# Driver Code:
print(soma(1,1))

if __name__ == "__main__":
    doctest.testmod(verbose=True) #Testa e verifica os casos da documentação. Se "resposta documentação" = "resposta esperada" o teste passa. Se não, ele acusa o erro.
    #soma(100, "Carlos Ivan") # Demos o comando e descobrimos o tipo de erro para colocar na documentação.