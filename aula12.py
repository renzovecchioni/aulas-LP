import time
from functools import wraps

def retry(retries=3,exceptions=(ValueError,), delay=0.1, backoff=1.0):
    # validacao basica de parametro
    if not isinstance(retries, int) or retries <1:
        raise ValueError("Retries deve ser int e maior igual a 1")
    if not isinstance(delay, (int, float)) or delay <0:
        raise ValueError("delay deve ser int ou float e >=0")
    if not isinstance(backoff, (int, float)) or backoff<1:
        raise ValueError("o 'backoff' deve ser int ou float e >=1")
    if not isinstance(exceptions, tuple):
        exceptions = (exceptions,)
    for exc in exceptions:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)):
            raise TypeError("Parametro: exceptions deve conter classes derivadas de BaseException")
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tentativa_atual = 1
            atraso_atual = float(delay)
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if tentativa_atual >= retries:
                        raise err
                    nome_erro = type(err).__name__
                    msg = str(err)
                    print(f"Tentativa {tentativa_atual} falhou: ({nome_erro}: {msg}), tentanto outra vez em {atraso_atual:.3f}s")

                    if atraso_atual>0:
                        time.sleep(atraso_atual)
                    tentativa_atual+=1
                    atraso_atual*=backoff
        return wrapper
    return decorador

contador_falhas = 0

# O decorador tentara 3 vezes, aguardando 0,1s antes de tentar novamente. Caso tenha erro informado, ele informa para o codigo. O "backoff" eh a quantidade de tempo que ele ira incrementar 
@retry(retries=3,exceptions=(ValueError,), delay=0.1, backoff=2)
def pode_falhar():
    global contador_falhas
    if contador_falhas<2:
        contador_falhas+=1
        raise ValueError("Deu ruim")
    return "deu bom"

print(pode_falhar())

