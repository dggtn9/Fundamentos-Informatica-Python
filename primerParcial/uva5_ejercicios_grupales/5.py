"""La universidad necesita un sistema para cargar las notas finales de los alumnos. Los datos para
ingresar son: Legajo (número positivo), mes (solamente se aceptan los números 3, 6 y 12)
y nota (número entre 1 y 10). La carga de datos termina al ingresar -1 como legajo. Validar los datos
pedidos. Al finalizar, informar:
Cantidad de alumnos que promocionaron la materia (nota 7 o más).

Cantidad de alumnos que aprobaron (nota 4 o más).

Porcentaje de alumnos reprobados.

Promedio de notas obtenidas en el mes 6."""
cantidad_promocionan=0
cantidad_reprobados=0
cantidad_aprueban=0
sumatoria_notas=0
cantidad_notas_mes_seis=0
legajo=int(input("ingresa numero de legajo"))
while legajo <0 and legajo != -1:
    legajo = int(input("ingresa numero de legajo"))
while legajo !=-1:
    mes = int(input("Ingrese numero de mes"))
    while mes!=3 and mes!=6 and mes!=12:
        mes=int(input("Ingrese numero de mes"))
    nota = int(input("Ingrese nota"))
    while nota <1 or nota >10:
        nota=int(input("Ingrese nota"))
    if nota >=7:
        cantidad_promocionan+=1
    elif nota >=4:
        cantidad_aprueban+=1
    else:
        cantidad_reprobados+=1
    if mes==6:
        sumatoria_notas+=nota
        cantidad_notas_mes_seis+=1
    legajo = int(input("ingresa numero de legajo"))
    while legajo < 0 and legajo != -1:
        legajo = int(input("ingresa numero de legajo"))
cantidad_total=cantidad_reprobados+cantidad_promocionan+cantidad_aprueban
promedio_reprobados=cantidad_reprobados/cantidad_total
promedio_notas_mes_seis=sumatoria_notas/cantidad_notas_mes_seis

print("Cantidad de alumnos que promocionaron la materia (nota 7 o más): ",cantidad_promocionan)

print("Cantidad de alumnos que aprobaron (nota 4 o más): ",cantidad_aprueban)

print("Porcentaje de alumnos reprobados: ",promedio_reprobados*100,"%")

print("Promedio de notas obtenidas en el mes 6: ",promedio_notas_mes_seis)