# Para desempacotar, é necessário que a quantidade de valores informados seja igual a quantidade de valores na tupla
tupla = (10,20,30)
a,b,c = tupla
print(a,b,c)

# Podemos usar o símbolo "*" para empacotar valores em uma variável
tupla = (10,20,30,40,50)
a,*b,c = tupla
print(a,b,c)

# O símbolo "_" é utilizado para demonstrar que os valores não serão utilizados
tupla = (10,20,30,40,50)
a,b,*_ = tupla
print(a,b) # Nesse caso, somente "a" e "b" importam, logo, os valores posteriores à ele não importam, por isso o "_"

# "Driver Code" - É essa parte da função
def somar_tudo(*numeros):
    return sum(numeros)
########################################
print(somar_tudo(1,2,3,4,5,6,7,8,9,10))

def somar_tudo(*numeros):
    return a+b+c
numeros = [1,2,3]
print(somar_tudo(*numeros))

def apresentar(nome,idade):
    return f"{nome} tem {idade} anos"
pessoa = {"nome": "Arthur", "idade": 18}
print(apresentar(**pessoa)) # Desempacotando a variável "pessoa", o primeiro argumento funciona como o primeiro argumento da função, no caso "nome" e a segunda como segunda, no caso "idade"

def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave} = {valor}")
mostrar_info(nome="Arthur", idade=18) # Essa linha define as variáveis da função anterior

d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}

d3 = {**d1, **d2} # Desempacotando os valores, os valores vão se sobrepor, sendo o valor adicionado depois o predominante
print(d3)

# "args" são argumentos não nomeados e "kwargs" são os argumentos nomeados
def relatorio(*args, **kwargs):
    print("Participantes:")
    for nome in args:
        print(f" - {nome}")
    for chave, valor in kwargs.items():
        print(f" - {chave}: {valor}")
        
relatorio("Ana", "Arthur", "Yuri", tema="Anime", duracao="2h")

    

