texto = " EMAp "
print(texto.strip())

nome_metodo = "strip"

print("Todos os métodos disponíveis para uma string:")
print(dir(texto))
print("=" * 130)

# O comando "hasattr" verifica se existe o método "nome_metodo" dentre os métodos possíveis de "texto"
if hasattr(texto, nome_metodo):
    print(":)")
else:
    print(f"O método {nome_metodo} NÃO EXISTE")


# O getattr então basicamente vincula o método "strip" ao texto passado, tornando a variável metodo = texto.strip
# Em seguida, ao chamar texto = metodo(texto), estamos fazendo: texto.strip(texto), ou seja, texto.strip(" EMAp "), basicamente passando ao programa para retirar de " EMAp " todos os caracteres de " EMAp " encontradas na variável texto.
# Como isso é justamente o texto, ele remove tudo. Como tudo foi excluído, o print retornará somente o "kd?"
# O nome desse tipo de método é "Método Ligado"
if hasattr(texto, nome_metodo):
    metodo = getattr(texto, nome_metodo) 
    texto = metodo(texto) 

    print(texto, "kd?")
else:
    print(f"O método {nome_metodo} NÃO EXISTE")
