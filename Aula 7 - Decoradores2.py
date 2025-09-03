from functools import wraps
def log_args(func):
    """
    DECORADOR
    
    Parameters
    ----------
    func : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    @wraps(func) # Colocar o @wraps(func) faz a função subtrair virar a "própria" decorada. Ou seja, ela possui seu próprio nome e seu próprio doc string, mesmo sendo decorada.
    def wrapper(*args, **kwargs):
        """
        DECORADOR INTERNO

        Parameters
        ----------
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        print(f"Chamando função {func.__name__} com args = {args} e kwargs = {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def dobrar_retorno(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2
    return wrapper
    
@log_args # Lembre-se: o "@" serve para chamar o decorador e vincular a função abaixo dela na função decoradora.
@dobrar_retorno # O decorador mais próximo é o que será utilizado.
def somar(a, b):
    return a + b
print("Resultado:", somar(1,41))

@log_args
def subtrair(a,b):
    """
    SUBTRAIR

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return a - b

print("Resultado:", subtrair(43,1))
print(subtrair.__name__) # A função decorada irá possuir o nome da decoradora, nesse caso, wrapper.
print(subtrair.__doc__) # É possível confirmar isso ao pegar o "doc string" e ver que o "decorador interno", colocado em wrapper, aparece.
# Para alterar isso, adicionamos o @wraps(func) antes da função "wrapper".