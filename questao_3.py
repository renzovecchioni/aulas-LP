def e_palindromo(palavra: str)-> str:
    """_summary_

    Args:
        palavra (str): palavra que sera verificada se sera palindromo

    Returns:
        str: frase indicando se eh ou nao eh palindromo

    
    """
    try:
        tam = len(palavra)-1
        for indice, letra in enumerate(palavra):
            if letra == palavra[tam-indice]:
                pass
            else:
                return "Nao eh palindromo"
        return "Eh palindromo"
    except TypeError as err:
        print("EScreva uma palavra ou frase para saber se eh ou nao palindromo")

#driver code
print(e_palindromo("ovo"))
print(e_palindromo("sorvete"))