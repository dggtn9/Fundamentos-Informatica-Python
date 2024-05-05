"""Ejercicio 2: Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante
multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar.
Por ejemplo 43 = 4 * 4 * 4."""


def elevar( a,b):
    resultado = 1
    if b!=0:
        if b>0:
            base=a
            exponente=b
        else:
            base=-1/a
            exponente=-1*b
        for i in range(int(exponente)):
            resultado*=base
    return resultado


r=elevar(float(4),float(-3))
print("Resultado de la multipplicación es igual a: ",r)