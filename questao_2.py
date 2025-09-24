from typing import List, Sequence
import unittest

def converter_celsius_para_fahrenheit(lista: Sequence[float])-> Sequence[float]:
    """Converte uma sequencia de temperaturas em celsius para fahrenheit

    Args:
        lista (list): A lista de numeros que sera enviada a funcao em graus Celsius

    Returns:
        list: A lista de numeros convertidos em Kelvins
    
    Examples:

    """
    arr = []
    for i in lista:
        if isinstance(i,(float, int)):
            F = i * (9/5) + 32
            arr.append(F)
        else:
            print("Escreva uma lista de numeros")
    return arr
        
#driver code
print(converter_celsius_para_fahrenheit([10,20,30]))

print(ord("z"))