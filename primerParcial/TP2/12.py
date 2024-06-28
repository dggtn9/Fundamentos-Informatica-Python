"""Ejercicio 12: Escribir un programa para convertir un número binario de 4 cifras en un
número decimal. El número binario se ingresa como un solo número
entero de cuatro dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente.
Este exponente se obtiene de la posición que ocupa el dígito
dentro del número, comenzando desde la derecha con la posición 0. Todos
estos resultados se suman para obtener el valor final. Ejemplo: Convertir
1011 a decimal:
13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11"""

print("EJERCICIO 12 :")


numero_binario=int(input("Ingrese numero binario de 4 cifras"))

b4 = (numero_binario//1000)*2**3
resto = numero_binario % 1000
b3 = (resto // 100)*2**2
resto = resto % 100
b2 = (resto // 10)*2**1
resto = resto % 10
b1 = (resto//1)*2**0
print(b4+b3+b2+b1)

