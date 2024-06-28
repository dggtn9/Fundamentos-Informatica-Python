"""La universidad necesita un sistema para cargar las notas finales de los alumnos.
 Los datos para ingresar son: Legajo (número positivo), mes (solamente se aceptan los números 3, 6 y 12)
 y nota (número entre 1 y 10). La carga de datos termina al ingresar -1 como legajo. Validar los datos pedidos.
Al finalizar, informar:
Cantidad de alumnos que promocionaron la materia (nota 7 o más).

Cantidad de alumnos que aprobaron (nota 4 o más).

Porcentaje de alumnos reprobados.

Promedio de notas obtenidas en el mes 6."""

promocionados=0
aprobados=0
reprobados=0
notas_mes_6=0
total_notas=0
notas=0
legajo = int(input("Ingresa tu legajo"))
while legajo < 0 and legajo != -1:
    legajo = int(input("Ingresa tu legajo"))
while legajo!=-1:
    total_notas+=1
    mes = int(input("Ingresa mes"))

    while  mes !=3 and mes !=6 and mes!=12 :
        mes=int(input("Ingresa mes"))

    nota = int(input("Ingresa nota"))

    while nota < 1 or nota > 10:
       nota=int(input("Ingresa nota"))
    if mes==6:
        notas+=nota
        notas_mes_6+=1
    if nota >=7:
        promocionados+=1
    elif nota >=4 and nota<7:
       aprobados+=1
    else:
       reprobados+=1
    legajo = int(input("Ingresa tu legajo"))
    while legajo < 0 and legajo != -1:
        legajo = int(input("Ingresa tu legajo"))
porcentaje_reprobados=reprobados/total_notas
promedio_mes_6=notas/notas_mes_6
print("Promocionados:",promocionados)
print("aprobados: ",aprobados)
print("reprobados: ",reprobados)
print("Promedio de las notas en el mes 6: ",promedio_mes_6)