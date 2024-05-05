"""Ejercicio 8: La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente
fórmula de Newton:
donde a es una aproximación a n. Al aplicar repetidamente esta fórmula reemplazando
a por la aproximación obtenida en el paso anterior, se obtiene cada vez
una aproximación mejor.
 Desarrollar un programa que calcule la raíz cuadrada
aproximada de un número entero positivo n utilizando como primera aproximación
a n/2. Detener el proceso cuando la diferencia entre dos cálculos sucesivos
sea menor a 0,0001.
"""

def newton(n,a):
    return ((n/a)+a)/2
def calcular(n):
       a=n/2
       raiz=newton(n,a)
       a=raiz
       raiz2 = newton(n,a)

       while (raiz2-raiz)>0.0001:
           a = raiz2
           raiz=raiz2
           raiz2=newton(n,a)

       return raiz2

r=calcular(16)

print(r)



