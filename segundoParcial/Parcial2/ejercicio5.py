"""
#Ejercicio 4: Escribir una función para contar cuántas veces aparece un valor dentro de la
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
#un número entero."""

def contarApariciones(lista,numero):
    cantidad=0
    for i in range(len(lista)):
        if lista[i]==numero:
            cantidad+=1
    return cantidad


