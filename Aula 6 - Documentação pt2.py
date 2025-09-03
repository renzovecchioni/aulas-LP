# # Ao invés de usar um "#", usando o """, significa que é um comentário especial, ou melhor, documentar.
"""Módulo de Matemática Financeira 
    Documentação de múltiplas linhas
    Documentação de múltiplas linhas
    Documentação de múltiplas linhas"""
    
# Função calcula montante e juros em um regime de juros simples
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple: # Reforça que capital, taxa e tempo devem ser inteiros e que o retorno é uma tupla. Não é restritivo, não influencia diremente o código, apenas indica ao usuário a preferência de dados.
    # Fórmula padrão de juros simples
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    # Fazer: Utilizar números de ponto flutuante nesta função
    
    return (montante, juros)

# Docstring NumPy/SciPy
def juros_compostos(capital: int, taxa: int, tempo: int = 1) -> tuple:
    # "Documentar" o código daqui para frente será essencial - basta adicionar três aspas duplas e dar enter no espaço abaixo da função:
    """Cálculo de juros compostos
    

    Parameters
    ----------
    capital : int
        Valor inicial utilizado para a base do cálculo.
    taxa : int
        Taxa de juros
    tempo : int, optional
        Tempo total. The default is 1.

    Returns
    -------
    tuple
        Uma tupla com montante e os juros, nesta ordem
            

    """
    # O montante representa o capital elevado a um valor definido pela taxa/tempo
    montante = capital*pow((1 + taxa/100), tempo)
    
    juros = montante - capital
    
    return(round(montante, 2)), round(juros, 2)
