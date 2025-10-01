import warnings
import math
import sys
import textwrap
import argparse

from typing import Sequence, TypeAlias

def juros_compostos():
    pass

def funcao_antiga(valor: float)->float:
    warnings.warn(
        """Funcao antiga esta deprecada e sera removida na versao futura, use /'math.sqrt/'""",
        category = DeprecationWarning,
        stacklevel = 2
    )
    return math.sqrt(valor)

def executar_cli(lista_argumentos: Sequence[str])->int:
    """ Executa a CLI de demonstracao"""
    parser_principal = construir_parser()
    argumentos = parser_principal.parse_args(lista_argumentos)

    if argumentos.nome_comando == "simples":
        montante, juros = juros_simples(argumentos.capital, argumentos.taxa_percentual, argumentos.periodo)
        print(f"Montante: {montante:.2f} e juros: {juros:.2f}")
    else:
        parser_principal.erro("Subcomando desconhecido")
    return 0

def juros_simples():
    pass


print("funcao_antiga(16):", funcao_antiga(16))

def construir_parser() -> argparse.ArgumentParser:
    """ Cria um parser de linha de comando para demonstração

    Retorna um parser com subcomandos
    - simples: calcula juros simples
    """
    parser_principal = argparse.ArgumentParser(
        prog = "Aula documentação",
        description="Exemplo de CLI documentada utilizando argparse",
        formatter_class=argparse.RawDescriptionlpFormatter,
        epilog=textwrap.dedent(
            """ 
            Exemplos:
                python doctest.py simples --capital 1000 --taxa 5 --tempo 2
            """
        )
    )
    subcomandos = parser_principal.add_subparsers(dest="nome_comando", required=True)
    parser_simples = subcomandos.add_parser("simples", help="Calcula montante e juros_simples")
    parser_simples.add_argument("--capital", type=float, required=True, help="...")
    parser_simples.add_argument("--taxa", type=float, required=True, help="...")
    parser_simples.add_argument("--tempo", type=float, required=True, help="...")

    return parser_principal

def main()->int:
    pass

__version__ = "2.0.1"

if __name__ == "__main__":
    print("Versao do modulo: ", __version__, "\n")
    raise SystemExit(main())


#TODO: fazer duas funcaoes e revisar, constantes iguais em todo o programa, fazer funcao main() que executa CLI