"""Ejercicio 7: Leer un número correspondiente a un año e imprimir un mensaje indicando si es
bisiesto o no. Un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos
años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que
también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el
2000."""


anio = int(input("Ingresa un anio"))

if anio%4 == 0:
     if anio%100 == 0:
         if anio%400 != 0:
            print("no es bisiesto")
         else:
             print("Es bisiesto")
else:
     print("No es bisiesto")


