"""Ejercicio 4: Devolver True si el número entero recibido como primer parámetro es múltiplo
del segundo, o False en caso contrario. Ejemplo: es multiplo(40, 8) devuelve True
y esmultiplo(50, 3) devuelve False."""


def calcular(a,b):
    if b==0:
         resultado="Error"
    else:
        if a%b == 0:
           resultado =True
        else:
           resultado = False
    return resultado

r=calcular(7,7)

print(r)