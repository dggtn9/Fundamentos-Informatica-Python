"""Ejercicio 10: El factorial de un número entero N mayor que cero se define como el producto
de todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular
el factorial de un número dado. Deberán rechazarse las entradas inválidas
(menores que 0)."""


factorial=int(input("Ingrese un numero para calcular su factorial"))

if factorial<0:
    print("Entrada invalida")
else:
    while factorial >0 and factorial <= n:
