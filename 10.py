def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

num = int(input("Ingresa un número: "))
print("El factorial de", num, "es:", factorial(num))