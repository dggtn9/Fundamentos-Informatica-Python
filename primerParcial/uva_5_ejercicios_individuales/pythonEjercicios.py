""""
EJEMPLO 1:
---------

Un Comercio tiene 5 vendedores
De cada vendedor se conoce su DNI
Realizar la carga de los vendedores en una funcion cargar_vendedores.
El DNI debe ser un numero entre 30.000.000 y 50.000.000

Por cada día, cada vez que el comercio realiza una venta se pide la siguiente informacion:
DNI del vendedor
Monto de la venta (Debe ser un valor mayor a cero. Validar esto en una funcion validar_mayor)
La carga finaliza con DNI = 0

DETERMINAR:
a) Recaudacion total
b) Informar la cantidad de ventas de cada vendedor
VENDEDOR      CANTIDAD_DE_VENTAS
##.###.###           #
##.###.###           #
##.###.###           #
"""


def validar(inicio,fin,texto):
    v=int(input(texto))
    while v<inicio or v>fin :
        v=int(input(texto))
    return v
def validar2(inicio,fin,excepcion,texto):
    v=int(input(texto))
    while v<inicio or v>fin and v!=excepcion:
        v=int(input(texto))
    return v


def validar_mayor(valor,texto):
    v = int(input(texto))
    while v < valor:
        v = int(input(texto))
    return v
def cargar_vendedores(lista1,lista2):
    for i in range(5):
        vendedores=validar(1,5,"Ingresa numero de vendedores")
        print("aaaaaa")
        dni=validar2(30000000,50000000,0,"Ingresa numero de dni")
        lista1.append(vendedores)
        lista2.append(dni)

def imprimir(lista1, lista2, titulo):
    print(titulo)
    for i in range(lista1):
        print(lista1[i], " ", lista2[i], end=" ")

def busqueda(lista,valor):
    pos=-1
    i=0
    while i<len(lista) and pos==-1:
        if lista[i]==valor:
            pos=i
        i+=1
    return pos

cant=0
vendedores=[]
dnis=[]
cargar_vendedores(vendedores,dnis)
cantidad_ventas=[0]*5
recaudacion_total=0
dnis_con_ventas = []
dni = validar2(30000000, 50000000, 0,"Ingresa numero de vendedores")
while dni!=0:
    monto=validar_mayor(0,"Ingresa monto de la venta")

    if busqueda(dnis,dni)!=-1:
        cantidad_ventas[busqueda(dnis,dni)]+=1
        cant+=1

    recaudacion_total += monto
    dni = validar(30000000, 50000000, 0,"Ingresa numero de dni")



imprimir(vendedores,cantidad_ventas,"VENDEDOR      CANTIDAD_DE_VENTAS ")
print("Recaudacion total: ",recaudacion_total)