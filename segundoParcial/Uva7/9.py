"""
Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
 utilizando búsqueda secuencial en una lista desordenada.
 La función debe devolver -1 si el elemento no se encuentra en la lista.

"""
import random

def crear_lista(a,b):
    lista = []
    for i in range (5):
        valor = random.randint(a, b)
        lista.append(valor)
    return lista

def busquedasecuencial(lista,dato):
    pos = -1
    i = 0
    while pos == -1 and i< len(lista):
        if lista[i] == dato:
            pos = i
            print("El dato", dato,"se encontró en la pos", pos)
        i += 1
    if pos == -1:
            print("No se encontro el dato  en ninguna posición.", pos)
    return pos
lista1 = crear_lista(1,10)
posicion = busquedasecuencial(lista1,8)

print(lista1)
print(posicion)
