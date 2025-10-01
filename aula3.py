# Para além das exceções existentes no Python, podemos também criar nossas próprias exceções:

class AppError(Exception):
    """Raíz dos erros de domínio da aplicação"""
    
class AuthenticationError(AppError):
    """Falha de Autenticação (Identidade Inválida)"""
    
class AuthorizationError(AppError):
    """Falha de Autorização (Permissão Inválida)"""
    
class RateLimitExceededError(AppError):
    """Cliente excedeu o limite de requisições permitidas"""

class ResourceNotFoundError(AppError):
    """Recurso solicitado não foi encontrado"""
    
def demo_heranca():
    erro = AuthorizationError("Acesso negado a recurso")
    print(erro.args)
    print(str(erro))
    
    classes = [cls.__name__ for cls in erro.__class__.mro()]
    print(classes)
    
    print(hasattr(erro, "__cause__"))
    print(hasattr(erro, "__context__"))
    print(hasattr(erro, "__traceback__"))

def mock_obter_recurso(simular):
    if simular == "authn":
        raise AuthenticationError("Credenciais Inválidas")
    if simular == "authz":
        raise AuthorizationError("Sem permissão para essa operação")
    if simular == "limit":
        raise RateLimitExceededError("Limite de requisições excedido")
    return "Outro erro"

def demo_ordem_erros(simular): # Função que acessa uma função que conecta-se a um banco de dados. Esse tipo de função é extremamente perigosa, deve-se ter atenção.
    try:
        resultado = mock_obter_recurso(simular) # Mock: tipo de técnica usada para simular o comportamento real das funções/objetos. Ele é extremamente importante.
        print(resultado)
    except AuthenticationError as err:
        print("Fiz um tratamento de erro para (authn):", err)
    except AuthorizationError as err:
        print("Fiz um tratamento de erro para (authz):", err)
        # Poderíamos também não separar as exceções "Authorization" e "Authentication", usando tuplas:
    # except (AuthenticationError, AuthorizationError) as erro:
        # print("Exceção de autorização e autenticação juntos)
    except RateLimitExceededError as err: # Caso não queira separar uma exceção de forma específica, basta retirar o código da exceção especificada.
        print("Fiz um tratamento de erro para (limit):", err)
    except AppError as err:
        print("Fiz um tratamento de erro para qualquer AppError:", err)
    else: # O "else" só vai rodar caso não existam exceções. Em caso de existência de exceção, o else não será executado.
        print("Estou fazendo operações após o sucesso de execução")
    finally: # Mesmo em caso de exceção, o "finally" será executado. Pode-se perceber que ele aparece em todos os "prints" dos testes de mock.
        print("Eu sempre sou EXECUTADO") # O "finally" é usado, por exemplo, em sistemas operacionais: quando o sistema fecha um aplicativo que não estamos usando mais / bancos de dados em um banco, por exemplo, que desloga automaticamente da nossa conta após certo tempo/certas operações
# Casos como esses citados acima, devem acontecer SEMPRE, por isso o finally é usado, para que aconteça em todos os casos.

def buscar_em_armazenamento(chave, dicionario):
    try:
        return dicionario[chave]
    except KeyError as err: # Exceções às vezes podem ser "levantadas" mas não resolvidas corretamente, haja vista que um programa pode "mostrá-la" porém não especificamente.
        print("Eu estou tratando um pouquinho da exceção")
        raise ResourceNotFoundError(f"Chave ausente: {chave!r}") from err # Para evitar isso, podemos usar o "raise" dentro do "except", ou seja, no caso de exceções de "KeyError", destacamos se ele é um "ResourceNotFoundError"
buscar_em_armazenamento

def demo_encadeamento():
    dados = {"login_ativo": True}
    try:
        buscar_em_armazenamento("Carlos Ivan", dados)
    except ResourceNotFoundError as err:
        print("\nEncadeado:", err)
    if err.__cause__ is not None: # Enquanto uma causa tem uma outra causa, sabemos que essa causa não foi o 1° erro. Se ela for a "última" causa, ela é o erro original.
        print("Causa original:", (err.__cause__).__class__.__name__, " ", err.__cause__)
demo_encadeamento()

if __name__ == "__main__":
    demo_heranca()

for cada_caso in ["authn", "authz", "limit", "ok"]: # Linha de teste para cada caso
    print(f"\nCaso: {cada_caso}")
    demo_ordem_erros(cada_caso)
    
