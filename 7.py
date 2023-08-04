def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
print("La temperatura en Celsius es:", fahrenheit_a_celsius(fahrenheit))