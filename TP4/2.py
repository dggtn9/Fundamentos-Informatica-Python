"""Ejercicio 2: Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar
la lectura de datos con -1."""

while numero != -1:
    n=1
    es_impar= not es_impar
    numero = int(input("Leer numero entero"))
if n==0:
    print("no se ingresaron datos")
else:
    if es_impar:
        print("La cantidad de numeros ingresados es impar")
    else:
        print("La cantidad de numeros ingresados es par")


