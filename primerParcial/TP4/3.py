"""Ejercicio 3: Realizar un programa para ingresar desde el teclado un conjunto de números y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un valor -1."""

numero = int(input("Ingresa un numero"))
numero_menor=0
numero_mayor=0
while numero != -1:
    numero = int(input("Ingresa un numero"))
    if numero>numero_mayor:
        numero_mayor=numero
    if numero<numero_menor:
        numero_menor=numero
print("Numero mayor es: ",numero_mayor)
print("Numero menor es: ", numero_menor)

