import inspect
from functools import wraps

def enforce_types(func):
    assinatura = inspect.signature(func)
    print("Assinatura: ", str(assinatura))

    anotacoes = func.__annotations__
    print("Anotacoes:", anotacoes)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = assinatura.bind(*args, **kwargs)
        bound.apply_defaults()
        print("Bound:", str(bound))
        print("Bound Arguments:", str(bound.arguments))
        for nome_param, valor in bound.arguments.items():
            if nome_param in anotacoes:
                tipo_esperado = anotacoes[nome_param]
                if not isinstance(tipo_esperado, type):
                    raise TypeError(f"Anotacao para \"{nome_param}\" utiliza tipo nao suportado")
                if not isinstance(tipo_esperado, type):
                    raise TypeError(f"Argumento\"{nome_param}\" esperado: \"{tipo_esperado!r}\", argumento recebido: \"{type(valor)!r}\"")
        resultado = func(*args, **kwargs)

        if "return" in anotacoes:
            tipo_retorno = anotacoes["return"]
            if not isinstance(tipo_retorno, type):
                raise TypeError("Anotacao de retorno utiliza tipo nao suportado")
            if not isinstance(resultado, tipo_retorno):
                raise TypeError("Argumento esperado nao suportado")

        return resultado
    return wrapper

#### driver code

@enforce_types
def concatena(texto_esquerda: str, texto_direita:str)->str:
    return texto_esquerda+texto_direita

@enforce_types
def area_retangulo(base:float, altura:float)->float:
    return base*altura

print(concatena("Eu adoro", " a EMAP"))
print(area_retangulo(3.0, 42.0))

