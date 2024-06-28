"""Un banco otorga a sus clientes una categoría de acuerdo al nivel de depósitos mensuales. Desarrollar un programa
que permita ingresar
importes positivos hasta que se ingrese -1. Si la suma de esos importes es mayor a 1.000.000 la categoría será “Oro”,
si está entre 500.000 y 1.000.000 la categoría será “Platino” y en el resto de los casos “Estándar”.
Mostrar la categoría. Realizar la prueba de escritorio para comprobar el correcto funcionamiento del programa.
"""
importe=int(input("Ingrese importe"))
importe_total=0
categoria=0
while importe !=-1:
    importe_total+= importe
    importe = int(input("Ingrese importe"))
if importe_total>=1000000:
 categoria="oro"
elif (importe_total >= 500000) and (importe_total<=1000000):
 categoria = "platino"
else:
 categoria="estandar"

print("Importe total es: ",importe_total)
print("Categoria es ",categoria)


