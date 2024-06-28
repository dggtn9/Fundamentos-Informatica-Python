"""Ejercicio 8: Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no."""

dia= int(input("Ingrese un dia"))
mes=int(input("Ingrese un mes"))
anio=int(input("Ingrese un anio"))

if (dia>0 and dia <=31) and (mes>0 and mes<=12) and (anio>0):
    print("fecha correcta")

else:
    print("Datos incorrectos")

