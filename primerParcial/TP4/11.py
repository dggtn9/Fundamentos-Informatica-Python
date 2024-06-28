"""Ejercicio 11: Realizar un programa que lea un número natural H e imprima un mensaje indicando
si H es primo o no. Se dice que un número es primo cuando sólo es divisible
por sí mismo y por la unidad."""

h=int(input("Ingresa un numero natural"))
if h//h == 1 and h//1==h :
    print("Numero es primo")
else:
    print("no es primo")
