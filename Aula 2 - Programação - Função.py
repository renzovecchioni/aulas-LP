def exibir_evento(mensagem):
    print("Evento:", mensagem)

# Se não existe o objeto, ele será criado dentro da função, que é um dicionário.
exibir_evento.contador = 0
exibir_evento.log = []
print(exibir_evento.__dict__)

def registrar_evento(mensagem):
    exibir_evento.contador += 1
    exibir_evento.log.append(mensagem)
    exibir_evento(mensagem)
    print(f"Chamadas até agora: {exibir_evento.contador}")
    print(f"Histórico: {exibir_evento.log}")
    
registrar_evento("Sistema iniciado")
registrar_evento("Usuário autenticado")
registrar_evento("Navegador iniciado")
registrar_evento("Instagram acessado")                 
    
