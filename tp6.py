print("TP6")
"""Ejercicio 1: Escribir una función que reciba como parámetros dos números enteros. Calcular
y devolver el resultado de la multiplicación de ambos valores utilizando solamente
sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .
Ejercicio 2: Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante
multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar.
Por ejemplo 43 = 4 * 4 * 4.
Ejercicio 3: Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.
Ejercicio 4: Devolver True si el número entero recibido como primer parámetro es múltiplo
del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True
y esmultiplo(50, 3) devuelve False.
Ejercicio 5: Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o
0 según el valor recibido sea positivo, negativo o nulo.
Ejercicio 6: Escribir la función comparar(a, b) que reciba como parámetros dos números enteros
y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si
el primero es menor que el segundo. En este ejercicio debe aprovecharse la función
del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4)
devuelve -1.
Ejercicio 7: Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, basándose
en las siguientes fórmulas matemáticas:
· MCD(X,X) = X
· MCD(X,Y) = MCD(Y, X)
· Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
Ejemplo: MCD(40, 15) devuelve 5.
Ejercicio 8: La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente
fórmula de Newton:
donde a es una aproximación a n. Al aplicar repetidamente esta fórmula reemplazando
a por la aproximación obtenida en el paso anterior, se obtiene cada vez
una aproximación mejor. Desarrollar un programa que calcule la raíz cuadrada
aproximada de un número entero positivo n utilizando como primera aproximación
a n/2. Detener el proceso cuando la diferencia entre dos cálculos sucesivos
sea menor a 0,0001.

Ejercicio 9: Escribir una función que reciba como parámetros un número de día, un número
de mes y un número de año y devuelva la cantidad de días que faltan hasta fin
de mes. Luego desarrollar tres programas para:
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días que faltan hasta fin de año.
· Ingresar una fecha formada por tres enteros (día, mes y año) e imprimir
la cantidad de días transcurridos en ese año hasta esa fecha.
· Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir
cuánto tiempo transcurrió entre ambas, expresando el resultado en
años, meses y días.
Los tres programas deben realizar su trabajo a través de la función indicada al
comienzo.
Ejercicio 10: Extraer un dígito de un número. La función recibe como parámetros dos números
enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea
obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si
no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o
negativo. Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8)
devuelve -1.
Ejercicio 11: Obtener el dígito central de un número entero pasado como parámetro, sólo si la
cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo:
digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1."""