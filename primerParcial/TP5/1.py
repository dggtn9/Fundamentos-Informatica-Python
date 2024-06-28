""" Ejercicio 1: Leer números que representan edades de un grupo de personas, finalizando la
lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18
años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válida una
edad entre 0 y 100)."""

edad=int(input("Ingresa edad"))
cantidad_menores=0
cantidad_mayores=0

while edad !=-1:
    if edad>0 and edad<=100:
        if edad <18:
              cantidad_menores+=1
        else:
              cantidad_mayores+=1
    edad = int(input("Ingresa edad"))

cantidad_total=cantidad_mayores+cantidad_menores
promedio_menores= (cantidad_mayores)/cantidad_total
promedio_mayores= (cantidad_mayores)/cantidad_total

print("Cantidad menores de edad",cantidad_menores)
print("Cantidad mayores de edad",cantidad_mayores)
print("Promedio de edad menores",promedio_menores)
print("Promedio de edad mayores",promedio_mayores)
