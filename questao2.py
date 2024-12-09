import time
import random


def ordenar_lista(lista):
    inicio = time.time()
    lista_ordenada = sorted(lista)
    fim = time.time()
    tempo_execucao = fim - inicio
    return lista_ordenada, tempo_execucao



# Gerando uma lista com 5 milhões de elementos aleatórios
lista = [random.randint(0, 1000000) for _ in range(5000000)]

# Ordenando a lista
lista_ordenada, tempo_execucao = ordenar_lista(lista)
print(f"Lista ordenada com sucesso! Tempo de execução: {tempo_execucao:.2f} segundos")
