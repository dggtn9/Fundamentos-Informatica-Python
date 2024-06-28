"""
#Ejercicio 1
#Escribir una función para ingresar desde el teclado una serie de números entre A
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la
# función mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B."""

def cargarNumerosEntreExtremos(a,b):
    lista=[]

    if a>b:
        aux=a
        a=b
        b=aux
    bandera=True
    while bandera:
        num=int(input("Ingrese un número\n"))
        if num==-1:
            bandera=False
        elif num<a or num>b:
            print("Valor inválido")
        else:
            lista.append(num)
    return lista






