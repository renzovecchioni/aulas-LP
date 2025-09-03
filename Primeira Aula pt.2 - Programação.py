# Antes fazíamos assim:
quadrados = []
for i in range(10):
    quadrados.append(i**2)
print(quadrados)

# Outra possibilidade - não recomendado:
quadrados = [i**2 for i in range(10)]
print(quadrados)

matriz = [[1,2], [3,4]]
matriz_achatada_trad = []

# Tradicionalmente fazemos assim:
for cada_linha in matriz:
    for cada_elemento in cada_linha:
        matriz_achatada_trad.append(cada_elemento)
print(matriz_achatada_trad)

# Podemos fazer assim - não recomendado:
matriz_achatada = [elem for linha in matriz for elem in linha]
print(matriz_achatada)

# Exemplo - demonstra como é confuso o código escrito dessa forma condensada:
valores = [10,-2,3,-1,0]
negativos = [abs(x) for x in valores if x < 0]
print(negativos)

letras = "banana"
conj_letras = {letra for letra in letras}
print(conj_letras)

numeros = [1,2,3,4]
quadrados = {n: n**2 for n in numeros}

print(quadrados)