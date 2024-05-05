"""Ejercicio 1: Escribir una función que reciba como parámetros dos números enteros. Calcular
y devolver el resultado de la multiplicación de ambos valores utilizando solamente
sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 ."""


def multiplicar(a, b):
    resultado = 0
    for i in range(b):
        resultado+=a
    return resultado

r=multiplicar(4,4)
print("Resultado de la multipplicación es igual a: ",r)
