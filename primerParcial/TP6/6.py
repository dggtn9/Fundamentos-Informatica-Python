""" Ejercicio 6: Escribir la función comparar(a, b) que reciba como parámetros dos números enteros
y devuelva 1 si el primero es mayor que el segundo,
0 si son iguales
o -1 si el primero es menor que el segundo.

En este ejercicio debe aprovecharse la función
del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4)
devuelve -1."""


def comparar(a,b):
   if a >b:
       resultado=1
   elif a<b:
       resultado=-1
   else:
       resultado=0
   return resultado

r=comparar(9,10)

print(r)

