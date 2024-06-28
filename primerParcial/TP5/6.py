"""Ejercicio 6: Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa
12345 se debe imprimir 5."""

entero=int(input("Ingresa numero entero"))
n=10
digitos=1
while entero%n != entero:
    n=n*10
    digitos+=1

print(digitos)