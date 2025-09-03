"""Módulo de Matemática Financeira""" # Ao invés de usar um "#", usando o """, significa que é um comentário especial, ou melhor, documentar.

# Função calcula montante e juros em um regime de juros simples
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple: # Reforça que capital, taxa e tempo devem ser inteiros e que o retorno é uma tupla. Não é restritivo, não influencia diremente o código, apenas indica ao usuário a preferência de dados.
    # Fórmula padrão de juros simples
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    # Fazer: Utilizar números de ponto flutuante nesta função
    
    return (montante, juros)


