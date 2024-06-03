"""
Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista: métodos de selección, inserción y burbujeo.
 ¿Qué cambia para ordenar en forma descendente?
"""

import random

def __main__():
    def crear_lista(a,b):
        lista = []
        for i in range (5):
            valor = random.randint(a, b)
            lista.append(valor)
        return lista
    lista1 = crear_lista(1, 5)
    lista2 = crear_lista(5, 10)
    lista3 = crear_lista(10, 15)
    #Métodos de ordenamiento

    #método de selección

    def metodoseleccion(v):  # v es la variable
        largo = len(v)
        for i in range(len(v) - 1):
            for j in range(i + 1, largo):
                if v[i] > v[j]:  # ascendente > o descendente <
                    aux = v[i]
                    v[i] = v[j]
                    v[j] = aux



    #método de intercambio -burbujeo
    def metodointercambio(v):
        n = len(v)
        # Recorre todo el arreglo
        for i in range(1,n):
            # Últimos i elementos ya están en su lugar
            for j in range(n-1):
                # Intercambia si el elemento encontrado es mayor que el siguiente elemento
                if v[j] > v[j + 1]:
                    aux =v[j]
                    v[j]=v[j+1]
                    v[j+1]=aux


    #metodo de insercion:
    def metodoinsercion(lista):
        # Recorre el arreglo desde el segundo elemento hasta el final
        for i in range(1, len(lista)):
            # Guarda el valor actual
            valorInsertar = lista[i]
            # Inicializa la variable j que apuntará al índice anterior al actual
            j = i
            # Desplaza los elementos del arreglo que son mayores que el valor actual
            # a una posición adelante de su posición actual
            while j >0 and lista[j-1]>valorInsertar:
                lista[j] = lista[j-1]
                j -= 1
            # Coloca el valor actual en su posición correcta
            lista[j ] = valorInsertar

    metodoseleccion(lista3)
    metodointercambio(lista2)
    metodoinsercion(lista1)
    print("Lista ordenada por insercion: ",lista1)
    print("Lista ordenada por intercambio: ",lista2)
    print("Lista ordenada por seleccion: ",lista3)

if __name__=="__main__" :
 __main__()
