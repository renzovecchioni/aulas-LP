# Cadeia/hierarquia de erros: Sistema Operacional - Interpretador - Driver Code - Função1 - Função2
# No caso da hierarquia, o Sistema Operacional é o "topo", responsável por chamar o Interpretador, que chama o Driver Code, e assim por diante.
# Se ocorre um erro na Função2, por exemplo, ela tem a chance de tentar resolver/acusar. Caso não consiga, passa para a Função1 tentar resolver. Caso não consiga, Driver Code, depois Interpretador e, por último, o Sistema Operacional.
# Caso o Sistema Operacional identifique o erro, ele simplesmente encerra o programa, pois identifica o Interpretador como não capaz de identificar/resolver problemas.
# Erros podem ser: Sintático ou Erro. 

#x = 10
#resultado = x/y # Isso aqui dá erro, pois y não existe. Essa é uma linha problemática.
#print(resultado)

# Para casos como esse, podemos fazer possibilidades pro caso de exceção. Tente "tal" se não for, então é exceção.
x = 10
y = 0

try:
    resultado = x/y
except Exception as erro: # Podemos colocar o exception como o erro. Já que é o mais genérico, caso exista erro, ele identifica e especifica com o "type(erro)"
    print("Ocorreu uma exceção! Cuidado!", type(erro)) 
    resultado = "Feito para saber qual foi o erro específico!"
#except ZeroDivisionError as erro:
 #   print("Ocorreu uma exceção! Cuidado!", type(erro)) # O "type(erro)" nos confirma o tipo de erro
  #  resultado = "Divisão por 0!" # Definimos a variável "resultado" para os dois casos, apesar de, nesse caso, ela ser intitulada como "não existente", já que é exceção.
except NameError as erro: # Erro acontece quando a variável não está definida
    print("Ocorreu uma exceção! Cuidado!")
    resultado = "NameError"
except ArithmeticError as erro: # Erros mais genéricos devem ficar por baixo, haja vista que, quanto mais especificado nosso erro, mais fácil de identificá-lo e resolvê-lo.
    print("ArithmeticError", type(erro), erro.__class__.mro()) # Mesmo sendo uma classe de erros genérica, o "type(error)" sabe qual o tipo de erro específico dentro do grupo e indica-o corretamente.
    resultado = "Erro aritmético"
# O "mro" utilizado nesse caso, serve para ver a "árvore genealógica" do erro, sendo possível ver os grupos que contém/estão contidos no grupo/objeto. 
# É importante ressaltar que, apesar de existirem "erros filhos", ou seja, específicos dentro de grupos, o erro mais específico é TAMBÉM o erro geral, não um erro diferente. Lembre-se: o "pai" não é o "filho", porém o "filho" é o "pai". 
# Nesse caso abaixo, todas as exceções/erros são colocadas nesse "pacote". O "except" geral deve ficar por último, já que todos os erros estão dentro dele.
except: 
    print("Ocorreu uma exceção! Cuidado!", type(erro), erro.__class__.mro())
    resultado = "Variável não existe!"
print(resultado)

# Existem hierarquias de erros. O "except" é o caso genérico, que pega todos os erros. Dentro dos erros possíveis, existe o "ArithmeticError" por exemplo, que contém erros de "float", "divisão por zero", etc.

