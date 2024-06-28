"""Ejercicio 7: Leer 10 números enteros e imprimir su promedio, el mayor valor leído y en qué
posición se encontraba. Si se ingresó más de una vez sólo debe informar la primera."""

mayor=0
for i in range(10):
    numero=(int(input("Ingrese numero: ")))
    if mayor < numero:
        mayor = numero
    numero += numero
    promedio = numero / 10



print("La suma es ",numero)
print("Promedio es ",promedio)
print("Mayor es ",mayor)
