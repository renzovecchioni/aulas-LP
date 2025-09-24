def contar_vogais(palavra: str)-> int:
    """conta as vogais de uma string

    Args:
    -------------
        palavra (str): a palavra que sera enviada a função

    Returns:
    --------------
        int: numero de vogais da palavra

    Example:
    --------------
        >>> contar_vogais("palavra") 
        3
        >>> contar_vogais("AEIOU")
        5
        >>> contar_vogais(7)
        A palavra deve ser uma string
    """
    try:
        count = 0
        for i in palavra:
            i = i.lower()
            if i in 'aeiou':
                count+=1
        return count
    except TypeError as err:
        print("A palavra deve ser uma string")

#driver code
print(contar_vogais("palavra")) # return 3
print(contar_vogais("AEIOU")) # return 5
print(contar_vogais(7)) # return A palavra deve ser uma string
