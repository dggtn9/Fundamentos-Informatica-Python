"""
Utilizando búsqueda binaria sobre una lista ordenada realizar la búsqueda de valores e informar si se encuentran o no en la lista,
finalizar las búsquedas con -1 e informar cuantas búsquedas fueron exitosas y en cuantas no se encontró el valor buscado.

Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. Validar que N sea menor o igual a 100.
"""

import random

def buscar_secuencial(lista,valor):
    encontrado = False
    i = 0
    while i<len(lista) and valor != lista[i]:
        i=i+1
    if i<len(lista):
        encontrado=True
    return encontrado
def crearlista():
    lista=[]
    n=int(input("Ingresa tamano de la lista"))
    while n<0 or n>100:
        n = int(input("Ingresa tamano de la lista entre 0 y 100"))
    valor = random.randint(0, 100)
    lista.append(valor)
    for i in range(1,n):
        valor = random.randint(0, 100)
        while buscar_secuencial(lista,valor)==True:
            valor = random.randint(0, 100)
        lista.append(valor)
    return lista
def metodoseleccion(lista):
    for i in range(0,len(lista)-1):
        for j in range (i+1,len(lista)):
            if lista[i]>lista[j]:
                aux = lista[i]
                lista[i]=lista[j]
                lista[j]=aux
def busquedaBinaria(lista,valor):
    pos=-1
    izq=0
    der=len(lista)
    der-=1
    while izq <=der and pos==-1:
        centro = (izq+der)//2
        if lista[centro]==valor:
            pos=centro
        elif valor>lista[centro]:
            izq=centro+1
        else:
            der=centro-1
    return pos

def __main__():
    busquedas_exitosas=0
    notfound=0
    lista1 = crearlista()
    metodoseleccion(lista1)
    print(lista1)
    for i in range (10):
        valor=random.randint(0,100)
        print("Buscando el valor: ",valor)
        if busquedaBinaria(lista1,valor)!=-1:
            busquedas_exitosas+=1
        else:
            notfound+=1

    print("Total busquedas exitosas: ", busquedas_exitosas)
    print("Total no encontrados: ", notfound)
if __name__=="__main__":
    __main__()





