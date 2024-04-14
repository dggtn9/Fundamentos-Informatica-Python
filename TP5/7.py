"""Ejercicio 7: Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo,
si se ingresa 1234 debe mostrar 4321."""

numero = int(input("Leer numero entero"))
n=10
digitos=1
resto=numero
while numero%n != numero:

    print(resto%10)
    n = n * 10
    digitos+=1
    resto=resto//10
print(resto % 10)

