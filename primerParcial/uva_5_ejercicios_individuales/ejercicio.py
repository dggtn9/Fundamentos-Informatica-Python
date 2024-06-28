"""
Una librería tiene en promoción 10 libros nuevos.
De los libros se conoce el CODIGO (númerico de 4 cifras) y el NOMBRE (String)
Cargar los libros en una función cargar_libros

La libreria necesita saber cual es el libro mas pedido y el menos pedido.
Por cada día, anota que libro fue pedido.
Para eso se pide CODIGO de libro y la CANTIDAD de pedidos. La carga finaliza con el CODIGO 0
Si el codigo pedido no existe, mostrar un error indicando LIBRO INEXISTENTE.

DETERMINAR:
a) Libro mas pedido:
LIBRO PEDIDOS
#####  ###

b) Libro menos pedido:
LIBRO PEDIDOS
#####  ###
"""


def validar(inicial,final,texto):
    v=int(input(texto))
    while v<inicial or v>final:
        v = int(input(texto))
    return v

def validarExcepcion(inicial,final,excepcion,texto):
    v = int(input(texto))
    while (v < inicial and v != excepcion)or v > final :
        v = int(input(texto))
    return v


def cargar_libros(lista1,lista2):
    for i in range(3):
        codigo=validar(1000,9999,"iNGRESA CODIGO DE 4 CIFRAS")
        nombre=input("Ingresa nombre")
        lista1.append(codigo)
        lista2.append(nombre)

def busqueda(lista,valor):
    pos = -1
    i = 0
    while pos == -1 and i < len(lista):
        if lista[i] == valor:
            pos = i
        i += 1
    return pos


def main():
    codigos=[]
    nombres=[]
    cantidad_libros=[0]*3
    cargar_libros(codigos,nombres)
    codigo = validarExcepcion(1000, 9999, 0,"iNGRESA CODIGO DE 4 CIFRAS o cero para salir del programa")
    while codigo!=0:
        cantidad=input("Ingresa la cantidad de libros")
        posicion=busqueda(codigos,codigo)
        cantidad_libros[posicion]+=1
        if posicion==-1:
            print("LIBRO INEXISTENTE")

        codigo = validarExcepcion(1000, 9999, 0,"iNGRESA CODIGO DE 4 CIFRAS")




if __name__ == "__main__":
    main()