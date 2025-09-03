# Nesse caso, atribuímos duas variáveis olhando para o mesmo espaço de memória. Isso pode ser percebido olhando o número de ID que, nesse caso, são iguais. 

lista_original = [1,2,3]
lista_alias = lista_original
print("ID lista original:".ljust(20, " "), id(lista_original))
print("ID lista alias:".ljust(20, " "), id(lista_alias))

# Alterando uma, alteramos a outra, haja vista que estamos olhando para o mesmo espaço de memória:
    
lista_alias[0] = 99
print(lista_original)
print(lista_alias)

# 

import copy
perfil_aluno = {
    "nome": "João",
    "idade": 18,
    "preferencias": ["filmes", "música", "livros"]}
perfil_aluno_shallow = perfil_aluno.copy() # Cópia direta do objeto, mais adequado.
# perfil_aluno_shallow = copy.copy(perfil_aluno) - Outra opção de cópia, menos comum e menos adequado. É uma função.


# Podemos, ao copiar, modificar superficialmente os objetos sem alterar o projeto original.
perfil_aluno_shallow["idade"] = 40
print(perfil_aluno)
print(perfil_aluno_shallow)

# Perceba que, ao tentarmos alterar o objeto de cópia em um nível interior, o original também é alterado. A cópia utilizada é uma cópia rasa.
perfil_aluno_shallow["preferencias"][0] = "Teatro"
print(perfil_aluno)
print(perfil_aluno_shallow)

# Por conta disso, utilizamos a cópia profunda, a "Deep Copy". Essa cópia consegue alterar num nível interior, sem alterar o objeto original.
perfil_aluno_deep = copy.deepcopy(perfil_aluno)
perfil_aluno_deep["idade"] = 40
perfil_aluno_deep["preferencias"][0] = "Teatro mudo"
print(perfil_aluno)
print(perfil_aluno_shallow)
print(perfil_aluno_deep)

numeros = [10, 20, 30, [1,2,3]]
numeros_copia = numeros[:] # Podemos copiar com o slice, haja vista que, dessa forma, o slice está indo do "início" ao "fim".
print(numeros)
print(numeros_copia)

# Podemos alterar superficialmente os objetos.
numeros_copia[0] = 99
print(numeros)
print(numeros_copia)

# Apesar disso, é imprescindível perceber que esse tipo de cópia é "Shallow", ou seja, uma cópia rasa, resultando no mesmo problema que vimos anteriormente usando o ".copy()"
numeros[3][0] = 99
print(numeros)
print(numeros_copia)