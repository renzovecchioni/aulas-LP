def diga_ola(): 
    return "Olá" # Usar o return torna a função menos restrita - permite fazermos outras coisas com o retorno

def diga_ola():
    print("Olá") # Usar o print torna a função mais restrita - apenas printa


def meu_decorador(funcao_original):
    def nova_funcao():
        print("Algo antes da função...")
        funcao_original()
        print("Algo depois da função")

    return nova_funcao

def diga_tchau():
    print("Tchau!")

@meu_decorador # O "@" é usado para indicar decoradores no código. Ele usa o código de decorador na função abaixo dele.
def diga_tudo_bem():
    print("Tudo bem?")

diga_ola()
diga_tchau()

# Decoradores são, basicamente, funções "decoradas"/"pré-prontas". Vinculamos uma função nova em uma existente de acordo com a variável que for de nosso interesse.
diga_ola_decorada = meu_decorador(diga_ola)
diga_tchau_decorada = meu_decorador(diga_tchau)
diga_ola_decorada()
print("#"*60)
diga_tchau()
diga_tchau_decorada()
print("#"*60)
diga_tudo_bem()