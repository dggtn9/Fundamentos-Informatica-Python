"""Ejercicio 9: Se desea analizar cuántos autos circulan con patente con numeración par y
cuántos con numeración impar en un día. Escribir un programa que permita ingresar
la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe
cuántos vehículos pasaron con numeración par y cuántos con numeración impar."""

patente = int(input("Ingrese la terminacion de su patente"))
cantidad_par=0
cantidad_impar=0
while patente != -1:
    patente = int(input("Ingrese la terminacion de su patente"))
    if patente%2==0:
        cantidad_par += 1
    else:
        cantidad_impar += 1

print("Cantidad par",cantidad_par)
print("Cantidad impar",cantidad_impar)
