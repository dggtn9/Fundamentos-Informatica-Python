"""Ejercicio 7: Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo,
si se ingresa 1234 debe mostrar 4321."""

numero = int(input("Leer numero entero"))

for numero in range (numero-1,numero,-1):
    print(numero)
