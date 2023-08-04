def calcular_media(lista):
    if not lista:
        return 0
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
print("La media de los números es:", calcular_media(numeros))