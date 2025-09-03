import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executada em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper    
    
@medir_tempo
def tarefa_lenta():
    time.sleep(5)
    return "Concluída"

print(tarefa_lenta())