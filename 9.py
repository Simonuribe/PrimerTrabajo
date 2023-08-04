def encontrar_maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = [10, 5, 20, 15, 30]
maximo, minimo = encontrar_maximo_minimo(numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)