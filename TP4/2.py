"""Ejercicio 2: Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar
la lectura de datos con -1."""

numero = int(input("Ingresa un numero"))
cantidad_numeros=1
while numero != -1:
    cantidad_numeros += 1
    numero = int(input("Ingresa un numero"))
if cantidad_numeros%2==0:
        print("cantidad par")
else:
        print("cantidad impar")


