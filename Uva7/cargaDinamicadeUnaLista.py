"""
Iniciar nuetsro programa cargando una lista con valores random o aleatorios con
numeros de 3 cifras,finalizar la carga con valor 99.
Realizar la carga en una funcion cargalista
realizar una funcion mostrar lista
realizar una funcion que
 calcule la suma de los elementos de una lista
"""

import random
def cargarLista(lista):
    valor=random.randint(99,999)
    while valor!=99:
        lista.append(valor)
        valor = random.randint(99, 999)
def mostrarLista(lista):
    print("============")
    print("LISTADO DE NUMEROS")
    print("============")

    for i in range(len(lista)):
        print(lista[i],end="-")

def suma(lista):
    resu=0
    for i in range (len(lista)):
        resu+=lista[i]
        return resu
def maximo(lista):
    maximo=lista[0]
    for i in range (1,len(lista)):
        if lista[i]>maximo:
            maximo=lista[i]
        return maximo
#otra manera de def maximo:
"""
def maximo(lista):
    for i in range(len(lista)):
    if i==0 or lista[i]>maximo:
    maximo=lista[i]
    return maximo
"""
def main():
    listaNumeros=[]
    cargarLista(listaNumeros)
    print(listaNumeros)
    print("La lista tiene: ",len(listaNumeros),"elementos")
    mostrarLista(listaNumeros)
    acum=suma(listaNumeros)

    if len(listaNumeros)>0:
        max = maximo(listaNumeros)
        print("El valor maximo es: ",max)
        promedio=acum/len(listaNumeros)
        print("El valor promedio es",promedio)
    else:
        print("No se ingresaron datos")
if __name__=="__main__":
    main()