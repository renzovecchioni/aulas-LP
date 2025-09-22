import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])
A = a.copy()
A[0:] = 42
print(A)

array = np.arange(1, 13)
print(array)

mat = array.reshape((3, 4))
print(mat)

c_flat = mat.flatten()
print("Flatten, estilo C:", c_flat)

f_flat = mat.flatten(order="F")
print("Flatten, estilo Fortran:", f_flat)

mat_ravel = mat.ravel()
print("Ravel: ", mat_ravel)

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Empilhamento vertical", np.vstack([a, b]))
print("Empilhamento horizontal", np.hstack([a, b]))

c = np.arange(10)

print("Array base:", c)
print("Split em 3 partes iguais:", np.split(c, [3, 6]))

np.savetxt("dados.csv", mat, delimiter=",", fmt="%d")
print("Dados salvos")

dados_carregados = np.loadtxt("dados.csv", delimiter=",", dtype=int)
print("Matriz carregada\n", dados_carregados)


dados = np.genfromtxt(
    "dados_01.txt",
    delimiter=None,
    dtype=None,
    names = True, 
    encoding="utf-8", 
    missing_values="-",
    filling_values=np.nan
    )

print(dados)
print("Nome da segunda coluna", dados["nome"][1])

# dados = np.loadtxt("exemplo.csv", delimiter=",", dtype=float, skiprows=3, usecols=(1,2))
# print("Matriz carregada\n", dados)