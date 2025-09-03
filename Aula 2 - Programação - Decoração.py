# Isso nós já fizemos:
def saudador(pessoa):
    saudacao = "Bem-vindo"
    return f"{saudacao}, {pessoa}"
# Driver Code - Código que faz a aplicação da função
print(saudador("João"))

# Agora veremos funções dentro de funções: 
def saudador(pessoa):
    saudacao = "Bem-vindo"
    
    def mensagem():
        return f"{saudacao}, {pessoa}"
    return mensagem
# Driver Code - Código que faz a aplicação da função
#print(saudador.__code__)
#print(dir(saudador.__code__))

print(saudador.__code__.co_consts)
print(dir(saudador.__code__.co_consts))
print(hasattr(saudador.__code__.co_consts, "__iter__")) # Então é "iterável"
print(hasattr(saudador.__code__.co_consts, "__next__")) # Mas não é "iterador"

for cada_constante in saudador.__code__.co_consts:
    if isinstance(cada_constante, type(saudador.__code__)):
        print(f"Função interna detectada: {cada_constante.co_name}")

# Agora nós podemos criar funções personalizadas de acordo com os parâmetros que passamos. Nesses casos aqui, eles só retornarão "Ana" e "João".
mensagem_ana = saudador("Ana")
mensagem_joao = saudador("João")
print(mensagem_ana())
print(mensagem_joao())
        