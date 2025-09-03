texto = " EMAp "
print(texto.strip())

nome_metodo = "strip"

print("Todos os métodos disponíveis para uma string:")
print(dir(texto))
print("=" * 130)

if hasattr(texto, nome_metodo):
    print(":)")
else:
    print(f"O método \"{nome_metodo}\" NÃO EXISTE")

if hasattr(texto, nome_metodo):
    metodo = getattr(texto, nome_metodo)
    texto = metodo(texto)
    print(texto, "kd?")
else:
    print(f"O método \"{nome_metodo}\" NÃO EXISTE")