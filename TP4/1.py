""" Ejercicio 1: Realizar un programa para ingresar desde el teclado un conjunto de números. Al
finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lectura
con -1."""
numero = int(input("Ingresa un numero"))
lei_primer_numero = False

while numero != -1:
    if lei_primer_numero == True:
        ultimo_numero = numero
    else:
       primer_numero = numero
       lei_primer_numero = True
    numero = int(input("Ingresa un numero"))

print("primer numero = ",primer_numero)
print("ultimo numero = ",ultimo_numero)

