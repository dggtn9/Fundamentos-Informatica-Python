"""
Escribir una función para crear una lista con N números al azar en un rango de valores que se recibe por parámetro.
 La función devuelve la lista cargada (o vacía si el rango indicado no es válido)
"""
import random


def crear_lista(a,b):
    lista = []
    for i in range (5):
        valor = random.randint(a, b)
        lista.append(valor)
    return lista


a = int(input("Ingrese numero con el que inicia el rango"))
b = int(input("Ingrese numero con el que finaliza el rango"))
lista = crear_lista(a,b)
print(lista)


