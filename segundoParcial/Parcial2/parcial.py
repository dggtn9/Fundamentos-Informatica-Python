"""
Una tienda de electrónicos dispone de 4 almacenes (1 a 4) y maneja
15 productos distintos (código de 3 cifras).
Ingresar primeramente los códigos de los productos y sus respectivas
cantidades en stock, mediante una función.

Por cada día, cada vez que se realiza una venta, se dispone de la siguiente
información:
- Nro. de almacén
- Código de producto
- Cantidad vendida. SOLO PUEDO VENDER CUANDO EL STOCK ES SUFICIENTE. Sino descartar
la venta con un error!.

Esta información finaliza con Nro. de almacén cero.
Validar todos los datos ingresados mediante funciones genéricas.

Con las informaciones anteriores, realizar e informar el siguiente resumen:
a) Un listado donde indique la cantidad de productos vendidos por código de
producto según el siguiente formato.
PRODUCTO CANTIDAD VENDIDA
xxxx      xxxx
xxxx      xxxx
Implementar una función para informar
b) Stock total restante de todos los productos, luego de procesar las ventas.
c) Producto/s NO vendidos
d) Nro./s de almacén/es con mínima cantidad de productos vendidos

Implementar función main() ** OPCIONAL **
UTILIZAR LA METODOLOGIA VISTA EN CLASE
NO USAR ESTRUCTURAS NO TRABAJADAS EN LA MATERIA
NO USAR CICLOS INFINITOS-RUPTURA DE CICLOS, NO USAR TUPLAS/DICCIONARIOS/CONJUNTOS
NO USAR VARIABLES GLOBALES
USAR LISTAS HOMOGENEAS. MODULARIZAR EL CODIGO"""

import random

def busqueda(lista,valorBuscado):
    pos=-1
    i=0
    while pos==-1 and i<len(lista):
        if lista[i]==valorBuscado:
            pos=i
        i+=1
    return pos

#carga que controla duplicados
def cargarListas(liCod,liStock):
    i=0
    while i<15:
        auxCod=random.randint(100,999)
        """
        auxCod=int(input("Ingrese un codigo de 3 cifras"))
        while auxCod<100 or auxCod>999:
            auxCod=int(input("Error,Ingrese un codigo de 3 cifras"))
        """
        posicion=busqueda(liCod,auxCod)
        #busqueda devuelve -1 si no encuentra el elemento
        #busqueda devuelve una posicion >=0 si encuentra el elemento
        if posicion ==-1:
            liCod.append(auxCod)
            liStock.append(random.randint(0,1000))
            """
            auxStock=int(input("Ingrese un stock"))
            while auxStock<0:
                auxStock=int(input("Error,Re-Ingrese un stock"))
            liStock.append(auxStock)
            """
            i+=1
        else:
            print("CODIGO DUPLICADO!")

#carga sin controlar duplicados
def cargaListas2(liCod,liStock):
    for i in range(15):
        liCod.append(random.randint(100,999))
        liStock.append(random.randint(0,1000))

def ingresaValidaRango(li,ls,texto):
    valor=int(input(texto))
    while valor<li or valor>ls:
        valor=int(input(texto))
    return valor

def listadoCantidadVendida(liCod,liCant):
    print("CODIGO\tCANTIDAD")
    for i in range(len(liCod)):
        print("%6d\t%8d" %(liCod[i],liCant[i]))
        #print(liCod[i],"   ",liCant[i])
    """
    LO QUE NO HAY QUE HACER ES
    print(liCod)
    print(liCant)"""

def listadoStock(liCod,liStock):
    print("CODIGO\t STOCK")
    for i in range(len(liCod)):
        print("%6d\t%8d" %(liCod[i],liStock[i]))
        #print(liCod[i],"   ",liStock[i])

def minimo(lista):
    """
    valMin=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<valMin:
            valMin=lista[i]
    return valMin"""

    for i in range(len(lista)):
        if i==0 or lista[i]<valMin:
            valMin=lista[i]
        """
        if i==0:
            valMin=lista[i]
        else:
            if lista[i]<valMin:
                valMin=lista[i]
        """
    return valMin

def main():
    CODIGOS=[]
    STOCK=[]
    CANTIDAD=[0]*15
    #CANTIDAD=[0,0,0,0,0,.....0]
    ALMACENES=[0]*4

    #cargar las listas en la funcion cargarListas
    #15 productos con codigos de 3 cifras SIN DUPLICADOS
    cargarListas(CODIGOS,STOCK)
    print(CODIGOS)
    print(STOCK)


    #PROCESAMIENTO
    """
    Por cada día, cada vez que se realiza una venta, se dispone de la siguiente
    información:
    - Nro. de almacén
    - Código de producto
    - Cantidad vendida. SOLO PUEDO VENDER CUANDO EL STOCK ES SUFICIENTE. Sino descartar
    la venta con un error!.

    Esta información finaliza con Nro. de almacén cero.
    Validar todos los datos ingresados mediante funciones genéricas."""

    auxAlmacen=random.randint(0,4)
    #auxAlmacen=ingresaValidaRango(0,4,"Ingrese un codigo de almacen")
    while auxAlmacen!=0:
        auxCod=random.randint(100,999)
        #auxCod=ingresaValidaRango(100,999,"Ingresa codigo valido")
        posicion=busqueda(CODIGOS,auxCod)
        if posicion >=0:#el codigo ingresado existe!
            auxCant=random.randint(1,1000)
            if STOCK[posicion]>=auxCant:#verifico si el stock es suficiente
                CANTIDAD[posicion]+=auxCant
                STOCK[posicion]-=auxCant
                ALMACENES[auxAlmacen-1]+=auxCant
            else:
                print("Error,stock insuficiente")
        else:
            print("Error producto no encontrado")
        auxAlmacen=random.randint(0,4)

    #listados o informes
    """
    a) Un listado donde indique la cantidad de productos vendidos por código de
    producto según el siguiente formato.
    PRODUCTO CANTIDAD VENDIDA
    xxxx      xxxx
    xxxx      xxxx
    Implementar una función para informar"""
    listadoCantidadVendida(CODIGOS,CANTIDAD)

    #b) Stock total restante de todos los productos, luego de procesar las ventas.
    listadoStock(CODIGOS,STOCK)

    #c) Producto/s NO vendidos
    print("PRODUCTOS NO VENDIDOS")
    for i in range(15):
        if CANTIDAD[i]==0:
            print("Producto no vendido ->", CODIGOS[i])

    #d) Nro./s de almacén/es con mínima cantidad de productos vendidos. Minimo
    #en funcion
    cantMinima=minimo(ALMACENES)
    print("La cantidad minima vendida en los almacenes es ",cantMinima)
    for i in range(4):
        if ALMACENES[i]==cantMinima:
            print("Almacen ",i+1," con cantidad minima")


if __name__=="__main__":
    main()
