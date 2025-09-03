import warnings
import math

def funcao_antiga(valor: float) -> float:
    """ [ DEPRECATED ] funcao_antiga: use "math.sqrt" (coloca-se a função a ser utilizada no lugar da antiga)
    Esta função será removida na versão futura da aplicação.
    """
    warnings.warn(
        "Função antiga está deprecada e será removida na versão futura. Use \"math.sqrt\""
        category=DeprecationWarning,
        stacklevel=2
)
    return math.sqrt(valor)

print("funcao_antiga(16):", funcao_antiga(16))

