"""
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

lista1=crearlista()
print(lista1)