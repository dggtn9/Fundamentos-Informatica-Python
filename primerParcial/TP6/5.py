"""Ejercicio 5: Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o
0 según el valor recibido sea positivo, negativo o nulo.
"""

def signo (a):
    if a >0:
        resultado=1
    elif a <0:
        resultado=-1
    else:
        resultado=0

    return resultado

r= signo(5)
print(r)