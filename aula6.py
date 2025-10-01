# Podemos importar o arquivo que indica a função de juros simples:
import modulo

capital_1 = 23
taxa_1 = 1
tempo_1 = 4

capital_2 = 231
taxa_2 = 1
tempo_2 = 4

# Ao digitar "print(modulo)" vamos visualizar a "docstring" de 1 linha presente no arquivo original: " Módulo de Matemática Financeira "
# Ao digitar "print(modulo.)" vamos visualizar a função "juros_simples" presente no arquivo original
print(modulo.juros_simples(capital_1, taxa_1, tempo_1))

print(modulo.juros_compostos(capital_2, taxa_2, tempo_2))
