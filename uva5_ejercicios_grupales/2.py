"""Un banco otorga a sus clientes una categoría de acuerdo al nivel de depósitos mensuales.
 Desarrollar un programa
que permita ingresar importes positivos hasta que se ingrese -1.

Si la suma de esos importes es mayor a 1.000.000
 la categoría será “Oro”, si está entre 500.000 y 1.000.000 la categoría será “Platino” y en el resto de los casos 
 “Estándar”. Mostrar la categoría. Realizar la prueba de escritorio para comprobar el correcto funcionamiento 
 del programa."""

sumatoria=0
importe_a_ingresar=int(input("Ingresa importe"))
while importe_a_ingresar <0 and importe_a_ingresar != -1:
    importe_a_ingresar = int(input("Ingresa importe"))

while importe_a_ingresar !=-1:
    sumatoria += importe_a_ingresar
    importe_a_ingresar = int(input("Ingresa importe"))
    while importe_a_ingresar < 0 and importe_a_ingresar != -1:
        importe_a_ingresar = int(input("Ingresa importe"))
if sumatoria > 500000 and sumatoria < 1000000:
    categoria = "platino"
elif sumatoria > 1000000:
    categoria = "oro"
else:
    categoria = "estandar"

print("Categoria es: ",categoria)
