"""
Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa.
Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones que ocupe.
La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.


"""
import random

def ingresar_numeros():
    lista = []
    numero = random.randint(0,100)
    while numero!=0:
        lista.append(numero)
        print(numero)
        numero = random.randint(0, 100)
    return lista

def obtener_minimo(lista):
    minimo=lista[0]
    for i in range (1,len(lista)):
        if lista[i]<=minimo:
            minimo=lista[i]
    return minimo

def posicion(minimo,lista):
    posiciones=[]
    for i in range(1,len(lista)):
         if minimo == lista[i]:
            posiciones.append(i)
    return posiciones


lista1 = ingresar_numeros()
valor_minimo = obtener_minimo(lista1)
lista_posiciones = posicion(valor_minimo,lista1)

print("Lista: ",lista1)
print("valor_minimo: ",valor_minimo)
print("posiciones: ",lista_posiciones)


