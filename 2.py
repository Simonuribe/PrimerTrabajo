import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

radio = float(input("Ingresa el radio del círculo: "))
print("El área del círculo es:", calcular_area_circulo(radio))