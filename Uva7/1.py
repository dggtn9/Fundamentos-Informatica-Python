"""
Escribir una función que solicite ingresar una serie de números entre a y b y guardarlos en una lista.
En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error y solicitará un nuevo número.
Para finalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y devuelve la lista cargada
(o vacía, si el usuario no ingresó nada) como valor de retorno.
"""

def ingresar_numeros():
    a = 1
    b = 100
    lista = []
    numero = int(input("Ingresa un numero"))
    while (numero < a or numero > b) and numero!=-1:
        numero = int(input("Error, Ingresa un numero entre a y b"))

    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingresa un numero"))
        while (numero < a or numero > b) and numero!=-1:
            numero = int(input("Error, Ingresa un numero entre a y b"))
    return lista


print(ingresar_numeros())
