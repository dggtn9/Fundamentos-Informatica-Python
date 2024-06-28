"""Un técnico tiene la responsabilidad dentro de una empresa en el mantenimiento
y gestión de los equipos conectados a la red que utilizan los administrativos.
Dado que los equipos tienen diferentes tipos de fallas quiere reportar los
problemas para poder evaluar una solución a ellos
Para ello le pidió al Departamento de Sistemas que le diseñen un programa que:

1.Solicite el ingreso por teclado del código interno del equipo (número entero de 4 dígitos).

2.Luego se le solicitara al usuario que ingrese el tipo de falla encontrado:
 “P” error en periférico, “M” error en memoria, “D” error de disco, “N” error no identificado.

3.EL ingreso de los datos finalizara con el número de equipo -99.

4.Informar:
-Cuantas fallas de cada tipo de detectaron y cuál fue la de mayor ocurrencia"""

tipo_p = 0
tipo_m = 0
tipo_d = 0
tipo_n = 0

codigo_interno = int(input("Ingrese código de 4 digitos: "))
while codigo_interno < 999 or codigo_interno > 9999:
    codigo_interno = int(input("Ingrese código de 4 digitos: "))

while codigo_interno != -99:
    tipo_de_falla = input(
        "ingrese tipo de falla 'P' error en periférico, 'M' error en memoria, 'D' error de disco, 'N' error no identificado: ")
    while tipo_de_falla != 'P' and tipo_de_falla != 'M' and tipo_de_falla != 'D' and tipo_de_falla != 'N':
        tipo_de_falla = input(
            "ingrese tipo de falla 'P' error en periférico, 'M' error en memoria, 'D' error de disco, 'N' error no identificado: ")

    if tipo_de_falla == 'P':
        tipo_p += 1
    elif tipo_de_falla == 'M':
        tipo_m += 1
    elif tipo_de_falla == 'D':
        tipo_d += 1
    else:
        tipo_n += 1
    codigo_interno = int(input("Ingrese código de 4 digitos: "))
    while (codigo_interno < 1000 or codigo_interno > 10000) and codigo_interno != -99:
        codigo_interno = int(input("Ingrese código de 4 digitos: "))
if tipo_p > tipo_m and tipo_p > tipo_d and tipo_p > tipo_n:
    falla_mayor = 'P'
elif tipo_m > tipo_p and tipo_m > tipo_d and tipo_m > tipo_n:
    falla_mayor = 'M'
elif tipo_d > tipo_m and tipo_d > tipo_p and tipo_d > tipo_n:
    falla_mayor = 'D'
else:
    falla_mayor = 'N'

print("Se detectaron: ", tipo_p, " fallas tipo P, ", tipo_m, " fallas tipo M ", tipo_d, " fallas tipo D ", tipo_n,
      " fallas tipo N")
print("La falla con mayor ocurrencia fue ", falla_mayor)



