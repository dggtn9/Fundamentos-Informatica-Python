"""Ejercicio 4: Desarrollar un programa que imprima la suma de los números impares comprendidos
entre 42 y 176."""

impar =0
for i in range (42,177):
    if i%2!=0:
        impar = impar+i
print(impar)
