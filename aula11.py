import numpy as np 
print("versao numpy:", np.__version__)
array_1 = np.array([1,2,3])
array_2 = np.array([[1,2,3],[4,5,6]])

print("Array 1:", array_1)
print("Array 2:\n", array_2)
#Propriedades dos NDarrays
print("Formato (shape)")
print("1D", array_1.shape)
print("2D", array_2.shape)
print("Tamanho (size)")
print("1D", array_1.size)
print("2D", array_2.size)
print("Tipo dos dADOS (dtype)")
print("1D", array_1.dtype)
print("2D", array_2.dtype)
print("Numero de dimensoes (ndim)")
print("1D", array_1.ndim)
print("2D", array_2.ndim)
### Criacao de NDarrays
print("Zeros:\n", np.zeros((2,3)))
print("Uns:\n", np.ones((2,3)))
print("Cheio:\n", np.full((5,5), 42))
print("ARange:\n", np.arange(0,10,2))
print("Linspace:\n", np.linspace(0,1,5))
print("Random:\n", np.random.rand(2,2))
matriz = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(matriz)
print("Elemento da Linha 1, coluna 2:", matriz[0,1])
print("Primeira linha:", matriz[0])
print("SeguNDA COLUNA :", matriz[:,1])
print("Submatriz linhas 0-1, colunas 1-2:\n", matriz[0:2, 1:3])
print("Ultima linha", matriz[-1])
print('Ultima coluna:', matriz[:, -1])

### Operacoes em NDarrays

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print("Soma elemento a elemento:\n", x+y)
print("Multiplica elemento a elemento:\n", x*y)
print("Produto matricial (dot product)\n", x@y)
print("Transposta de X:\n", x.T )
print("Soma total dos elementos\n", np.sum(x))
print("Soma por colunas de x:\n", np.sum(x, axis=0))
print("Soma por linhas de x:\n", np.sum(x, axis=1))

### Estatistica em NDarrays

data = np.random.randint(1, 100, size=10)
print("ND array aleatorio", data)
print("Media", np.mean(data))
print("Desvio padrao:", np.std(data))
print("Valor maximo: ", np.max(data))
print("INdice do valor maximo", np.argmax(data))


### Indexacao Booleana e condicional em NDarray

array_  = np.array([10,15,20,25,30])
print("ARRAY: ", array_)
print("Valores maiores que 20:", array_[array_ > 20])
print("Valores pares:", array_[array_ %2==0])