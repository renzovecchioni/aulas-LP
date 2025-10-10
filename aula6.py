# Podemos importar o arquivo que indica a função de juros simples:

"""Módulo de Matemática Financeira""" # Ao invés de usar um "#", usando o """, significa que é um comentário especial, ou melhor, documentar.

# Função calcula montante e juros em um regime de juros simples
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple: # Reforça que capital, taxa e tempo devem ser inteiros e que o retorno é uma tupla. Não é restritivo, não influencia diremente o código, apenas indica ao usuário a preferência de dados.
    # Fórmula padrão de juros simples
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    # Fazer: Utilizar números de ponto flutuante nesta função
    
    return (montante, juros)


capital = 23
taxa = 1
tempo = 4

# Ao digitar "print(modulo)" vamos visualizar a "doc stream" de 1 linha presente no arquivo original: " Módulo de Matemática Financeira "
# Ao digitar "print(modulo.)" vamos visualizar a função "juros_simples" presente no arquivo original
print(juros_simples(capital, taxa, tempo))

capital_1 = 23
taxa_1 = 1
tempo_1 = 4

capital_2 = 231
taxa_2 = 1
tempo_2 = 4

# Ao digitar "print(modulo)" vamos visualizar a "docstring" de 1 linha presente no arquivo original: " Módulo de Matemática Financeira "
# Ao digitar "print(modulo.)" vamos visualizar a função "juros_simples" presente no arquivo original
print(juros_simples(capital_1, taxa_1, tempo_1))

def juros_compostos():
    ...
print(juros_compostos(capital_2, taxa_2, tempo_2))